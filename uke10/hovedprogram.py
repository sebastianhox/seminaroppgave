from fag import Fag
from student import Student

def hovedprogram():
    in1000 = Fag("IN1000")
    in1020 = Fag("IN1020")
    inec1821 = Fag("INEC1821")

    seb = Student("Sebastian")
    seb1 = Student("Sebasti")
    seb2 = Student("Seba")

    in1000.leggTilStudent(seb1)
    in1020.leggTilStudent(seb1)
    inec1821.leggTilStudent(seb)
    seb1.leggTilFag(in1000)
    seb1.leggTilFag(in1020)
    seb.leggTilFag(inec1821)
    in1000.leggTilStudent(seb)

    seb1.skrivFagPaaStudent()
    print(seb1.hentStudentNavn(), seb1.hentAntallFag())
    in1000.skrivStudenterVedFag()


hovedprogram()
