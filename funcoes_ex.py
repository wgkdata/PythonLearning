from random import randint


'''
def saudacao(msg='Olá', name='usuário'):
    print(f'{msg}, {name}!')

saudacao('Hey', 'John')

def soma(n1, n2, n3):
    s = n1 + n2 + n3
    print(s)

soma(10, 20, 30)

def aumento(valor, percentual):
    add = print(((percentual * valor) / 100) + valor)
    return add

aumento(130, 33)
'''
def fb(valor):
    if valor % 2 == 0:
        return 'fizz'
    if valor % 5 == 0 and valor % 3 ==0:
        return 'FizzBuzz'
    if valor % 5 == 0:
        return 'buzz'

    else:
        return valor

print(fb(25))

for i in range(randint(0, 50)):
    aleatorio = randint(0, 200)
    i += 1
    print(fb(aleatorio))
print(f'thats {i}')