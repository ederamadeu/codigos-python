# Dado uma sequencia de números, calcule a soma e média dos números.
# Não pode usar a função SUM do python
# Dado uma sequencia de números, calcule o maior valor da sequencia.
#Atenção não pode usar a função max do python

listaDados = [] #Declaração da lista de dados

print("Digite uma lista de números (ou 'sair' para finalizar):") #Interação com o usuário

while True: #estrutura de repetição para o usuário continuar digitando numeros dentro do programa até o mesmo encerrar com a palavra sair
    dado = input('Digite um valor:')

    if dado.lower() == 'sair':
        break #sair do código


    listaDados.append(dado) # código adicona dado a lista

print(f'Sua lista de dados é: {listaDados}')

totalDados = 0
mediaDados = 0
maiorDado = listaDados[0]

for num in listaDados:
    totalDados += float (num)
    mediaDados = totalDados/len(listaDados)


print(f'A sonma total é :{totalDados}')
print(f'A média dos dados digitados é: {mediaDados}')

for n in listaDados:
    if n >= maiorDado:
        maiorDado = n

print(f'O maior valor digitado foi:{maiorDado}')


