import time
import webbrowser

def inputNumber(message):
  while True:
    try:
       Benutzereingabe = int(input(message))       
    except ValueError:
       print("Das ist keine ganze Zahl! Bitte versuche es noch einmal.")
       continue
    else:
       return Benutzereingabe
       break 

url = 'https://www.youtube.com/watch?v=5qap5aO4i9A'

Lernzeit = inputNumber("Hallo! Ich bin ein Pomodoro Timer.\n Bitte gebe jetz deine gewünschte Lernzeit in Sekunden ein.")
while 1> Lernzeit and Lernzeit >6000:
    print ("Versuche es noche einmal!")  
    Lernzeit = inputNumber()

Pausenzeit = inputNumber("Bitte gebe jetz deine gewünschte Pausenzeit in Sekunden ein.")
while 1> Pausenzeit and Pausenzeit >600000000:
    Pausenzeit = inputNumber("Versuche es noche einmal!")

print ("Vielen Dank, Deine Lernzeit ist:", Lernzeit)
print ("Deine Pausenzeit ist:", Pausenzeit)

time.sleep(Lernzeit)
print ("Hi, du hast dir eine Pause verdient. Hier kommen deine Lieblingssongs!")
webbrowser.open(url)
time.sleep(Pausenzeit)

print ("Brauchst Du ein Warmup? Möchtest DU das Zahlenratespiel spielen? (Ja/Nein)")

if input() == "ja":
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

if input()== "nein":
    exit
