import Aufgabe

class Spiel:

    aufgaben_menge = 0
    fehl_eingaben = 0

    def __init__(self):
        print("Menge an Fragen eingeben:")
        while self.aufgaben_menge <= 0 or self.aufgaben_menge >= 30:
            try:
                self.aufgaben_menge = int(input())
            except:
                continue

        for i in range(1, self.aufgaben_menge + 1):
            aufgabe = Aufgabe(i)
            aufgabe.beantworten()

            self.fehl_eingaben += aufgabe.get_fehler()

        print("Fertig!")
        print("Auswertung:")
        print("Aufgaben: " + self.aufgaben_menge)
        print("Fehler: " + self.fehl_eingaben)