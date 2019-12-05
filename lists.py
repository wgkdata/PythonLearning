'''
Listas em Python
    Fatiamento
    append, insert, pop, del, clear, extend, +
    min,max
    range
- Suporta todos os tipos de dados, funções, classes;
- Argumentos são list[start:end:step]
'''

#        0     1     2      3
lista = ['v1', 'v2', 'v3', 'v453']
#      - 4     3     2      1

# print(list[-1])

vaults = ['Dash', 'Speed', 'Kong', 'Lazy', 'Reverse']
tricks = ['Front', 'Back', 'Side']

'''
print(vaults[2])

print(vaults[0:3]) # Último número/índice não é incluído (think start + end+1)
print(vaults[1:])  # Do índice 1 até o fim

print(vaults[-1])  # Último item

print(vaults[::2])
'''
'''
movements = vaults + tricks
# print(movements)

movements.append('Monkey') # Adiciona um item ao fim da lista
# print(movements[-1])

movements.insert(0, 'Climb up') # Adiciona um item no índice especificado - .insert(indice, item)
print(movements)

movements.pop() # Remove o último item da lista
print(movements)

del(movements[0:3]) # Remove o item correspondente ao índice especificado
print(movements)
'''
'''
id = list(range(101))

for i in id:
    rst = i * 2
    print(rst)

#print(max(id))
#print(min(id))
'''

mult = ['Sphere', False, 'Sky', 122.98, 145]

for i in mult:
    print(f'Value {i} has the type {type(i)}')