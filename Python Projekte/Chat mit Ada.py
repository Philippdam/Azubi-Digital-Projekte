# -*- coding: utf-8 -*-

NameUser = input ("Hallo! Ich bin ein Chatbot.\nWenn du wissen willst,wie ich heiße, frage mich einfach.\nWie heißt du?\n")
print ("Hallo", NameUser, "du heißt ja genau wie mein Haustier! So ein Zufall! hihi.\nWie alt bist du?\n")

Alter = int(input())
if Alter < 18:
    print ("Du bist ja jung, du BABY!\nIch bin schon ganze 1 Tag alt! Magst du Züge? Ja oder Nein?\n")
if Alter >= 18:
    print ("Du bist ja alt...Ich bin schon 1 Tag alt!\n Magst du Züge? Ja oder Nein?\n")
if input() == "ja" or input == "Ja" or input() == "yes" or input() == "jo":
    print ("OH MEIN PROGRAMMIERGOTT!\nICH AUCH!\nBye! Bye!")
else:
    print ("OH MEIN PROGRAMMIERGOTT!\nJetzt lösche ich alle deine Daten auf deinem PC. Bye! Bye!")

if input() ==  "Wie heißt du?"or input() == "Wie ist dein Name?" or input() == "what's your name":
    print ("Ich heiße Ada! Merke dir den Namen gut, BABY!")

