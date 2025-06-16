from kafka import KafkaProducer
import json
from faker import Faker
import random
import time

fake = Faker()
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
topic = 'transactions'

def generate_transaction():
    return {
        'user_id': fake.uuid4(),
        'amount': round(random.uniform(5, 5000), 2),
        'location': fake.country(),
        'timestamp': fake.iso8601()
    }

while True:
    transaction = generate_transaction()
    print(f"Sending: {transaction}")
    producer.send(topic, transaction)
    time.sleep(1)  # Simulate real-time flow
