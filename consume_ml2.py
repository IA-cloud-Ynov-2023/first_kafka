from kafka import KafkaConsumer, KafkaProducer
import json
import numpy as np
import joblib

consumer = KafkaConsumer('prediction_robin', bootstrap_servers='51.38.185.58:9092',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for msg in consumer:
    data = msg.value
    print("Predictions finale :", data)
