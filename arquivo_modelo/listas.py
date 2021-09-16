'''
gduarte@home-vm
Created on 16-set-2021
'''

from .render import render_as
from .registro import *


class Registros(list):
    """
    Cria uma lista de registros a partir de um arquivo_modelo.

    Parametros
    ----------
    fname : str
        arquivo a ser aberto
    """
    def __init__(self, fname):
        self.fname = fname
        with open(fname) as f:
            lines = f.readlines()
        self.header = HeaderArquivo(lines[0])
        self.trailer = TrailerArquivo(lines[-1])

        lotes = []
        for i, line in enumerate(lines[1:-1]):
            tipo_registro = line[7]
            if (tipo_registro == '1'):
                # inicia um novo lote ao encontrar um header
                lote = [] 
                header = HeaderLote(line)
                lote.append(header)
            elif (tipo_registro == '3'):
                detail = Detalhe(line)
                lote.append(detail)
            elif (tipo_registro == '5'):
                trailer = TrailerLote(line)
                lote.append(trailer)
                lotes.append(Lote(lote))
            super().__init__(lotes)

    def salvar_como(self, fname, fmt=None):
        """
        Salva o arquivo com o formato da extensao em fname. O formato
        tambem pode ser indicado com o argumento fmt.

        Parametros
        ----------
        fname : str
            arquivo a ser salvo
        fmt : str, optional
            formato do arquivo desejado (txt, html ou csv)
        """
        if not fmt:
            fmt = fname.split('.')[-1]
        out = render_as(self, fmt)
        with open(fname, 'w') as f:
            f.write(out)


class Lote(list):
    """
    Cria uma lista com os registros de segmento dentro
    de um lote
    """
    def __init__(self, registros=[]):
        for i, reg in enumerate(registros):
            if isinstance(reg, HeaderLote):
                self.header = registros.pop(i)
            elif isinstance(reg, TrailerLote):
                self.trailer = registros.pop(i)
        super().__init__(registros)
