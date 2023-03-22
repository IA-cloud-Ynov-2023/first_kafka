from kafka import KafkaConsumer, KafkaProducer
import json
import numpy as np
import joblib


def load_model(model_name):
    model = joblib.load(model_name)
    return model


ml1_model = load_model("models/ml1.joblib")

consumer = KafkaConsumer('robin', bootstrap_servers='51.38.185.58:9092',
                         value_deserializer=lambda m: json.loads(
                             m.decode('utf-8')),
                         group_id="grouptest")

for msg in consumer:
    data = msg.value
    predictions = ml1_model.predict(data)[0]
    print("Predictions :", predictions)
