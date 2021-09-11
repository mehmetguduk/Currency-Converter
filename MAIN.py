# © Designed and Developed by Mehmet Güdük.
# © Licensed with GPL-3.0 License, Author is Mehmet Güdük.


import sys
import requests
from PyQt5 import QtWidgets
from interface import Ui_MainWindow
from bs4 import BeautifulSoup

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.combobox_HAVE_currencies.currentIndexChanged.connect(self.clear_one)
        self.ui.combobox_HAVE_crypto_currencies.currentIndexChanged.connect(self.clear_two)
        self.ui.combobox_WANT_currencies.currentIndexChanged.connect(self.clear_three)
        self.ui.combobox_WANT_crypto_currencies.currentIndexChanged.connect(self.clear_four)
        self.ui.lineedit_HAVE_input.textChanged.connect(self.correct_input)
        self.ui.button_convert.clicked.connect(self.converter)
        self.ui.button_change.clicked.connect(self.change)

    def clear_one(self):
        if self.ui.combobox_HAVE_currencies.currentIndex() != -1:
            self.ui.combobox_HAVE_crypto_currencies.setCurrentIndex(-1)
    def clear_two(self):
        if self.ui.combobox_HAVE_crypto_currencies.currentIndex() != -1:
            self.ui.combobox_HAVE_currencies.setCurrentIndex(-1)
    def clear_three(self):
        if self.ui.combobox_WANT_currencies.currentIndex() != -1:
            self.ui.combobox_WANT_crypto_currencies.setCurrentIndex(-1)
    def clear_four(self):
        if self.ui.combobox_WANT_crypto_currencies.currentIndex() != -1:
            self.ui.combobox_WANT_currencies.setCurrentIndex(-1)

    def correct_input(self):
        self.ui.lineedit_WANT_output.clear()
        try:
            input = float(self.ui.lineedit_HAVE_input.text())
        except ValueError:
            self.ui.lineedit_HAVE_input.clear()

    def converter(self):
        if self.ui.label_HAVE_selected_currency.text() != "" and self.ui.label_WANT_selected_currency.text() != "" and self.ui.lineedit_HAVE_input.text() != "":
            have = self.ui.label_HAVE_selected_currency.text().split("-")[0].strip()
            want = self.ui.label_WANT_selected_currency.text().split("-")[0].strip()

            url = f"https://currency.world/tr/convert/{have}_1/{want}"
            response = requests.get(url)
            html = response.content 
            soup = BeautifulSoup(html, "html.parser")
            result = soup.find("input", {"id":"amountv1"})['value']
            result = float(result.replace(",",".")) * float(self.ui.lineedit_HAVE_input.text())

            if float(result) == int(result):
                self.ui.lineedit_WANT_output.setText(str(int(result)))
            else:
                self.ui.lineedit_WANT_output.setText(str(result))

    def change(self):
        have_currency_index = self.ui.combobox_HAVE_currencies.currentIndex()
        have_crypto_index = self.ui.combobox_HAVE_crypto_currencies.currentIndex()
        want_currency_index = self.ui.combobox_WANT_currencies.currentIndex()
        want_crypto_index = self.ui.combobox_WANT_crypto_currencies.currentIndex()

        self.ui.combobox_HAVE_currencies.setCurrentIndex(want_currency_index)
        self.ui.combobox_HAVE_crypto_currencies.setCurrentIndex(want_crypto_index)
        self.ui.combobox_WANT_currencies.setCurrentIndex(have_currency_index)
        self.ui.combobox_WANT_crypto_currencies.setCurrentIndex(have_crypto_index)

        self.ui.lineedit_HAVE_input.clear()
        self.ui.lineedit_WANT_output.clear()


if __name__ == '__main__': 
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())