from blockchain.blockchain import Blockchain
from flask import Flask, jsonify

node = Flask(__name__)

blockchain = Blockchain()

@node.route('/assign/task', methods=['POST', 'GET'])
def assign_task():
    pass

@node.route('/read/blockchain', methods=['GET'])
def read_blockchain():
    return jsonify(str(blockchain))

node.run(debug=True, port=7000)