import telnetlib
from commands import *


class FastIron:

    def __init__(self, host, user="", port=23, password=""):
        self.hostname = host
        self.username = user
        self.port = port
        self.password = password
        self.session = None

    def open(self):
        self.session = telnetlib.Telnet(self.hostname, self.port)

    def close(self):
        self.session.close()

    def interact(self):
        self.session.interact()
        
    def send_command(self, my_list):
        for val in my_list:
            self.session.write(val)

    def show_version(self):
        self.session.write(b"show version \n")
        return self.session.read_until(b'HW: ', 1).decode('utf-8')

