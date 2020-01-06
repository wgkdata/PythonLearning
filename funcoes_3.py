def func(*args, **kwargs):
#    print(args, len(args))
#    print(kwargs['surname'])
    nome = kwargs.get('nome')
lista = [1,2,3,4,5,6]

func(*lista, name='Krishna', surname='Raj')