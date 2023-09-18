
class CacheLine:
    def __init__(self, k):
        self.k = k
        self.tag = None
        self.dados = [0] * k
        self.modif = False
