import random

class Robot:
    name = ''

    def __init__(self):
        self.set_name()

    def reset(self):
        self.name = ''

    def set_name(self):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.name = "".join([random.choice(alphabet), random.choice(alphabet), str(random.randrange(100,999))])
