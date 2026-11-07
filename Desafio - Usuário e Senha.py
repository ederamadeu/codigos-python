# Desafio -- crie um programa que:
# - Pede por um nome de usuário e uma senha
# - Se ambos estiverem corretos, exibe uma mensagem de sucesso
# - Caso contrário, exibe uma mensagem de erro. A mensagem deve ser diferente quando o usuário está incorreto, e quando a senha está incorreta
# - O usuário/ senha "Corretos" podem ser definidos como variáveis dentro do próprio código.

print ('Login Asimov')

_usuario = input('Informe o seu usuário ?\n')

if _usuario == 'eder.amadeu':
    _senha = input('Digite sua senha\n')
    if _senha == 'Pedro@1702':
        print('Logon efetuado com sucesso\n')
    else: print('Senha Incorreta\n')
else: print('Usuário não encontrado\n')






