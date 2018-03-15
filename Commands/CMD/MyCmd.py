class MyCmd:
    def pre_cmd(self, orign_cmd):
        return 'bash -lc \'' + orign_cmd + '\''
