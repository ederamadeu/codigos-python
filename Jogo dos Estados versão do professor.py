#Jogo Quiz... Versão do professor.

DicionarioEstados = {
    'Alagoas (AL)':'Maceió',
    'Bahia (BA)':'Salvador',
    'Ceará (CE)':'Fortaleza',
    'Maranhão (MA)':'São Luiz',
    'Paraíba (PB)':'João Pessoa',
    'Pernambuco (PE)':'Recife',
    'Piaiu (PI)':'Teresina',
    'Rio Grande do Norte (RN)':'Natal',
    'Sergipe (SE)':'Aracaju',
    'Espirito Santo (ES)':'Vitória',
    'Minas Gerais (MG)':'Belo Horizonte',
    'Rio de Janeiro (RJ)':'Rio de Janeiro',
    'São Paulo (SP)':'São Paulo',
    'Distrito Federal (DF)': 'Brasília',
    'Goiás (GO)': 'Goiânia',
    'Mato Grosso (MT)': 'Cuiabá',
    'Matro Grosso do Sul (MS)': 'Campo Grande',
    'Acre (AC)':'Rio Branco',
    'Amapá (AP)': 'Macapá',
    'Amazonas (AM)': 'Manaus',
    'Pará (PA)':'Belém',
    'Rondônia (RO)': 'Porto Velho',
    'Roraima (RR)':'Boa vista',
    'Tocantins (TO)':'Palmas',
}

querContinuar = True

rodadas = 0
acertos = 0

for estado, capital in DicionarioEstados.items():

    if not querContinuar:
        break
    rodadas +=1

    print(f'\n - > Qual a capital do Estado {estado}?')
    resposta = input('Sua Resposta: ')

    if resposta.lower() == capital.lower():
        print('Resposta Correta!')
        acertos +=1

    else:
        print(f'\nResposta Errada! O Correto é {capital}')

    while True:
        opcao = input('Deseja continuar ? (s/n)').lower()

        if opcao not in ['s','n']:
            print('Responda apenas com  "s" para sim ou "n" para não.')
            continue

        elif opcao == 'n':
            querContinuar = False
        break




porcentagem = acertos / rodadas *100
print(f'Voce acertou {acertos} de {rodadas}')
print(f'Porcentagem de acertos: {porcentagem:.2f}%')
