import datetime as date
import hashlib as hasher

class Block:
    def __init__(self, index, timestamp, previous_hash):
        self.index = index + 1
        self.timestamp = timestamp
        self.previous_hash = previous_hash

        self.hash = self.hash_block()
        self.transactions = []
        self.transaction_count = 0

    def hash_block(self):
        sha = hasher.sha256()
        hash_string = str(self.index) + \
                      str(self.timestamp) + \
                      str(self.previous_hash)
        # TODO
        # Also hash based on all data in the block (a.k.a transactions)
        sha.update(hash_string.encode('utf-8'))
        return sha.hexdigest()

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.transaction_count = self.transaction_count + 1
        # TODO
        # change hash whenever transaction is added

    def size(self):
        total_size = 0
        if not len(self.transactions):
            return 0
        for transaction in self.transactions:
            total_size = total_size + transaction.size()
        return total_size

def create_genesis_block():
    return Block(0, date.datetime.now(), "0")

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_hash)