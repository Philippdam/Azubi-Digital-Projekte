from collections import Counter
import random
Counter = 0

Maxcap = 30
while Counter<Maxcap:
    wuerfelzahl = random.randint(1,6)
    print ("Gewürfelte Zahl ist: ", wuerfelzahl)
    Counter = Counter + 1
    print ("Anzahl Counter benutzt: ",Counter)



    