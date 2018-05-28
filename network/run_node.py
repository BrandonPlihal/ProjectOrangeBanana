from blockchain.blockchain import Blockchain
from flask import Flask, jsonify, request
import requests
from blockchain.task import Task

node = Flask(__name__)

blockchain = Blockchain(100)

@node.route('/assign/task', methods=['POST', 'GET'])
def assign_task():
    print('assigning_task')
    if request.method == 'POST':
        task = request.get_json(force=True)
        required_fields = ['assigned_from', 'assigned_to', 'subject', 'message']

        for field in required_fields:
            if not task.get(field):
                return "Invalid transaction data", 404
        new_task = Task(task['assigned_from'], task['assigned_to'], task['subject'], task['message'])
        blockchain.assign_task(new_task)

        return "Success", 201
    return "test", 0

@node.route('/read/blockchain', methods=['GET'])
def read_blockchain():
    return jsonify(str(blockchain))

node.run(debug=True, port=7000)