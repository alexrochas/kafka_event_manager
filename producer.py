from kafka import SimpleProducer, SimpleClient
import json


def send_message(message, kafka_url='localhost:9092', topic='ec_events_v1'):
    producer = SimpleProducer(SimpleClient(kafka_url))
    json_message = json.dumps(message)
    return producer.send_messages(topic, json_message.encode())
