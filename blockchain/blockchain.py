import hashlib as hash
import json
from datetime import date
from blockchain.block import *

class Blockchain:
    def __init__(self, max_block_bytes):
        self.max_block_bytes = max_block_bytes
        self.chain = [create_genesis_block()]

    def assign_task(self, task):
        if task.bytes() + self.chain[-1].bytes() < self.max_block_bytes:
            self.chain[-1].assign_task(task)
        else:
            self.chain[-1].hash = self.hash(self.chain[-1])
            self.chain.append(self.chain[-1].next_block())


    def hash(self, block):
        blockstring = json.dumps(block, sort_keys=True).encode()
        return hash.sha256(blockstring).hexdigest()

