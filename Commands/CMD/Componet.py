class Componet:
    def __init__(self, name, path, stop, start):
        self.name = name
        self.path = path
        self.stop = stop
        self.start = start

    def getcmd(self, action):
        mycmd = ''
        if action == 'stop':
            mycmd = self.path + '/' + self.stop
        elif action == 'start':
            mycmd = self.path + '/' + self.start
        return mycmd
