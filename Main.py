import sys

from EnderecoInvalido import EnderecoInvalido
from Cache import Cache
from CPU import CPU
from InpOut import InpOut
from RAM import RAM

try:
    io = InpOut()
    ram = RAM(11)  # 2K de RAM (2**11)
    cache = Cache(128, 16, ram)  # total cache = 128, cacheline = 16 palavras
    cpu = CPU(cache, io)

    inicio = 0
    ram.write(inicio, 110)
    ram.write(inicio + 1, 130)
    cpu.run(inicio + 1)
except EnderecoInvalido as e:
    print("Endereco inválido:", e.ender, file=sys.stderr)
