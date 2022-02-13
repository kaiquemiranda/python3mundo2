nome = str(input('qual é seu nome? '))
if nome == 'gustavo':
    print('que nome bonito!')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('seu nome é bem popular no brasil')
else:
    print('seu nome é bem normal')

print('tenha um bom dia {}'.format(nome))
