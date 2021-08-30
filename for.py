from time import sleep
import os
def telle():
    print('start')
    for bruh in range(1, 71):
        print(''+str(bruh)+'');sleep(0.01)
        if bruh==70/2:
            print('halvveis')
        elif bruh%3==0 or bruh%5==0:
            print(''+str(bruh)+' *');sleep(0.01)
    print('ferdig')

elever = []
def liste():
    global elever
    os.system('cls')
    elev=str(input('Skriv et navn: '))
    if elev != 'stopp':
        os.system('exit')
    while elev not in 'stopp':
        elever.append(elev)
        elever.sort()
        print(elever)
        elev=str(input('Skriv et navn: '))
        if elev != 'stopp':
            os.system('exit')
liste()