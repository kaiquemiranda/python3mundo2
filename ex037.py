num = int(input('digite um numero inteiro: '))
print('''escolha uma das bases para converção:
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL  ''')
opcao = int(input('sua opção: '))
if opcao == 1:
    print('{} convertido para BINARIO é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida, tente novamente')

