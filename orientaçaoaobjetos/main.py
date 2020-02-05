'''

Método de instância: Refere-se à instância/objeto da classe, baseando-se nisso pra execução.
Método de classe: Está ligado a classe em si e não à instância.
Método estático: Não depende nem do objeto nem da classe. É como uma função normal, mas dentro de uma classe:
    - Não precisa do self nem do cls;
    - Não é possível usar self e cls dentro do método;
    - Chamável pela classe ou pela instância;
'''

from random import randint

class Pessoa:
    ano_atual = 2020

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)


    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

# p1 = Pessoa.por_ano_nascimento('John', 1987)

p1 = Pessoa('Luiz', 33)

print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

print(Pessoa.gera_id())
print(p1.gera_id())
