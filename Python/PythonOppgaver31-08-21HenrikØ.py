import random

def oppg1():
    frukt = "agurk"
    grønnsak = "eple"
    print('Frukt: '+frukt)
    print('Grønnsak: '+grønnsak)
    bruh = frukt
    frukt = grønnsak
    grønnsak = bruh
    print('Frukt: '+frukt)
    print('Grønnsak: '+grønnsak)

#oppg2
#Den skriver ut du heter Maren eller er 22 år.

def oppg3():
    t1=14
    t2=7
    t3=11
    print('\nTall 1 er: '+str(t1)+'\nTall 2 er: '+str(t2)+'\nTall 3 er: '+str(t3)+'\n')
    if t1 > t2 and t3:
        print('Tall 1 er størst')
    elif t2 > t1 and t3:
        print('Tall 2 er størst')
    elif t3 > t1 and t3:
        print('Tall 3 er størst')

def oppg4():
    n1="Jonatan"
    n2="Tobias"
    len1=len(n1)
    len2=len(n2)
    if len(str(n2)) > len1:
        print(n2+' er lengere enn '+n1)
    elif len(str(n1)) > len2:
        print(n1+' er lengere enn '+n2)

def oppg5():
    start=1
    slutt=12
    #start til slutt
    print('start')
    for bruh in range(start, slutt):
        print(''+str(bruh)+'')
    print('ferdig')
    #slutt til start
    print('\nstart')
    for bruh in range(slutt, start, -start):
        print(''+str(bruh)+'')
    print('ferdig')

def oppg6():
    tall=0
    while tall !=9:
        input('Trykk på en tast')
        tall = random.randint(1, 999)
        print(tall)
        if tall != 571:
            print('lessss go')

oppg5()