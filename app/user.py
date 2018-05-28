import requests

if __name__ == '__main__':
    response = requests.post('http://localhost:7000/assign/task', json={'sender': "d4ee26eee15148ee92c6cd394edd974e", 'recipient': "d4ee26eee15148ee92c6cd394edd4326d", 'amount': 100})