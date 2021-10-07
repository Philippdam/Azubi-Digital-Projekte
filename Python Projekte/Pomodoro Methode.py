import time
import webbrowser

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Das ist keine ganze Zahl! Bitte versuche es noch einmal.")
       continue
    else:
       return userInput 
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