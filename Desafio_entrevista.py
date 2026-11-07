# Desafio de entrevista)
# Crie um programa que :
#Pede pelo seu nome  e idade
# Dá oi para você
# Conta quantas letras o seu nome possui
#Fala quantos anos você terá daqui 5 anos

print ("Por favor digite seu nome")
_nome = input()
print ("Olá "+_nome+", agora digite sua idade")
_idade = int(input())
_contaCaracteres= str(len(_nome))
print("Seu nome possui " +_contaCaracteres+" caracteres")
_contaIdade = str(_idade +5)
print("Você terá " +_contaIdade+"anos de idade daqui a 5 anos")

