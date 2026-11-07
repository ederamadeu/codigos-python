# Listas em Python/ vetores
# tuplas são listas/ valores são imutáveis
# Para criar listas eu coloco os dados entre colchetes ao declarar uma varial , exemplo alunos = [ Alina, Marcos, Paula]
# Para criar uma tupla, eu coloco os dados entre parenteses alunos = (Aline, Marcos, Paula)



# Desafio anterior com FOR

numeroSecreto = 7
descobriu = False

for n in range(3):

    if not descobriu:
        chute = int(input('Descubra o número!'))
        if chute < numeroSecreto:
            print('Chute baixo!')
        elif chute > numeroSecreto:
            print('Chute Alto!')
        else:
            print('Descobriu!')
            descobriu = True



if descobriu:
    print('Parabens, você ganhou!')
else:
    print(f'Que pena, você perdeu!\nO número secreto era {numeroSecreto}')

