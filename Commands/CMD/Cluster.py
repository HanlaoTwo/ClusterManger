class Cluster():
    def __init__(self, components):
        self.components = components

    def stop(self):
        for component in self.components:
            for master in component.masters:
                print('\n***************\n停止')
                stdin, stdout, stderr = master.getSSHClient().exec_command(component.getcmd(action='stop'))
                print('-------------\n执行结果：', stdout.read().decode('utf-8'), '-------------\n', '报错信息：',
                      stderr.read().decode('utf-8'))

    def start(self):
        for component in self.components:
            for master in component.masters:
                print('\n***************\n启动')
                stdin, stdout, stderr = master.getSSHClient().exec_command(component.getcmd(action='start'))
                print('-------------\n执行结果：', stdout.read().decode('utf-8'), '-------------\n', '报错信息：',
                      stderr.read().decode('utf-8'))

    def restart(self):
        self.stop()
        self.start()
