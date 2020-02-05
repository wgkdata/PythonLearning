"""
Operador ternário em Python

Facilita e diminui as linhas de código de condições.
"""

'''
logged_user = False
msg = 'Usuário online.' if logged_user else 'Usuário offline.'

print(msg)
'''

idade = input('Digite sua idade: ')

if not idade.isnumeric():
    print('[!] Digite apenas números [!]')
else:
    idade = int(idade)
    check = 'Acesso autorizado.' if idade >= 18 else 'Acesso não autorizado: Você precisa ter mais de 18 anos.'

    print(check)