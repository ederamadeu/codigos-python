# Dado uma lista de palabras, print todas as palavras com pelo menos 5 caracteres

listaNomes = []

print("Digite uma lista de nomes (ou 'sair' para finalizar):") #Interação com o usuário

while True: #estrutura de repetição para o usuário continuar digitando numeros dentro do programa até o mesmo encerrar com a palavra sair
    dado = input('Digite um nome:')

    if dado.lower() == 'sair':
        break #sair do código


    listaNomes.append(dado) # código adicona dado a lista

print(f'Sua lista de dados é: {listaNomes}')

for nome in listaNomes:
    if len(nome)>= 5:
        print(f'Os nomes com mais de 5 lestras são: {nome}')

