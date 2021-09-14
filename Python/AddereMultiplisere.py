import os
from time import sleep
def s():
    os.system('cls') 
    print('Hva skal du?')
    print('1. Addisjon')
    print('2. Multiplikasjon')
    print('3. Ingen ting')
    bruh=input('> ')
    if bruh == '1':
        a()
    elif bruh == '2':
        m()
    elif bruh == '3':
        sheesh()
    else:
       s()
def a():
    os.system('cls')
    print('Addisjon')
    t1=int(input('Tall 1 er: '))
    t2=int(input('Tall 2 er: '))
    t3=t1+t2
    print(''+str(t1)+' + '+str(t2)+' = '+str(t3)+'');sleep(3)
    s()
def m():
    os.system('cls')
    print('Multiplikasjon')
    t1=int(input('Tall 1 er: '))
    t2=int(input('Tall 2 er: '))
    t3=t1*t2
    print(''+str(t1)+' x '+str(t2)+' = '+str(t3)+'');sleep(3)
    s()
def sheesh():
    os.system('cls')
    os.system('exit')
s()