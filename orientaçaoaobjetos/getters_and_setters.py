'''

Funciona como uma proteção/filtro para cada valor/atributo onde é possível validar tipos de dados e informações.

Getter: Obtém um valor (decorador: @property)
Setter: Configura um valor (decorador: @(varconfigurada).setter)

'''

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):  # Checa se a variável 'valor' é do tipo string
            valor = float(valor.replace('R$', ''))  # replace o R$ por nada e transforma a var em float
        self._preco = valor

p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('Caneca', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preco)