namelist = []
leng = len(namelist)


def explain():
    for i in namelist:
        a = print(i)



while leng < 25:
    name = input("Enter your name: ")
    namelist.append(name)
    leng = len(namelist)
    print(f"It's done, {name}. Your list has {leng} names and the names {explain()}")

# TODO: Verificar e corrigir para exibição correta dos nomes

