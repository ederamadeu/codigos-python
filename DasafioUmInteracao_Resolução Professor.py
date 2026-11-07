# Dado uma sequencia de números, calcule a soma e média dos números.
# Não pode usar a função SUM do python# Escreva o seu código aqui :-)

#Resolução do  professor

valores = [10,30,-8,0,-2,4]

soma = 0
media = 0
for valor in valores:
    soma += valor
    media = soma/len(valores)

print(f'A soma dos {valores} da lista é : {soma}')
print(f'A média dos {valores} da lista é: {media}')

print('\n\n\n')

#Dado uma sequencia de numeros, calcule o maior valor da sequencia sem usar a formuma MAX do Python

valoresDois= [10,30,10,50,60,90]
maiorDado = 0

for n in valoresDois:
    if n>maiorDado:
        maiorDado = n

print(f'O maior dado da lista {valoresDois} é: {maiorDado}')


print('\n\n\n')

# Dado uma lista de palavras, print todas as palavras que  contenham pelo menos  5 caracteres oi mais

palavras = ['oi', 'João', 'Pedro', 'Maria', 'Jennifer', 'Eder']

for palavra in palavras:
  if len(palavra) >= 5:
      print(f'Encontrada a palavra com 5 ou mais caracteres: {palavra}')


