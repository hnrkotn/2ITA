#terningkast
import random
t1=0
t2=0
while t1 + t2 !=12:
    input('Trykk på en tast')
    t1 = random.randint(1, 6)
    t2 = random.randint(1, 6)
    print(t1 + t2)
