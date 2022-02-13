n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('sua media é {}, voce foi REPROVADO!'.format(format(media)))
elif media > 5.0 and media < 7:
    print('sua media é {}, voce esta de RECUPERAÇÃO!'.format(media))
else:
    print('sua media é {}, voce foi APROVADO!'.format(media))
