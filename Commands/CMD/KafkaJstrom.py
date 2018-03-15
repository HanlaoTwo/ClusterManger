from CMD.MyCmd import MyCmd


class Kafka(MyCmd):
    def __init__(self, masters, path='', start='', stop='', config=''):

        self.name = 'kafka'
        self.masters = masters
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
