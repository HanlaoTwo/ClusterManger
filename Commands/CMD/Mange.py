import paramiko
from CMD import Componet

zookeeperPath = ''
zookeeperStart = ''

redisPath = ''
redisStart = ''
redisStop = ''

vps = '192.168.207.139'

cluster = [vps]
userName = 'root'
password = '000000'


class MyCmd:
    def pre_cmd(self, orign_cmd):
        return 'bash -lc \'' + orign_cmd + '\''


class Kafka(MyCmd):
    def __init__(self, path='', start='', stop='', config=''):

        self.name = 'kafka'
        if len(path) == 0:
            self.path = '/opt/kafka/kafka_2.10-0.8.1.1'
        else:
            self.path = path
        if len(stop) == 0:
            self.stop = '/bin/kafka-server-stop.sh'
        else:
            self.stop = stop
        if len(start) == 0:
            self.start = '/bin/kafka-server-start.sh -daemon '
        else:
            self.start = start
        if len(config) == 0:
            self.config = '/config/server.properties'
        else:
            self.config = config

    def getcmd(self, action):
        mycmd = ''
        if action == 'stop':
            mycmd = self.path + self.stop
        elif action == 'start':
            mycmd = self.path + self.start + self.path + self.config
        else:
            mycmd = 'echo $PATH'

        mycmd = self.pre_cmd(mycmd)
        print('执行命令：', mycmd)
        return mycmd


class Jstorm(MyCmd):
    def __init__(self, path='', start='', stop=''):

        self.name = 'Jstrom'
        if len(path) == 0:
            self.path = '/opt/rt/jstorm'
        else:
            self.path = path
        if len(stop) == 0:
            self.stop = '/bin/stop.sh'
        else:
            self.stop = stop
        if len(start) == 0:
            self.start = '/bin/start.sh'
        else:
            self.start = start

    def getcmd(self, action):
        mycmd = ''
        if action == 'stop':
            mycmd = self.path + self.stop
        elif action == 'start':
            mycmd = self.path + self.start
        else:
            mycmd = 'echo $PATH'

        mycmd = self.pre_cmd(mycmd)
        print('执行命令：', mycmd)
        return mycmd


class Cluster():
    def __init__(self, components, masters):
        self.components = components
        self.masters = masters

    def stop(self):
        for component in self.components:
            print('\n***************\n停止')
            stdin, stdout, stderr = component.master.getSSHClient().exec_command(component.getcmd(action='stop'))
            print('-------------\n执行结果：', stdout.read().decode('utf-8'), '-------------\n', '报错信息：',
                  stderr.read().decode('utf-8'))


    def start(self):
        for component in self.components:
            print('\n***************\n启动')
            stdin, stdout, stderr = component.master.getSSHClient().exec_command(component.getcmd(action='start'))
            print('-------------\n执行结果：', stdout.read().decode('utf-8'), '-------------\n', '报错信息：',
                  stderr.read().decode('utf-8'))

    def restart(self):
        self.stop()
        self.start()


class Master:
    def __init__(self, host, username, passw):
        self.host = host
        self.username = username
        self.passw = passw

    def getSSHClient(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.host, username=self.username, password=self.passw)
        return self.client

    def __del__(self):
        self.client.close()


class Componet(MyCmd):
    def __init__(self, name, stop, start, master):
        self.name = name
        self.stop = stop
        self.start = start
        self.master = master

    def getcmd(self, action):
        if action == 'stop':
            mycmd = self.stop
        elif action == 'start':
            mycmd = self.start
        else:
            mycmd = 'echo $PATH'
        mycmd = self.pre_cmd(mycmd)
        print('执行命令：', mycmd)
        return mycmd


master0 = Master(host=cluster[0], username=userName, passw=password)
components0 = Componet(name='test', start='echo \'start\'', stop='echo \'stop\'',master=master0)

MyCluster = Cluster(components=[components0], masters=[master0])
# MyCluster.stop(client=myMuster.getSSHClient())
MyCluster.restart()
