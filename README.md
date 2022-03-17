# Valid identifier

Utilizando a especificação do programa Identifier.java crie casos de teste baseado-se nos 
seguintes critérios da técnica funcional (use os [slides de apoio](https://moodle.utfpr.edu.br/mod/resource/view.php?id=1090131) do moodle): 

- Análise de valor limite; e

- Particionamento em classes de equivalência.

Implemente seus casos de teste usando o programa cedido. Se preferir, pode 
fazer algo similar em outra liguagem e com outro programa similar. Use o 
JUnit para testar seu programa (ou ferramentas similares para outras linguagens). 
Entregue um .ZIP (ou outro arquivo compactado) contendo o projeto e um PDF 
e relatórios de cobertura. Inclua um arquivo com os nomes de todos os alunos. 


# Requisitos

- Python 3
- poetry

## Instalar dependências

```
poetry install
```


# Rodar testes

```
poetry run pytest
```

### Tests with Coverage
```
poetry run pytest --cov
```
