# Operadores Booleanos
# True e False
# or e and

# Operador AND os dois valores precisam ser verdadeiros
#Operador OR um dos dois valores precisam ser verdadeiros
#Operador NOT ele inverte a propriedade do True e do False... se eu coloco not True ele passa a ser falso, se eu coloco not false ele passa a ser True


#Refazendo o exercício anterior com os operadores de booleanos

print ('_______________Início__________________\n')

estouComFome = input('Você está com fome ?\n (Digite Sim ou  Não)') == 'Sim'
tenhoComida = input('Tem comida em casa ?\n (Digite Sim ou Não)') == 'Sim'

if estouComFome and not tenhoComida:
    print('Ir ao mercado\n')
    print('Voltar para casa\n')
    print('Preparar uma refeição\n')
    print('Comer a comida')

if estouComFome and tenhoComida:
    print('Preparar uma refeição\n')
    print('Comer a comida')

print('\n___________Fim__________________')


