

class Student:
    def __init__(self, fulltnavn):
        self._fulltnavn = fulltnavn
        self._fagListe = []

    def __str__(self):
        return self._fornavn + " " + self._etternavn

    def leggTilFag(self, fag):
        self._fagListe.append(fag)

    def hentAntallFag(self):
        return len(self._fagListe)

    def hentStudentNavn(self):
        return self._fulltnavn

    def skrivFagPaaStudent(self):
        print(self._fulltnavn + "\n")
        for fag in self._fagListe:
            print(fag.hentFagNavn())
