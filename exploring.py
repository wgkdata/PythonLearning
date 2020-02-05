namelist = []
leng = len(namelist)

a = ''

def explain():
    for i in namelist:
        explain = print(i)



while leng < 25:
    name = input("Enter your name: ")
    namelist.append(name)
    leng = len(namelist)
    print(f"It's done, {name}. Your list has {leng} names and the names {explain()}")

# TODO: Verificar global var

