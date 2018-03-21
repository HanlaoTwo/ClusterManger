import json

def getComp():
    with open('../../config/config.json', 'r') as f:
        data = json.load(f)
        print('----------------------',str(data))
        return json.dumps(data)
