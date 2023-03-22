from kafka import KafkaProducer
import json

random_passenger = [[39.0, 0.0, 10.0, 0.0]]
jsonmsg = json.dumps(random_passenger)

producer = KafkaProducer(bootstrap_servers='51.38.185.58:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send('robin', value=random_passenger)
producer.flush()
