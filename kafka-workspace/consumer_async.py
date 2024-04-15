from confluent_kafka import Consumer, KafkaError
import json
from prettytable import PrettyTable
import asyncio

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

async def process_message(msg):
    try:
        _msg = json.loads(msg.value())
        
        payload = _msg.get('payload', {})
        source = payload.get('source', {})
        
        # Unpack the payload and source dictionaries
        op = payload.get('op')
        schema = source.get('schema')
        table = source.get('table')
        db = source.get('db')

        # Check conditions using dictionary unpacking
        if op == 'c' and schema == 'dbo' and table == 'customers' and db == 'demo-01':
            after_value = payload.get('after')
            
            table = PrettyTable(['Key', 'Value'])
            table.add_row(['After', json.dumps(after_value)])
            table.add_row(['DB', db])
            table.add_row(['Table', table])
            table.add_row(['Schema', schema])

            print(table)

    except json.JSONDecodeError as e:
        print(f"Error decoding message: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

async def consume():
    try:
        while True:
            msg = consumer.poll(0.0)
            if msg is None:
                continue
            if msg.error():
                print(f"Consumer error: {msg.error()}")
            elif msg.value() is not None:
                # Run process_message asynchronously
                asyncio.create_task(process_message(msg))
    except KeyboardInterrupt:
        print("Stopping consumer...")
    finally:
        consumer.close()
        print('Consumer closed.')

# Start the event loop and run the consume coroutine
async def main():
    await consume()

if __name__ == "__main__":
    asyncio.run(main())
