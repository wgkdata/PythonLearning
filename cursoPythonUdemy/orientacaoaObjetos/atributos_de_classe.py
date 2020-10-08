class A:
    var_da_classe = 12341234123412341234

a1 = A()
a2 = A()

A.var_da_classe = 123

print(a1.var_da_classe)
print(a2.var_da_classe)
print(A.var_da_classe)






