from datetime import date
atual = date.today().year
nascimento = int(input('ano de nascimento: '))
idade = atual - nascimento
print('quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('voce tem que se alistar IMEDIATAMETE')
elif idade < 18:
    saldo = 18 - idade
    print('ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('voce ja deveria ter se alistado a {} anos'.format(saldo))
    ano = atual - saldo
    print('seu alistamento foi em {}'.format(ano))

