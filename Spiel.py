from Aufgabe import Aufgabe
import time

aufgaben_menge = 0
fehl_eingaben = 0
aufgaben_zeit = time.mktime((0, 0, 0, 0, 0, 0, 0, 0, 0))

print("Menge an Fragen eingeben:")
while aufgaben_menge <= 0 or aufgaben_menge >= 30:
    try:
        aufgaben_menge = int(input())
    except:
        continue

for i in range(1, aufgaben_menge + 1):
    aufgabe = Aufgabe(i)
    print(aufgabe)
    aufgabe.beantworten()

    fehl_eingaben += aufgabe.get_fehler()

print("Fertig!")
print("Auswertung:")
print("Aufgaben: " + str(aufgaben_menge))
print("Fehler: " + str(fehl_eingaben))
print(aufgaben_zeit)