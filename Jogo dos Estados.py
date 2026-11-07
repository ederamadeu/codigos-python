# Crie um "jogo dos estados". Neste jogo, o jogador precisa responder o nome da capital de cada estado do Brasil. O jogo deve pergutar ao usuário "Qual a capital do estado X ?"
# E checar se o usuário respondeu de forma correta. Após a cada pergunta, o usuário pode escolher, parar o jogo ou continuar para a próxima pergunta.
# Quando o usuário decidir parar, oyu quando todas as perguntas forem respondiddas, o código mostra o número bruto e porcentagem de acertos.


CentroOeste = {
   'Distrito Federal (DF)': 'Brasília',
   'Goiás (GO)': 'Goiânia',
   'Mato Grosso (MT)': 'Cuiabá',
   'Matro Grosso do Sul (MS)': 'Campo Grande',

}

Norte = {
    'Acre (AC)':'Rio Branco',
    'Amapá (AP)': 'Macapá',
    'Amazonas (AM)': 'Manaus',
    'Pará (PA)':'Belém',
    'Rondônia (RO)': 'Porto Velho',
    'Roraima (RR)':'Boa vista',
    'Tocantins (TO)':'Palmas',
}


Nordeste = {

    'Alagoas (AL)':'Maceió',
    'Bahia (BA)':'Salvador',
    'Ceará (CE)':'Fortaleza',
    'Maranhão (MA)':'São Luiz',
    'Paraíba (PB)':'João Pessoa',
    'Pernambuco (PE)':'Recife',
    'Piaiu (PI)':'Teresina',
    'Rio Grande do Norte (RN)':'Natal',
    'Sergipe (SE)':'Aracaju',

}

Sudeste = {
    'Espirito Santo (ES)':'Vitória',
    'Minas Gerais (MG)':'Belo Horizonte',
    'Rio de Janeiro (RJ)':'Rio de Janeiro',
    'São Paulo (SP)':'São Paulo',

}


print ('Vamos iniciar o quiz das capitais dos estados brasileiros!')
print('\n\nA primeira região é a Centro-Oeste..')

totalAcerto = 0
totalErro = 0
continuarQuiz = True

for estadoCentroOeste, capitalCentroOeste in CentroOeste.items():
    print(f'\nInforme a capital do estado {estadoCentroOeste}, ou sair para encerrar o quiz')

    respostaUser = input('->:')

    if respostaUser == 'sair':
        continuarQuiz = False
        print('Quiz encerrado')
        break


    if respostaUser.lower() == capitalCentroOeste.lower():
        print('Resposta correta\n')
        totalAcerto +=1

    else:
        print(f'Resposta errada!\nO correto é {capitalCentroOeste}\n')
        totalErro +=1




if continuarQuiz:

    print('Agora vamos ver as capitals da região Nordeste...\n')

    for estadoNordeste, capitalNordeste in Nordeste.items():
        print(f'\nInforme a capital do estado {estadoNordeste}, ou sair para encerrar o quiz')

        respostaUserNordeste = input('->:')

        if respostaUserNordeste == 'sair':
                continuarQuiz = False
                print('Quiz encerrado')
                break

        if respostaUserNordeste.lower() == capitalNordeste.lower():
            print('Resposta Correta\n')
            totalAcerto +=1
        else:
            print(f'Resposta errada!\nO correto é {capitalNordeste}\n')
            totalErro +=1



if continuarQuiz:

    print('Agora vamos ver as capitals da região Norte...\n')

    for estadoNorte, capitalNorte in Norte.items():
        print(f'\nInforme a capital do estado {estadoNorte}, ou sair para encerrar o quiz')

        respostaUserNorte = input('->:')

        if respostaUserNorte == 'sair':
                continuarQuiz = False
                print('Quiz encerrado')
                break

        if respostaUserNorte.lower() == capitalNorte.lower():
            print('Resposta Correta\n')
            totalAcerto +=1
        else:
            print(f'Resposta errada!\nO correto é {capitalNorte}\n')
            totalErro +=1



if continuarQuiz:

    print('Agora vamos ver as capitals da região Sudeste...\n')

    for estadoSudeste, capitalSudeste in Sudeste.items():
        print(f'\nInforme a capital do estado {estadoSudeste}, ou sair para encerrar o quiz')

        respostaUserSudeste = input('->:')

        if respostaUserSudeste == 'sair':
                continuarQuiz = False
                print('Quiz encerrado')
                break

        if respostaUserSudeste.lower() == capitalSudeste.lower():
            print('Resposta Correta\n')
            totalAcerto +=1
        else:
            print(f'Resposta errada!\nO correto é {capitalSudeste}\n')
            totalErro +=1




mediaAcerto = totalAcerto/27
mediaErro = totalErro/27

print(f'Você acertou um total de {totalAcerto} de 27 capitais.Média de {mediaAcerto}\n\n')
print(f'Você erroum um total de {totalErro} de 27 capitals.Média de {mediaErro}')
