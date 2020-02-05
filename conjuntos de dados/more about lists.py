'''
    * Split - Divide uma string # str
    * Join - Junta uma lista # str
    * Enumerate - Enumerar elem da lista # list/iterable
    * Strip - Remove espaços do início e fim # str
'''

string = "STORROR was here and did jumps, Rio has a huge culture."

list1 = string.split(' ')
print(list1)
'''
list2 = string.split(',')

#print(list)

palavra = ''
contagem = 0

for word in list1:
    word_qtd = list1.count(word)

    if word_qtd > contagem:     # Checa a palavra que apareceu mais vezes;
        contagem = word_qtd
        palavra = word

print(f'\'{palavra}\' was here a total of {contagem} times!')
'''
'''
string_join = '_'.join(list1)

#print(f'{string} \n{list1} \n{string_join}')

for indice, valor in enumerate(list1):
    print(indice, valor)
'''