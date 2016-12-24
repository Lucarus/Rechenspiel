import time
import random


class Aufgabe:
    a = 0
    b = 0
    ergebnis = 0
    startZeit = 0
    endZeit = 0
    falscheingabe = 0
    aufgabe = 0

    def __init__(self, aufgabe):
        random.seed()
        self.startZeit = time.localtime()
        self.a = random.randint(10, 30)
        self.b = random.randint(10, 30)
        self.ergebnis = self.a + self.b
        self.aufgabe = aufgabe

    def __str__(self):
        return "Aufgabe " + self.aufgabe + ": " + self.a + " + " + self.b

    def beantworten(self):
        eingabe = -1

        while eingabe != self.ergebnis:
            try:
                print("Bitte Ergebnis eingeben")
                eingabe = int(input())
                if self.ergebnis == eingabe:
                    print("+++ R I C H T I G +++")
                    self.endZeit = time.localtime()
                    return 1
                else:
                    print("+++ F A L S C H +++")
                    self.falscheingabe += 1
            except:
                continue

    def get_zeit(self):
        return self.endZeit - self.startZeit

    def get_fehler(self):
        return self.falscheingabe
