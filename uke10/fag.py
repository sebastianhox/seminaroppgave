from student import Student

class Fag:
    def __init__(self, navn):
        self._navn = navn
        self._studenter = []

    def leggTilStudent(self, student):
        self._studenter.append(student)

    def hentAntallStudenter(self):
        return len(self._studenter)

    def hentFagNavn(self):
        return self._navn

    def skrivStudenterVedFag(self):
        print(self._navn + "\n")
        for student in self._studenter:
            print(student.hentStudentNavn())
