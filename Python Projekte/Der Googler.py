import webbrowser

url = 'https://www.google.de/'
print ("Hallo brauchst du Hilfe? Dann tippe 'suche' ein.\n")


Sucheingabe = input()

while Sucheingabe != ("suche"):
    print ("Versuche es noch einmal. Bitte gebe den Befehl \"suche\" ein")  
    Sucheingabe = input() 


print("Befehl wurde korrekt erkannt. Browser wird gestartet!")
webbrowser.open(url)
