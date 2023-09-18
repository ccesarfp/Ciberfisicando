from EnderecoInvalido import EnderecoInvalido


class RAM:
    def __init__(self, k):
        self.k = 2 ** k
        self.memoria = [0] * self.k

    def read(self, x):
        if x < 0 or x >= len(self.memoria):
            raise EnderecoInvalido(x)
        return self.memoria[x]

    def write(self, x, dado):
        if x < 0 or x >= len(self.memoria):
            raise EnderecoInvalido(x)
        self.memoria[x] = dado
