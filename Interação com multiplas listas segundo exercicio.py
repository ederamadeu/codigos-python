# Dado duas listas, printe uma mensagem dizendo se existe algum elemento em comum entre elas ou não .

listaDadosUm = [1,2,3,4,5,6,7,8,9,100]

listaDadosDois = [2,4,6,8,10,100,200]

listaDadosComum = []

for valorUm in listaDadosUm:
    for valorDois in listaDadosDois:
        if valorUm == valorDois:
            listaDadosComum.append(valorUm)

print(f'Os dados em comum encontrados foram: {listaDadosComum}')

