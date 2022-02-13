r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmanto: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima PODEM FORMAR UM TRIANGULO ', end='')
    if r1 == r2 and r2 == r3:
        print('EQUILATERO')
    if r1 != r2 and r2 != r3 and r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('os segmentos a cima NÃO PODEM FORMAR UM TRIANGULO!')
