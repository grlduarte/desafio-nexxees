'''
Este pacote faz a leitura do arquivo_modelo e consegue salva-lo
em formatos txt, html ou csv.

gduarte@home-vm
Created on 16-set-2021
'''

from .registro import *
from .listas import Registros, Lote
from .__main__ import main


__all__ = ['registro', 'listaregistros']
traduzir = main
