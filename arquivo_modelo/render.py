'''
Este modulo contem as funcoes necessarias para renderizacao dos dados
em cada um dos templates suportados. 

gduarte@home-vm
Created on 16-set-2021
'''

from . import __path__ as path


def render_as(reglist, fmt):
    g29_dict = {1: 'Credito em Conta Corrente',
                2: 'Cheque Pagamento/Administrativo',
                3: 'DOC/TED (1) (2)',} # ...
    
    moeda_dict = {'BRL': 'R$'}

    templates = {'txt': template_txt,
                 'html': template_html,
                 'csv': template_csv,}
    tab1, tab2, linha_t, end_of_table, end_of_doc = templates[fmt]()

    out = ''
    for lote in reglist:
        dados1_val = {'nome_empresa': lote.header.empresa.nome,
                      'cnpj_empresa': lote.header.empresa.numero_inscricao,
                      'nome_banco': reglist.header.nome_do_banco,
                      'rua': lote.header.endereco_empresa.logradouro,
                      'numero': lote.header.endereco_empresa.numero,
                      'cidade': lote.header.endereco_empresa.cidade,
                      'cep': lote.header.endereco_empresa.cep,
                      'estado': lote.header.endereco_empresa.estado,}
        out += tab1.format(**dados1_val) + tab2
        for reg in lote:
            dados2_val = {'nome_favorecido': reg.favorecido.nome,
                          'data_pgto': reg.credito.data_pgto,
                          'valor': (moeda_dict[reg.credito.tipo_moeda]
                                    + ' ' + reg.credito.valor_pgto),
                          'numero_documento': reg.credito.seu_numero,
                          'forma_lcto': g29_dict[lote.header.servico.forma_lancamento],}
            out += linha_t.format(**dados2_val)
        out += end_of_table
    out += end_of_doc
    return out


def template_txt():
    with open(path[0]+'/templates/template.txt') as f:
        template = f.readlines()
    tab1 = ''.join(template[:4])
    tab2 = ''.join(template[4:8])
    linha_t = template[8]
    end_of_table = template[9] + '\n'
    end_of_doc = ''
    return [tab1, tab2, linha_t, end_of_table, end_of_doc]


def template_html():
    with open(path[0]+'/templates/template.html') as f:
        template = f.readlines()
    tab1 = ''.join(template[:25])
    tab2 = ''.join(template[25:33])
    linha_t = ''.join(template[33:40])
    end_of_table = template[40] + '<br><br>'
    end_of_doc = ''.join(template[41:42])
    return [tab1, tab2, linha_t, end_of_table, end_of_doc]


def template_csv():
    with open(path[0]+'/templates/template.csv') as f:
        template = f.readlines()
    tab1 = ''.join(template[:2])
    tab2 = template[2]
    linha_t = template[3]
    end_of_table = '\n'
    end_of_doc = ''
    return [tab1, tab2, linha_t, end_of_table, end_of_doc]
