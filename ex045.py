from random import randint
from time import sleep
import emoji
itens = ('pedra', 'papel', 'tesoura')
pc = randint(0, 2)
print('''suas opções
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('qual é sua jogada? '))
print("JO", emoji.emojize(':fist:', use_aliases=True))
sleep(1)
print("KEN", emoji.emojize(':v:', use_aliases=True))
sleep(1)
print('PO', emoji.emojize(':raised_hand:', use_aliases=True))
sleep(1)
print('-=' * 11)
print('computador jogou {}'.format(itens[pc]))
print('jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if pc == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('jogada invalida')
elif pc == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR TESOURA')
    else:
        print('jogada invalida')
elif pc == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('jogada invalida')




