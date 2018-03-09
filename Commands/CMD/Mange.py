import paramiko
from CMD import Componet

kafka = Componet.Componet(name='Kafka', path='/home', start='ls', stop='echo \'hello\'')




kafkaPath = '/opt/rt/kafka'
kafkaStart = '/bin/kafka-server-start.sh -daemon '
kafkaConfig = '/config/server.properties'
kafkaStop = '/bin/kafka-server-stop.sh'

jstormPath = '/opt/rt/jstorm'
jstormStart = '/bin/start.sh'
jstormStop = '/bin/stop.sh'

zookeeperPath = ''
zookeeperStart = ''

redisPath = ''
redisStart = ''
redisStop = ''

cluster = ['hs01','hs02','hs03']
userName = 'root'
password = 'hello123!'

def stopCluster():
    for node in cluster:
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname=node, username=userName, password=password)

        stdin, stdout, stderr = s.exec_command(kafkaPath+kafkaStop)
        print(stdout.read(),'\n',stderr.read(),'\n')

        stdin, stdout, stderr = s.exec_command(jstormPath+jstormStop)
        print(stdout.read(),'\n',stderr.read(),'\n')

        s.close

def startCluster():
    for node in cluster:
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname=node, username=userName, password=password)

        print(node,' ：',kafkaPath+kafkaStart+kafkaPath+kafkaConfig)
        stdin, stdout, stderr = s.exec_command(kafkaPath+kafkaStart+kafkaPath+kafkaConfig)
        print(stdout.read(),'\n',stderr.read(),'\n')

        stdin, stdout, stderr = s.exec_command(jstormPath+jstormStart)
        print(node,' ：',jstormPath+jstormStart)
        print(str(stdout.read()),'\n')

        s.close

#stopCluster()
startCluster()
