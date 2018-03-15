from CMD.MyCmd import MyCmd


class Componet(MyCmd):
    def __init__(self, name, stop, start, masters):
        self.name = name
        self.stop = stop
        self.start = start
        self.masters = masters

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
