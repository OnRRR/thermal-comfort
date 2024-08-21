import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSlot
from arayuz import *
from secondwindow import *

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.first_window = QtWidgets.QMainWindow()
        self.first_ui = Ui_MainWindow()
        self.first_ui.setupUi(self.first_window)
        self.first_ui.onayla_pushButton.clicked.connect(self.onayla_clicked) #Onayla butonu fonksiyonunu bağlama işlemi
        
        #İkinci pencereyi tanımlama                      
        self.second_window = QtWidgets.QMainWindow()
        self.second_ui = Ui_SecondWindow()
        self.second_ui.setupUi(self.second_window)
        self.second_ui.evet_pushButton.clicked.connect(self.evet_clicked) #Evet butonu fonksiyonunu bağlama işlemi
        self.second_ui.hayir_pushButton.clicked.connect(self.evet_clicked) #Hayır butonu fonksiyonunu bağlama işlemi
        

        #Pencereyi açma
        self.first_window.show()

    def onayla_clicked(self):
        if not self.first_ui.checkBox.isChecked():
            QMessageBox.warning(None, "Uyarı", "Devam etmek için lütfen kişisel verilerinizin kullanılmasına izin verin.")
            return
        name = self.first_ui.get_name()
        surname = self.first_ui.get_surname()
        selected_city = self.first_ui.get_selected_city()
        selected_gender = self.first_ui.get_selected_gender()
        selected_country = self.first_ui.get_selected_country()
        height = self.first_ui.get_height()
        weight = self.first_ui.get_weight()
        selected_clothing = self.first_ui.get_selected_clothing()
        selected_activity_level = self.first_ui.get_selected_activity_level()

        # Bu değerleri daha sonra kullanabilirsiniz, örneğin ekrana yazdırmak için:
        print(f"Ad: {name}, Soyad: {surname}")
        print(f"Şehir: {selected_city}, Cinsiyet: {selected_gender}, Ülke: {selected_country}")
        print(f"Boy: {height}, Kilo: {weight}")
        print(f"Kıyafet Tercihi: {selected_clothing}, Hareketlilik Seviyesi: {selected_activity_level}")

        self.first_window.hide()
        self.second_window.show()

    def evet_clicked(self):
        print("Evetttttt")

    def hayir_clicked(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec())

