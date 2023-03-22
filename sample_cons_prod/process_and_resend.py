from kafka import KafkaConsumer, KafkaProducer
import json
import numpy as np

consumer = KafkaConsumer('exo1', bootstrap_servers='51.38.185.58:9092',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
producer = KafkaProducer(bootstrap_servers='51.38.185.58:9092',
                         value_serializer=lambda m: json.dumps(m).encode('utf-8'))

for msg in consumer:
    data = msg.value
    data_arr = np.array(data['data'])
    sum_values = np.sum(data_arr)
    print("message recu puis transmis :", sum_values)

    processed_msg = {"sum": int(sum_values)}
    producer.send('processed', processed_msg)
    producer.flush()
