from flask import Flask
from uuid import uuid4
from blockchain import Blockchain

app = Flask(__name__)

node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()

@app.route('/')
def home():
    return 'Blockchain Page!'

@app.route('/mine', methods=['GET'])
def mine():
    return 'We\'ll mine a new Block'

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return 'We\'ll add a new transaction'

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonfy(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)