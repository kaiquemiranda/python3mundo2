casa = float(input('qual o valor do imovel que voce deja comprar? '))
salario = float(input('qual é seu salario? '))
anos = float(input('em quantos anos voce pretende pagar? '))

prestação = (casa / anos) / 12
porcentagem = 0.3 * salario
if prestação < porcentagem:
    print('sua prestação mensal sera R${:.2f}'.format(prestação))
else:
    print('desculpe voce não foi aprovado!')



