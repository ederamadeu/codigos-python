# Desafio - Contador de Carecteres
# Crie um código que conta o número de vogais de um bloco de texto qualquer
#O Código deve desconsiderar letras maiúsculas e minúsculas, isto é, "a" e "A" contam da mesma forma.
# O texto pode ser colado diretamente como uma string no código.

texto= """
Python é uma linguagem de programação de alto nível e de propósito geral . Sua filosofia de design enfatiza a legibilidade do código com o uso de indentação significativa .
[ 38 ] Python é verificado dinamicamente quanto aos tipos e coletado pelo coletor de lixo .
Ele suporta múltiplos paradigmas de programação , incluindo programação estruturada (particularmente procedural ), orientada a objetos e funcional

"""

texto = texto.lower()

totalA = texto.count("a")
totalE = texto.count("e")
totalI = texto.count("i")
totalO = texto.count("o")
totalU = texto.count("u")

totalVogais = totalA+totalE+totalI+totalO+totalU

print(f"O total de vogais da string analisada  é {totalVogais},sendo:\n{totalA} de letras A\n{totalE} de letras E\n{totalI} de letras I\n{totalO} de letras  e \n{totalU} de letras U")

