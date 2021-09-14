import time
from time import sleep
import os
import sys
alder = 17
navn = 'Henrik Ø'
hobby = ''
def start():
    os.system('cls')
    s1 = 'Hei, jeg er en chatbot\n\n1. Navn\n2. Alder\n3. Hobbyer og interesser\n4. Teknologier\n5. Avslutt'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    print('\n');sleep(0.1)
    valg=input('>')
    if valg == '1':
        navn1()
    elif valg == '2':
        alder1()
    elif valg == '3':
        hobby1()
    elif valg == '4':
        tek1()
    elif valg == '5':
        avslutt()
    else:
        start()
def navn1():
    global navn
    os.system('cls')
    s1 = 'Jeg heter '+ navn +'.'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    print('\n');sleep(0.1)
    input('Trykk på ENTER for å gå tilbake')
    start()
def alder1():
    global alder
    os.system('cls')
    s2 = 'Jeg er '+str(alder)+' år gammel'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    print('\n');sleep(0.1)
    input('Trykk på ENTER for å gå tilbake')
    start()
def hobby1():
    os.system('cls')
    s3 = 'Hobbyene mine er å trene, gå på fjellturer og data.'
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    print('\n');sleep(0.1)
    input('Trykk på ENTER for å gå tilbake')
    start()
def tek1():
    os.system('cls')
    s4 = 'Jeg er godt kjent med Windows og ledeteksten/batch.\nHar også litt erfaring fra forskjellige varianter av Unix.\nJeg er flink med maskinvare.\nJeg har litt erfaring i Python, html, css og litt c#.\nPrøvde meg på en gang 8086 assembly, men ja, nei.'
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    print('\n');sleep(0.1)
    input('Trykk på ENTER for å gå tilbake')
    start()
def avslutt():
    os.system('cls')
    sys.exit()
start()