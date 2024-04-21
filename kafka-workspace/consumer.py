from confluent_kafka import Consumer, KafkaError
import json
from prettytable import PrettyTable

# Kafka broker configuration
conf = {
    'bootstrap.servers': 'localhost:29091,localhost:29092,localhost:29093',
    'group.id': 'demo-consumer',
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': 'true'  # Disable auto commit
}

# Create Kafka consumer
consumer = Consumer(conf)

# Kafka topics to consume messages from
topics = ['sqlserver1-.demo-01.dbo.customers', 'sqlserver1-.demo-02.dbo.demo_emp']

# Subscribe to topics
consumer.subscribe(topics)

try:
    while True:
        # Poll for messages
        msg = consumer.poll(1.0)  # Adjust the timeout as needed
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                print(f"Reached end of partition {msg.topic()} [{msg.partition()}]")
            else:
                # Other error
                print(f"Error occurred: {msg.error().str()}")
                continue

        # Decode message value if it's JSON
        try:
            value = msg.value().decode('utf-8')  # Assuming the message value is in utf-8 encoded bytes
            value = json.loads(value)
        except json.JSONDecodeError:
            value = msg.value().decode('utf-8')  # If not JSON, decode the value

        # Print message details
        print(f"Received message:\nKey: {msg.key()}\nValue: {value}\nPartition: {msg.partition()}")

except KeyboardInterrupt:
    pass
finally:
    # Close consumer
    consumer.close()
    print('Consumer closed.')