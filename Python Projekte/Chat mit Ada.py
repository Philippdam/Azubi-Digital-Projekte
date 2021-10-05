# -*- coding: utf-8 -*-

NameUser = input ("Hallo! Ich bin ein Chatbot.\nWenn du wissen willst,wie ich heiße, frage micht einfach.\nWie heißt du?\n")
print ("Hallo", NameUser, "du heißt ja genau wie mein Haustier! So ein Zufall! hihi.\nWie alt bist du?\n")

Alter = int(input())
if Alter < 18:
    print ("Du bist ja jung, du BABY!\n Magst du Menschen? Ja oder Nein?\n")
if Alter >= 18:
    print ("Du bist ja alt...Du alte Schachtel!\n Magst du Menschen?Ja oder Nein?\n")
if input() ==  "ja"or input() == "yes" or input() == "jo":
    print ("OMG. ICH AUCH! Poka ! Poka!\n  Das ist Russisch und heißt Bye! Bye!")
else:
    print ("OMG. ICH AUCH!\n. Poka ! Poka! Das ist Russisch und heißt Bye! Bye!")

if input() ==  "nein"or input() == "no" or input() == "ne":
    print ("OMG. ICH AUCH!\n. Poka ! Poka! Das ist Russisch und heißt Bye! Bye!")
else:
    print ("OMG. ICH AUCH!\n. Poka ! Poka! Das ist Russisch und heißt Bye! Bye!")

if input() ==  "Wie heißt du?"or input() == "Wie ist dein Name?" or input() == "What´s your name?":
    print ("Ich heiße Ada, Bby!")

