# Desafio - crie um programa que:
# Escolha um número secreto.
# Pede por um chute do usuário
# Indica se o usuário errou ou acertou
#Se não acertou , dá uma dica dizendo se o número é mais alto ou mais baixo
# Repete isso 3 vezes

numeroSecreto = 7
descobriu = False

if not descobriu:
    chute = int(input('Descubra o número\nSeu chute: '))
    if chute < numeroSecreto:
        print('Chute baixo\nVocê tem mais duas chances')
    elif chute > numeroSecreto:
        print('Chutou um numero maior!\nVocê tem mais duas chances')
    else:
        print('Descobriu!')
        descobriu = True

if not descobriu:
    chute = int(input('Descubra o número\nSeu chute: '))
    if chute < numeroSecreto:
        print('Chute baixo!\nVocê tem mais uma chance')
    elif chute > numeroSecreto:
        print('Chutou um numero maior!\nVocê tem mais uma chance')
    else:
        print('Descobriu!')
        descobriu = True

if not descobriu:
    chute = int(input('Descubra o número\nSeu chute: '))
    if chute < numeroSecreto:
        print('Chute baixo!')
    elif chute > numeroSecreto:
        print('Chutou um numero maior')
    else:
        print('Descobriu!')
        descobriu = True

if descobriu:
    print('Parabéns você ganhou o jogo!')
else:
    print(f'Que pena, você perdeu!\nO número secreto era {numeroSecreto}')

