## Flask
Criado por Armin Ronacher

Microframework baseado nas bibliotecas "Werkzeug + Jinja + simplejson"

Mantido pela "PALLETS"

Flask e seu ecossistema
![flask_eco](/tutorial/47_Flask/flask_eco.jpg)

### Iniciando
arquivo app.py, onde conterá todos os componente central para a aplicacao

```Python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello:
  return "Hello World"

@app.route("/<variavel>")  # passando uma variável a rota
def root(variavel): # chamando a variavel na funcao e concatenando eventualmente a alguma     coisa. Variavel como parametro. Encapsulando da informacao
  return f'eu estou chamando a {variavel}
```

### Blueprint
http://exploreflask.com/en/latest/blueprints.html

define como sera estruturado seu aplicativo. Evitando assim que todo o codigo esteja dentro de um só arquivo, mas sim separando-o em modulos com toda a sua colecao de views, templates, static file e outros elementos.

no mesmo level do arquivo app.py, crie uma pasta para todas os modulos.\
e a cada modulo (arquivo) um arquivo \__init__.py em branco deve ser criado para poder assim ser possivel importa-los\
alem do mais crie os arquivos:\
views.py - como page\
form.py - como fill page\

![blueprint](/tutorial/47_Flask/blueprint.jpg)

### ver sobre import novamente
aqui foi possivel fazer uma chamada direto ao objeto
arquivo \__init__.py foi instanciado a classe
arquivo \app.py importado o objeto.
