import json

with open('../../config/config.json', 'r') as f:
    data = json.load(f)
    print(data)
