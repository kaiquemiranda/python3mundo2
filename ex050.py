soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('a soma dos {} numeros pares que voce informou foi {}'.format(cont, soma))
