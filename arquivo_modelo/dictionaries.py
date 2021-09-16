'''
Esses dicionarios indicam o que cada segmento de uma linha significa
e qual o formatador a ser usado com esse valor

gduarte@home-vm
Created on 16-set-2021
'''

from .formatters import *


fheader_cards = {'controle': {
                              'banco': ((0, 3), int),
                              'lote': ((3, 7), int),
                              'registro': ((7, 8), int)
                              },
                 'empresa': {
                             'tipo_inscricao': ((17, 18), int),
                             'numero_inscricao': ((18, 32), cnpj),
                             'convenio': ((32, 52), alfa),
                             'cc_agencia': ((52, 57), alfa),
                             'cc_agencia_dv': ((57, 58), alfa),
                             'cc_conta': ((58, 70), alfa),
                             'cc_conta_dv': ((70, 71), alfa),
                             'cc_dv': ((71, 72), alfa),
                             'nome': ((72, 102), alfa)
                             },
                 'nome_do_banco': ((102, 132), alfa),
                 'van': ((132, 142), alfa),
                 'arquivo': {
                             'codigo': ((142, 143), int),
                             'data': ((143, 151), data),
                             'hora': ((151, 157), hora),
                             'sequencia': ((157, 164), int),
                             'layout': ((164, 167), alfa),
                             'densidade': ((167, 172), int),
                             },
                 'reservado_banco': ((172, 191), alfa),
                 'reservado_empresa': ((191, 211), alfa),
                 'cnab': ((211, 240), alfa)
                 }

lheader_cards = {
                 'controle': fheader_cards['controle'],
                 'servico': {
                             'operacao': ((8, 9), alfa),
                             'servico': ((9, 11), int),
                             'forma_lancamento': ((11, 13), int),
                             'layout': ((13, 16), int),
                             },
                 'empresa': fheader_cards['empresa'],
                 'informacao_1': ((102, 142), alfa),
                 'endereco_empresa': {
                                      'logradouro': ((142, 172), alfa),
                                      'numero': ((172, 177), int),
                                      'complemento': ((177, 192), alfa),
                                      'cidade': ((192, 212), alfa),
                                      'cep': ((212, 220), cep),
                                      'estado': ((220, 222), alfa),
                                      },
                 'ocorrencias': ((230, 240), alfa),
                 }

detail_cards = {'controle': fheader_cards['controle'],
                'servico': {
                            'numero_registro': ((8, 13), int),
                            'segmento': ((13, 14), alfa),
                            'tipo_movimento': ((14, 15), int),
                            'codigo_movimento': ((15, 17), int),
                            },
                'favorecido': {
                               'camara': ((17, 20), int),
                               'banco': ((20, 23), int),
                               'cc_agencia': ((23, 28), int),
                               'cc_agencia_dv': ((28, 29), alfa),
                               'cc_conta': ((29, 41), int),
                               'cc_conta_dv': ((41, 42), alfa),
                               'cc_dv': ((42, 43), alfa),
                               'nome': ((43, 73), alfa),
                               },
                'credito': {
                            'seu_numero': ((73, 93), alfa),
                            'data_pgto': ((93, 101), data),
                            'tipo_moeda': ((101, 104), alfa),
                            'qtde_moeda': ((104, 119), qtde_moeda),
                            'valor_pgto': ((119, 134), moeda),
                            'nosso_numero': ((134, 154), alfa),
                            'data_real': ((154, 162), data),
                            'valor_real': ((162, 177), moeda),
                            },
                'informacao_2': ((177, 217), alfa),
                'codigo_doc': ((217, 219), alfa),
                'codigo_ted': ((219,224), alfa),
                'codigo_lancamento': ((224, 229), alfa),
                'aviso': ((229, 230), int),
                'ocorrencias': ((230, 240), alfa),                              
                }

ltrailer_cards = {
                  'controle': fheader_cards['controle'],
                  'totais': {
                             'qtde_registros': ((17, 23), int),
                             'valor': ((23, 41), moeda),
                             'qtde_moeda': ((41, 59), qtde_moeda),
                             },
                  'aviso_debito': ((59, 65), int),
                  'nexxera': ((65, 230), alfa),
                  'ocorrencias': ((230, 240), alfa),
                  }

ftrailer_cards = {
                  'controle': fheader_cards['controle'],
                  'totais': {
                             'qtde_lotes': ((17, 23), int),
                             'qtde_registros': ((23, 29), int),
                             'qtde_contas_concil': ((29, 35), int),
                             },
                  }
