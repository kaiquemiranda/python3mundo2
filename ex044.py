print('==' * 5, 'LOJAS GUANABARA', '==' * 5)
compra = float(input('valor da compra: '))
print('''FORMAS DE PAGAMENTO
 [1] a vista
 [2] a vista no cartão
 [3] 2x no cartão
 [4] 3x ou mais no cartão''')
formapg = int(input('forma de pagamento: '))
desc10 = compra - (0.1 * compra)
desc5 = compra - (0.05 * compra)
juros20 = compra + (0.2 * compra)
if formapg == 1:
    print('sua compra a vista tera 10% de desconto e ficara R${:.2f}'.format(desc10))
elif formapg == 2:
    print('sua compra a vista no cartão  ficara R${:.2f}'.format(desc5))
elif formapg == 3:
    parcela = compra / 2
    print('sua compra em 2x no cartão ficara 2x de R${:.2f}'.format(parcela))
elif formapg == 4:
    parcela = compra / 3
    print('sua compra em 3x no cartão tera 20% de juros e ficara 2x de R${:.2f}'.format(parcela))



