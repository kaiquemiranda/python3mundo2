from time import sleep
for count in range(0, 51, 2):
    if count % 2 == 0:
        sleep(0.2)
        print(count, end=' ')
print('fim')


