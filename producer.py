from kafka import KafkaProducer
from kafka.errors import KafkaError
import json


def send_message(message, kafka_url='localhost:9092', topic='inputTopic'):
    print('Trying to send message to topic %s' % topic)
    producer = KafkaProducer(bootstrap_servers=[kafka_url])
    json_message = json.dumps(message)
    future = producer.send(topic, json_message.encode())

    # Block for 'synchronous' sends
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        # Decide what to do if produce request failed...
        print('Error sending to Topic')
        pass

    print('Message sent')
    return record_metadata
