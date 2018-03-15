from CMD.Cluster import Cluster
from CMD.Componet import Componet
from CMD.KafkaJstrom import Kafka
from CMD.Matser import Master

vps = '192.168.207.139'
cluster = [vps]
userName = 'root'
password = '000000'

import json

data = ''
with open('../../config/config.json', 'r') as f:
    data = json.load(f)

kafkaconfig = data.get('kafka')
kafkamasters = []
for k, node in kafkaconfig.get('masters').items():
    kafkamasters.append(Master(host=node.get('addr'), username=node.get('username'), passw=node.get('passw')))

kafkaCluster = Kafka(masters=kafkamasters, path=kafkaconfig.get('path'), start=kafkaconfig.get('start'),
                     stop=kafkaconfig.get('stop'), config=kafkaconfig.get('config'))

MyCluster = Cluster(components=[kafkaCluster])
#MyCluster.stop()

master0 = Master(host=cluster[0], username=userName, passw=password)
component0 = Componet(name='test', start='ls', stop='pwd', masters=[master0])
TestCluester = Cluster(components=[component0, kafkaCluster])
TestCluester.restart()
