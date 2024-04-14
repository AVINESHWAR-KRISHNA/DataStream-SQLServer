from confluent_kafka import Producer

# Kafka broker configuration
conf = {
    'bootstrap.servers': 'localhost:29092',  # Replace with your Kafka broker address
    'client.id': 'demo-producer',
}

# Create Kafka producer
producer = Producer(conf)

# Kafka topic to publish messages to
topic = 'demo-topic01'

# Produce messages
for i in range(5):
    value = f'Message {i}'
    producer.produce(topic, value=value)
    print(f'Produced message: {value}')

# Flush producer
producer.flush()
print('Message production completed.')
