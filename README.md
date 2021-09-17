## Desafio Nexxees

Objetivo: criar um programa que leia o modelo de arquivo e traduza para um dos relatórios dados como
exemplo. 

Uso no terminal com:

```console
python -m arquivo_modelo exemplo/modelo_arquivo.txt modelo_arquivo_traduzido.{txt, html, csv}
```
ou na IDE do Python:
```python
from arquivo_modelo import traduzir
traduzir('exemplo/modelo_arquivo.txt', 'modelo_arquivo_traduzido.html')
```

No desafio considerei que o arquivo de entrada sempre está no formato correto, por isso não implementei funções
que checassem isso.
