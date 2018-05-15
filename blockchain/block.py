import sys
import datetime as date

class Block:
    def __init__(self, index, timestamp, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash

        self.transactions = [self._create_genesis_block()]

    def __str__(self):
        pass

    def hash_block(self):
        pass

    def bytes(self):
        return sys.getsizeof(self.index) + sys.getsizeof(self.timestamp) + \
               sys.getsizeof(self.previous_hash) + sys.getsizeof(self.transactions)

def _create_genesis_block(self):
    return Block(0,date.datetime.now(),"0")