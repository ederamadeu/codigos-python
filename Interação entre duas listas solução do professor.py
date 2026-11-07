# #Solução do professor

ValoresUm = [10,11,True, 'xxx']

ValoresDois = [True, 'xxx',100,200,300]

elemento_em_comum = False

for valor1 in ValoresUm:
    if elemento_em_comum:
        break
    for valor2 in ValoresDois:
        if valor1 == valor2:
            elemento_em_comum = True
            break

if elemento_em_comum:
    print(f'As listas {ValoresUm} e {ValoresDois} possuem elemenrtos em comum')

else:
      print(f'As listas {ValoresUm} e {ValoresDois}NÃO possuem elemenrtos em comum')
