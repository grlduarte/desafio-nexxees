'''
Formatadores para os diversos tipos de dados no arquivo modelo.

gduarte@home-vm
Created on 15-set-2021
'''

def alfa(arg):
    return str(arg).strip()


def data(arg):
    dd = arg[:2]
    mm = arg[2:4]
    yyyy = arg[4:]
    return f'{dd}/{mm}/{yyyy}'


def hora(arg):
    hh = arg[:2]
    mm = arg[2:4]
    ss = arg[4:]
    return f'{hh}h{mm}m{ss}s'


def moeda(arg):
    valor_p = int(arg[:-2])
    out = f'{valor_p:,}'.replace(',', '.')
    valor_d = arg[-2:]
    out += f',{valor_d}'
    return out


def qtde_moeda(arg):
    valor_p = int(arg[:-5])
    out = f'{valor_p:,}'.replace(',', '.')
    valor_d = arg[-5:]
    out += f',{valor_d}'
    return out


def cnpj(arg):
    num = int(arg[:8])
    out = f'{num:,}'.replace(',', '.')
    dv1 = arg[8:12]
    dv2 = arg[12:]
    out += f'/{dv1}-{dv2}'
    return out


def cep(arg):
    return f'{arg[:5]}-{arg[5:]}'
    
