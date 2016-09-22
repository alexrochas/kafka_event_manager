from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                         group_id='events_ent',
                         enable_auto_commit=True)
consumer.subscribe(['ec_events_v1'])

for message in consumer:
    print(message)
