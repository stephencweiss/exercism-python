import string
from random import seed, choice, randrange


class Robot:
    name = ''
    usedNames = set()

    def __init__(self):
        self.name = self._generate_name()

    def reset(self):
        seed(self.name)
        self.name = self._generate_name()

    def _generate_name(self):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return "".join([choice(string.ascii_uppercase), choice(string.ascii_uppercase), str(randrange(100, 999))])
