import sys
import datetime as date
import json


class Block:
    def __init__(self, index, timestamp, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = None

        self.transactions = []

    def __str__(self):
        pass

    def bytes(self):
        return sys.getsizeof(self.index) + sys.getsizeof(self.timestamp) + \
               sys.getsizeof(self.previous_hash) + sys.getsizeof(self.transactions)

    def assign_task(self, task):
        self.transactions.append(task)

    def next_block(self):
        return Block(self.index + 1, self.hash_block())

def create_genesis_block():
    return Block(0,date.datetime.now(),"0")