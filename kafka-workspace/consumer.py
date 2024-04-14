from confluent_kafka import Consumer, KafkaError
import json
from prettytable import PrettyTable

# Kafka broker configuration
conf = {
    'bootstrap.servers': 'localhost:29092',
    'group.id': 'demo-consumer',
    'auto.offset.reset': 'earliest'
}

# Create Kafka consumer
consumer = Consumer(conf)

# Kafka topic to consume messages from
topic = 'sqlserver1-.demo-01.dbo.customers'

# Subscribe to topic
consumer.subscribe([topic])

try:
    while True:
        # Poll for messages
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
        elif msg.value() is not None:
            try:
                _msg = json.loads(msg.value())
                
                #this sections needs to be modified as per the schema
                if _msg['payload']['op'] == 'c' and \
                   _msg['payload']['source']['schema'] == 'dbo' and \
                   _msg['payload']['source']['table'] == 'customers' and \
                   _msg['payload']['source']['db'] == 'demo-01':
                    
                    after_value = _msg['payload']['after']
                    db_value = _msg['payload']['source']['db']
                    table_value = _msg['payload']['source']['table']
                    schema_value = _msg['payload']['source']['schema']

                    table = PrettyTable(['Key', 'Value'])
                    table.add_row(['After', json.dumps(after_value)])
                    table.add_row(['DB', db_value])
                    table.add_row(['Table', table_value])
                    table.add_row(['Schema', schema_value])

                    print(table)

            except json.JSONDecodeError as e:
                print(f"Error decoding message: {e}")
            except KeyError as e:
                print(f"Key not found: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")

except KeyboardInterrupt:
    pass
finally:
    # Close consumer
    consumer.close()
    print('Consumer closed.')
