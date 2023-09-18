
class EnderecoInvalido(Exception):
    def __init__(self, ender):
        self.ender = ender
