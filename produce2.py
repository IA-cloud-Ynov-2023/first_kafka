from kafka import KafkaProducer
import json

data = {"data": [[1, 2,], [3, 4]]}
jsonmsg = json.dumps(data)

producer = KafkaProducer(bootstrap_servers='51.38.185.58:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send('exo1', json.loads(jsonmsg))
producer.flush()
