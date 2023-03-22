from kafka import KafkaConsumer
import json
import numpy as np

consumer = KafkaConsumer('exo1', bootstrap_servers='51.38.185.58:9092',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
for msg in consumer:
    data = msg.value
    data_arr = np.array(data['data'])
    sum_values = np.sum(data_arr)
    print("message final reçu :", sum_values)
