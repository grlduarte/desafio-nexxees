'''
gduarte@home-vm
Created on 16-set-2021
'''

from .dictionaries import *


__all__ = ('HeaderArquivo', 'TrailerArquivo', 'HeaderLote',
           'TrailerLote', 'Detalhe')


class DataContainer:
    """Classe passiva para armazenar dados aninhados"""
    def __getitem__(self, k):
        return getattr(self, k)

    def __setitem__(self, k, v):
        return setattr(self, k, v)


class Registro:
    """Le uma linha de registro"""
    def __init__(self, line, cards):
        for k, v in cards.items():
            dc = DataContainer()
            try:
                for field, dt in v.items():
                    sl = slice(*dt[0])
                    fmt = dt[1]
                    data = fmt(line[sl])
                    dc[field] = data
            except AttributeError:
                # se v nao tiver o atributo items()
                # entao o campo nao tem infos aninhadas
                sl = slice(*v[0])
                fmt = v[1]
                dc = fmt(line[sl])
            setattr(self, k, dc)


class HeaderArquivo(Registro):
    def __init__(self, line):
        cards = fheader_cards
        super().__init__(line, cards)

class TrailerArquivo(Registro):
    def __init__(self, line):
        cards = ftrailer_cards
        super().__init__(line, cards)

class HeaderLote(Registro):
    def __init__(self, line):
        cards = lheader_cards
        super().__init__(line, cards)

class TrailerLote(Registro):
    def __init__(self, line):
        cards = ltrailer_cards
        super().__init__(line, cards)

class Detalhe(Registro):
    def __init__(self, line):            
        cards = detail_cards
        super().__init__(line, cards)
