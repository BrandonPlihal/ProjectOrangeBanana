import hashlib as hash
import json
from datetime import date
from blockchain.block import *

class Blockchain:
    def __init__(self, max_block_bytes):
        self.max_block_bytes = max_block_bytes
        self.chain = [create_genesis_block()]

    def assign_task(self, task):
        if task.bytes() +


    def hash(self, block):
        blockstring = json.dumps(block, sort_keys=True).encode()
        return hash.sha256(blockstring).hexdigest()

