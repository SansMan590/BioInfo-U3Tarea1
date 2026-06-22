"""
chmod +x degenerate_primer_alignment.py
./degenerate_primer_alignment.py ACATGTATGATCTGGTGATTTGTAAGA TST
"""

import sys
import re

# posibles bases
IUPAC = {
    'A': 'A',
    'T': 'T',
    'G': 'G',
    'C': 'C',
    'R': '[AG]',
    'Y': '[CT]',
    'S': '[GC]',
    'W': '[AT]',
    'K': '[GT]',
    'M': '[AC]',
    'B': '[CGT]',
    'D': '[AGT]',
    'H': '[ACT]',
    'V': '[ACG]',
    'N': '[ACGT]',
}


def partidor_a_regex(partidor):
    patron = ''
    for base in partidor.upper():
        if base not in IUPAC:
            print(f'Error: base "{base}" desconocida')
            sys.exit(1)
        patron += IUPAC[base]
    return patron


def buscar_alineamientos(secuencia, partidor):
    patron = partidor_a_regex(partidor)
    resultados = []

    for i in range(len(secuencia)):
        m = re.match(patron, secuencia[i:])
        if m:
            resultados.append((i, m.group()))

    return resultados

def main():
    if len(sys.argv) != 3:
        print(f'Uso: {sys.argv[0]} <secuencia_ADN> <partidor_degenerado>')
        sys.exit(1)

    secuencia = sys.argv[1].upper()
    partidor  = sys.argv[2].upper()

    resultados = buscar_alineamientos(secuencia, partidor)

    print(f'{"pos":<6} {"seq"}')
    for pos, seq in resultados:
        print(f'{pos:<6} {seq}')


if __name__ == '__main__':
    main()
