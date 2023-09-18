
class CPU:
    def __init__(self, cache, io):
        self.cache = cache
        self.io = io

    def run(self, x):
        try:
            dado = self.cache.read(x)
            print("Dado lido:", dado)
        except Exception as e:
            print("Endereco inválido:", e)
