import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        # Create the genesis block
        self.new_block(previous_hash="The Times 03/Jan/2009 Chancellor on the brink of second bailout for banks.", proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]) if self.chain else None,
        }

        self.pending_transactions = []
        self.chain.append(block)
        return block

    @property
    def last_block(self):
        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()
        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        return hex_hash

# Create a new blockchain instance
blockchain = Blockchain()

# Add transactions and create blocks
transaction1 = blockchain.new_transaction("Satoshi", "Alex", '10 BTC')
transaction2 = blockchain.new_transaction("Alex", "Satoshi", '2 BTC')
transaction3 = blockchain.new_transaction("Satoshi", "James", '10 BTC')
blockchain.new_block(10123)

transaction4 = blockchain.new_transaction("Alex", "Lucy", '2 BTC')
transaction5 = blockchain.new_transaction("Lucy", "Justin", '1 BTC')
transaction6 = blockchain.new_transaction("Justin", "Alex", '1 BTC')
blockchain.new_block(10384)

# Print the blockchain
print("Genesis block: ", blockchain.chain)
