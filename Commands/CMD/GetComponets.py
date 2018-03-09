import json

data1 = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}
str = json.dumps(data1)

with open('../config/componets.json', 'r') as f:
    data = json.load(f)
    print(data)
