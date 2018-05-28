import unittest
from blockchain.blockchain import  Blockchain
from blockchain.task import Task

class TestBlockchain(unittest.TestCase):
    def test_assign_task(self):
        new_blockchain = Blockchain(100)

        new_task = Task('Brandon', 'Xavier', 'Test message', 'This is a test message')

        new_blockchain.assign_task(new_task)
