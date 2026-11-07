# Dados duas listas, print todcos os valores que aparecem duplicados nas duas listas

listaValoresUm = [2,4,6,8,10]

listaValoresDois = [1,2,3,4,5,6,7,8,9]

for valorUM in listaValoresUm:
    for valorDois in listaValoresDois:
        if valorUM == valorDois:
            print(f'Valor duplicado encontrado na segunda lista de dados é: {valorUM}')



