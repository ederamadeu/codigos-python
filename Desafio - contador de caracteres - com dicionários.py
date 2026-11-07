# Desafio contador de caracteres solução com dicionários


texto= """
Python é uma linguagem de programação de alto nível e de propósito geral . Sua filosofia de design enfatiza a legibilidade do código com o uso de indentação significativa .
[ 38 ] Python é verificado dinamicamente quanto aos tipos e coletado pelo coletor de lixo .
Ele suporta múltiplos paradigmas de programação , incluindo programação estruturada (particularmente procedural ), orientada a objetos e funcional

"""

vogais = {
    "A":0,
    "E":0,
    "I":0,
    "O":0,
    "U":0,
}


for caractere in texto:
    if caractere.upper() == 'A':
        vogais['A'] +=1

    if caractere.upper() == 'E':
        vogais['E'] +=1

    if caractere.upper() == 'I':
        vogais['I'] +=1

    if caractere.upper() == 'O':
        vogais['O'] +=1

    if caractere.upper() == 'U':
        vogais['U'] +=1

totalCaractere = vogais['A'] + vogais['E'] + vogais['I'] + vogais['O'] + vogais ['U']
print(f"Há {totalCaractere} vogais no texto, sendo:\n")
for vogal, contagem in vogais.items():
    print(f"{contagem} letras {vogal} no texto.")


