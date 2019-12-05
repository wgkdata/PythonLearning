'''

Iterando strings com while

'''
string = 'aaaaaaaaaaeiou'
str_size = len(string) - 1

counter = 0
contagem_atual = 0
letra = ''

# print(string.count('i'))

while counter <= str_size:
    qtdx_letra = string.count(string[counter])

    if contagem_atual < qtdx_letra and string[counter].strip():
        letra = string[counter]
        contagem_atual = qtdx_letra

    #print(string[counter], conta)

    counter += 1

print(letra, contagem_atual)

