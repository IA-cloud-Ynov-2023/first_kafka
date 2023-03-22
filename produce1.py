from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='51.38.185.58:9092')
producer.send('exo1', b'coucou')
producer.flush()
