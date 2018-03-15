import paramiko


class Master:
    def __init__(self, host, username, passw):
        self.host = host
        self.username = username
        self.passw = passw
        self.client = None

    def getSSHClient(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.host, username=self.username, password=self.passw)
        return self.client

    def __del__(self):
        if self.client:
            self.client.close()
