import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem, QMessageBox

from layout import Ui_Dialog


class MyForm(QDialog):
        def __init__(self):
            super().__init__()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self)
            self.ui.save.clicked.connect(self.wyswietl)
            self.ui.pushButton_savetofile.clicked.connect(self.wyswietl)
            self.show()

        def wyswietl(self):
            name = self.ui.name.text().strip()
            secondname = self.ui.secondname.text().strip()
            pesel = self.ui.pesel.text().strip()
            numbertl = self.ui.numberofphone.text().strip()

            lista = ["imie ",name, "nazwisko ",secondname, "pesel " ,pesel, "numertelefonu ",numbertl]

            dane = name + " " + secondname

            waga = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
            suma_kontrolna = sum(int(pesel[i]) * waga[i] for i in range(10))
            numer_kontrolny = (10 - (suma_kontrolna % 10)) % 10


            if name == "" or secondname == "" or pesel == "" or numbertl == "":
                blad = QMessageBox()
                blad.setText("Pola wymagane")
                blad.exec()

            if len(pesel) != 11 or not pesel.isnumeric():
                blad = QMessageBox()
                blad.setText("Pesel nie zawiera numeru lub nie ma 11 znaków")
                blad.exec()


            if numer_kontrolny == int(pesel[10]):
                self.ui.listofuser.addItem(dane)
                plik = open(f'{name}.txt', 'w')
                lista_nowa = []
                for i in lista: lista_nowa.append(i + '\n')
                plik.writelines(lista_nowa)
                plik.close()

            else:
                blad = QMessageBox()
                blad.setInformativeText("Nieprawidłowy numer PESEL")
                blad.exec()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())