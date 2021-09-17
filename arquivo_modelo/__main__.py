'''
gduarte@home-vm
Created on 16-set-2021
'''

import argparse
from arquivo_modelo import Registros


def main(input_file, output_file, fmt=None):
    """
    Traduz o arquivo em input_file e salva em output_file

    Parametros
    ----------
    input_file : str
        Arquivo a ser traduzido
    output_file : str
        Arquivo destino
    fmt : str, optional
        Formato do arquivo destino (por padrão é escolhido
        pela extensão do arquivo destino)
    """        
    try:
        reglist = Registros(input_file)
        reglist.salvar_como(output_file, fmt=fmt)
    except NotImplementedError as e:
        print(str(e))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Traduz um arquivo_modelo para txt, csv ou html')
    parser.add_argument(dest='input_file', metavar='arquivo_entrada',
        type=str, help='arquivo para traducao')
    parser.add_argument(dest='output_file', metavar='arquivo_saida',
        type=str, help='arquivo destino')
    parser.add_argument('--fmt', dest='fmt', metavar='formato_saida',
        type=str, help='formato para o arquivo destino, se nao especificado\
                        usa a extensao do arquivo de saida para determinar')
    args = parser.parse_args()
    main(**vars(args))
