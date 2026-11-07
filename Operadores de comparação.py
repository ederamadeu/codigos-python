# Operadores Booleanos
#igual é representado por dois sinais de igual seguidos ==
#o sinal de diferença é uma exclamação seguido de um sinal de igualdade !=
# o sinal de maior é o > como nas demais linguagens
# o sinal de menor é o < como nas demais linguagens


print('-----------início----------\n')

_resposta1 = input('Você está com fome ?\n')
#_resposta2 = input('Você está tem comida em casa ?\n')

if _resposta1 == 'Sim':
    _resposta2 = input('\nVocê tem comida em casa?\n')
    if _resposta2 == 'Sim':
        print ('\nPrepare a refeição\n')
        print('Coma a comida\n')

    elif _resposta2 == 'Não':
        print('\nVá ao mercado\n')
        print('Volte para casa\n')
        print('Prepare a refeição\n')
        print('Coma a comida\n')
        print('________Fim_______')
print('__________Fim_________')
