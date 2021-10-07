import time

print ("Hallo. Bitte beantnworte 10 Fragen, oder die Welt explodiert!")
print ("Ich gebe Dir dafür 30 Sekunden Zeit!")
print ("Fage 1: Wie heißt die Hauptstadt von Deutschland?\n")
time.sleep(30)
print ("Die Zeit ist nun um!\nWas ist deine Antwort?")

if input() == "Berlin":
    print ("Richtig. Frage 2: Bin ich ein Mensch oder eine Maschiene?\n")
else: print ("Falsch!\nFrage 2: Bin ich ein Mensch oder eine Maschiene?\n")
time.sleep(30)
print ("Die Zeit ist nun um!\nWas ist deine Antwort?")

if input() == "Maschiene":
    print ("Richtig. Frage 3: In welchen Zug passt nur ein Mensch?\n")
else: print ("Falsch!\nFrage 3: In welchen Zug passt nur ein Mensch?\n")
time.sleep(30)
print ("Die Zeit ist nun um!\nWas ist deine Antwort?")

if input() == "Anzug":
    print ("Korrekt! Frage 4: Womit fängt der Tag an und hört die Nacht auf?\n")
else: print ("Falsch!\nFrage 4:  Womit fängt der Tag an und hört die Nacht auf?\n")
time.sleep(30)
print ("Die Zeit ist nun um!\nWas ist deine Antwort?")

if input() == "T" or "t":
    print ("Korrekt! Frage 5: Wer hat Hühneraugen am Kopf?\n")
else: print ("Falsch!\nFrage 5:  Wer hat Hühneraugen am Kopf?\n")
time.sleep(30)
print ("Die Zeit ist nun um!\nWas ist deine Antwort?")

if input() == "Huhn" or "Hühner" or "Huehner":
    print ("Richtig. Frage 6: Welches Tier ist reich?\n")
else: print ("Falsch!\nFrage 6: Welches Tier ist reich?\n")
time.sleep(30)
print ("Die Zeit ist nun um!\nWas ist deine Antwort?")

if input() == "Sparschwein":
    print ("Richtig. Frage 7: Wie heißt der Ring mit vier Ecken?\n")
else: print ("Falsch!\nFrage 7: Wie heißt der Ring mit vier Ecken?\n")
time.sleep(30)
print ("DIe Zeit ist nun um!\nWas ist deine Antwort?")

if input() == "Boxring":
    print ("Korrekt! Frage 8: An welcher Angst leidet jeder Luftballon?\n")
else: print ("Falsch!\nFrage 8: An welcher Angst leidet jeder Luftballon?\n")
time.sleep(30)
print ("Die Zeit ist nun um!\nWas ist deine Antwort?")

if input() == "Platzangst" or "platzen":
    print ("Korrekt! Frage 9: Bei welchem Stich blutet man nicht?\n")
else: print ("Falsch!\nFrage 9:  Bei welchem Stich blutet man nicht?\n")
time.sleep(30)
print ("Die Zeit ist nun um!\nWas ist deine Antwort?")

if input() == "Sonnenstich":
    print ("Korrekt! Frage 10: Was überwältig auch den/die stärksten Mann/Frau?\n")
else: print ("Falsch!\nFrage 10: Was überwältig auch den/die stärksten Mann/Frau?\n")
time.sleep(30)
print ("Die Zeit ist nun um!\nWas ist deine Antwort")

if input() == "Schlaf":
    print ("Korrekt! Du hast alle Fragen beantwortet. Die Welt wurde gerettet.\nHerzlichen Dank!")
else: print ("Korrekt! Du hast alle Fragen beantwortet. Die Welt wurde gerettet.\nHerzlichen Dank!")
