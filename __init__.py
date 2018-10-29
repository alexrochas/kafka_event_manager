import os
import producer
import consumer
import json
from flask import Flask, request, Response

app = Flask(__name__)
BASE_DIR = os.path.dirname(__file__)


@app.route('/consume', methods=['GET'])
def consume():
    commit = request.args.get('auto_commit')
    topic = request.args.get('topic')
    return_ = consumer.consume(auto_commit=commit, topic=topic)
    return Response(json.dumps(return_),  mimetype='application/json')


@app.route('/produce', methods=['POST'])
def produce():
    topic = request.args.get('topic')
    json_event = request.json
    producer.send_message(json_event, topic=topic)
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8081')
