#Nova Cifra de Cesar

#Função para criptografar uma mensagem usando a cifra de César
def cifra_cesar (letra, seq, chave):
    indice_atual = seq.index(letra)
    novo_indice = (indice_atual + chave) % len(seq)
    return seq[novo_indice]

alfabetoMaiusculo = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alfabetoMinusculo = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

input_mensagem = input("Digite a mensagem que deseja criptografar: ")
input_chave = int(input("Digite a chave de criptografia (um número inteiro): "))

mensagem_criptografada = ""
for letra in input_mensagem:
    if letra in alfabetoMaiusculo:
        mensagem_criptografada += cifra_cesar(letra, alfabetoMaiusculo, input_chave)
    elif letra in alfabetoMinusculo:
        mensagem_criptografada += cifra_cesar(letra, alfabetoMinusculo, input_chave)
    else:
        mensagem_criptografada += letra

print("Mensagem criptografada:", mensagem_criptografada)

