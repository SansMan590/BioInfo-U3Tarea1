#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Programa 1: Alineamiento de partidores degenerados
Uso: ./degenerate_primer_alignment.py <secuencia_ADN> <partidor_degenerado>
"""

import sys
import re

# Tabla de códigos IUPAC -> bases posibles
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
    """Convierte un partidor degenerado en una expresión regular."""
    patron = ''
    for base in partidor.upper():
        if base not in IUPAC:
            print(f'Error: base desconocida "{base}" en el partidor.')
            sys.exit(1)
        patron += IUPAC[base]
    return patron


def buscar_alineamientos(secuencia, partidor):
    """Retorna lista de (posición, secuencia_alineada) para todas las coincidencias."""
    patron = partidor_a_regex(partidor)
    resultados = []

    # Búsqueda con overlap: avanzamos de a 1 para no perder coincidencias traslapadas
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
