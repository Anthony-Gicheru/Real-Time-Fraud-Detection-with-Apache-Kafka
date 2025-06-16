from kafka import KafkaConsumer
import json
from rules import is_fraud

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

for msg in consumer:
    txn = msg.value
    if is_fraud(txn):
        print(f" Fraud detected!!! {txn}")
    else:
        print(f" Legitimate: {txn}")

