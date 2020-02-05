'''
Argumentos do range são range(wheretostart=0, end, step=1)
'''


texto = 'Python'
novo_texto = ''

# continue --> pula p/ proximo laço
# break --> interrompe o laço

for i in texto:
    if i == 'o':
        continue
        novo_texto += i.upper()
    else:
        novo_texto += i

print(novo_texto)
