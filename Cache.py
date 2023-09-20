
from CacheLine import CacheLine


class Cache:
    def __init__(self, capacidade_total, tamanho_cache_line, ram):
        self.capacidade_total = capacidade_total
        self.tamanho_cache_line = tamanho_cache_line
        self.ram = ram
        self.linhas = [CacheLine(tamanho_cache_line) for _ in range(capacidade_total // tamanho_cache_line)]

    def read(self, x):
        r, t, w, s = self.decode_endereco(x)
        linha = self.linhas[r]

        if linha.tag == t:
            print("Cache hit!")
            return linha.dados[w]
        else:
            print("Cache miss!")
            if linha.modif:
                self.write_back(linha)
            linha.tag = t
            self.ler_da_ram(linha, s)
            return linha.dados[w]

    def write(self, x, dado):
        r, t, w, s = self.decode_endereco(x)
        linha = self.linhas[r]

        if linha.tag == t:
            print("Cache hit!")
            linha.dados[w] = dado
            linha.modif = True
        else:
            print("Cache miss!")
            if linha.modif:
                self.write_back(linha)
            linha.tag = t
            self.ler_da_ram(linha, s)
            linha.dados[w] = dado
            linha.modif = True

    def decode_endereco(self, x):
        w = x % self.tamanho_cache_line
        s = x // self.tamanho_cache_line
        r = s % (self.capacidade_total // self.tamanho_cache_line)
        t = s // (self.capacidade_total // self.tamanho_cache_line)
        return r, t, w, s

    def ler_da_ram(self, linha, s):
        bloco_inicio = s * self.tamanho_cache_line
        for i in range(self.tamanho_cache_line):
            linha.dados[i] = self.ram.read(bloco_inicio + i)
        linha.modif = False

    def write_back(self, linha):
        bloco_inicio = linha.tag * (self.capacidade_total // self.tamanho_cache_line)
        for i in range(self.tamanho_cache_line):
            self.ram.write(bloco_inicio + i, linha.dados[i])
