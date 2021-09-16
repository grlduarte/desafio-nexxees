'''
gduarte@home-vm
Created on 15-set-2021
'''

from dictionaries import *


#is this class necessary?
class DataContainer:
    """Kind of a dict"""
    def __repr__(self):
        out = ''
        for at in dir(self):
            if at.startswith('__'): continue
            out += f'{at:<20}:{self[at]:>20}\n'
        return out

    def __getitem__(self, k):
        return getattr(self, k)

    def __setitem__(self, k, v):
        return setattr(self, k, v)


class FileData:
    def __init__(self, line):
        for k, v in self.data_dict.items():
            dc = DataContainer()
            try:
                for field, dt in v.items():
                    sl = slice(*dt[0])
                    fmt = dt[1]
                    data = fmt(line[sl])
                    setattr(dc, field, data)
            except AttributeError:
                sl = slice(*v[0])
                fmt = v[1]
                dc = fmt(line[sl])
            setattr(self, k, dc)


#TODO> create individual __repr__ for each card class
class FileHeader(FileData):
    data_dict = fheader_dict

class FileTrailer(FileData):
    data_dict = ftrailer_dict

class LoteHeader(FileData):
    data_dict = lheader_dict

class LoteTrailer(FileData):
    data_dict = ltrailer_dict

class DetailCard(FileData):
    data_dict = detail_dict


class InputFile:
    line_type = {'0': ('header', FileHeader),
                 '1': ('lote', LoteHeader),
                 '3': ('detail', DetailCard),
                 '5': ('lote_t', LoteTrailer),
                 '9': ('trailer', FileTrailer),
                 }

    def __init__(self, fname):
        with open(fname) as f:
            lines = f.readlines()
        for line in lines:
            #TODO> a "lot type" line must create a new instance of Lote
            card, card_obj = self.line_type[line[7]]
            card_data = card_obj(line)
            setattr(self, card, card_data)


class Lote:
    pass
