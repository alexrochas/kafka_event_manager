import os
import producer
import consumer
import json
from flask import Flask, request, jsonify, Response

app = Flask(__name__)
BASE_DIR = os.path.dirname(__file__)


@app.route('/consume', methods=['GET'])
def consume():
    commit = request.args.get('auto_commit')
    return_ = consumer.consume(auto_commit=commit)
    return Response(json.dumps(return_),  mimetype='application/json')


@app.route('/produce', methods=['POST'])
def produce():
    json_event = request.json
    producer.send_message(json_event)
    return ''


if __name__ == '__main__':
    app.run()
