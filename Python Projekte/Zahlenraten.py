import random
Counter = 0
GesuchteZahl = random.randint(1,100)
while Counter < 6:
    Spielerantwort = int(input("Errate die gesuchte Zahl zwischen 1 und 100, Arrrr!\n"))

    
    Counter = Counter + 1
    print ("Anzahl Counter benutzt: ",Counter)

    if Spielerantwort == GesuchteZahl:
        print ("Beim klabautermann! Gratulation! DU BIST SCHATZ! Arrrrr!")

    if Spielerantwort < GesuchteZahl:
        print ("Zu niedrig, du Landratte!")

    if Spielerantwort > GesuchteZahl:
        print ("Zu hoch!")
print ("GAME OVER! DU WIRST JETZT KIEL GEHOLT!\n HAR HAR HAR!")