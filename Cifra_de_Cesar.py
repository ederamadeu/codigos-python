# Crie um cóigo que implementa a "CIFRA DE CÉSAR", isto é,
# que transforma um string movendo cada letra um certo número de passos no alfabeto.
#O numero de passos é dado por uma chave.
#letras com  acentos, espaços e pontuação permanecem iguais

#Exemplos:
#"abc" com chave 1 = "bcd"
#"ABCDE" com chave 2 = "CDEFG"
#"Cachorro" com chave -1 = "Bzbgnqqn"
#"Olá Mundo!" com chave  3 = "Roá Pxqgr!"

#DICA: CONSTRUA 2 strings com as letras do faltabeto em ordem
#Um para letro maiúsculas e outra para as minúsculas, e use esse string para guiar as substituições


alfabetoMaiusculo = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alfabetoMinusculo = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


dadosDigitados = input('\nEntre com a palavra a ser embaralhada:\n')

chaveDados =  int(input('Entre com o número de chave para alterar a palavra\n'))
                  
dadosAlterados=[]

for letra in dadosDigitados:
    if letra.isupper():
        posicao = alfabetoMaiusculo.index(letra)
        novaPosicao = (posicao + chaveDados) %26
        dadosAlterados.append(alfabetoMaiusculo[novaPosicao])
    
    elif letra.islower():
        posicao = alfabetoMinusculo.index(letra)
        novaPosicao =  (posicao + chaveDados) %26
        dadosAlterados.append(alfabetoMinusculo[novaPosicao])

    else:
        dadosAlterados.append(letra)

textoFinal = ''.join(dadosAlterados)
print(f'\nTexto embaralhado:\n\n{textoFinal}')
