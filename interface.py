# © Designed and Developed by Mehmet Güdük.
# © Licensed with GPL-3.0 License, Author is Mehmet Güdük.


# The visual and design part of the application is here.


from PyQt5 import QtCore, QtGui, QtWidgets

import currencies


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 400))
        MainWindow.setMaximumSize(QtCore.QSize(500, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/images/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 461, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupbox_HAVE = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupbox_HAVE.setObjectName("groupbox_HAVE")
        self.label_HAVE_title_currencies = QtWidgets.QLabel(self.groupbox_HAVE)
        self.label_HAVE_title_currencies.setGeometry(QtCore.QRect(10, 30, 221, 21))
        self.label_HAVE_title_currencies.setFrameShape(QtWidgets.QFrame.Box)
        self.label_HAVE_title_currencies.setAlignment(QtCore.Qt.AlignCenter)
        self.label_HAVE_title_currencies.setObjectName("label_HAVE_title_currencies")
        self.label_HAVE_selected_currency = QtWidgets.QLabel(self.groupbox_HAVE)
        self.label_HAVE_selected_currency.setGeometry(QtCore.QRect(10, 90, 441, 21))
        self.label_HAVE_selected_currency.setFrameShape(QtWidgets.QFrame.Box)
        self.label_HAVE_selected_currency.setText("")
        self.label_HAVE_selected_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.label_HAVE_selected_currency.setObjectName("label_HAVE_selected_currency")
        self.combobox_HAVE_currencies = QtWidgets.QComboBox(self.groupbox_HAVE)
        self.combobox_HAVE_currencies.setGeometry(QtCore.QRect(10, 50, 221, 22))
        self.combobox_HAVE_currencies.setObjectName("combobox_HAVE_currencies")
        self.currency_icons = []

        def add_currency_icon(abbreviation: str):
            Icon = QtGui.QIcon()
            Icon.addPixmap(
                QtGui.QPixmap(f":/currencies/images/Currencies/{abbreviation.lower()}.png"),
                QtGui.QIcon.Normal,
                QtGui.QIcon.Off
            )
            self.currency_icons.append(Icon)
            self.combobox_HAVE_currencies.addItem(Icon, "")

        for currency in currencies.currencies:
            add_currency_icon(abbreviation=currency['abbreviation'])
        self.label_HAVE_title_crypto_currencies = QtWidgets.QLabel(self.groupbox_HAVE)
        self.label_HAVE_title_crypto_currencies.setGeometry(QtCore.QRect(230, 30, 221, 21))
        self.label_HAVE_title_crypto_currencies.setFrameShape(QtWidgets.QFrame.Box)
        self.label_HAVE_title_crypto_currencies.setAlignment(QtCore.Qt.AlignCenter)
        self.label_HAVE_title_crypto_currencies.setObjectName("label_HAVE_title_crypto_currencies")
        self.combobox_HAVE_crypto_currencies = QtWidgets.QComboBox(self.groupbox_HAVE)
        self.combobox_HAVE_crypto_currencies.setGeometry(QtCore.QRect(230, 50, 221, 22))
        self.combobox_HAVE_crypto_currencies.setObjectName("combobox_HAVE_crypto_currencies")
        self.crypto_currency_icons = []

        def add_crypto_currency_icon(abbreviation: str):
            Icon = QtGui.QIcon()
            Icon.addPixmap(QtGui.QPixmap(f":/crypto currencies/images/Crypto Currencies/{abbreviation.lower()}.png"),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.crypto_currency_icons.append(Icon)
            self.combobox_HAVE_crypto_currencies.addItem(Icon, "")
        for crypto_currency in currencies.crypto_currencies:
            add_crypto_currency_icon(abbreviation=crypto_currency['abbreviation'])
        self.lineedit_HAVE_input = QtWidgets.QLineEdit(self.groupbox_HAVE)
        self.lineedit_HAVE_input.setGeometry(QtCore.QRect(10, 110, 441, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineedit_HAVE_input.setFont(font)
        self.lineedit_HAVE_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly | QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineedit_HAVE_input.setInputMask("")
        self.lineedit_HAVE_input.setText("")
        self.lineedit_HAVE_input.setMaxLength(36)
        self.lineedit_HAVE_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineedit_HAVE_input.setAlignment(QtCore.Qt.AlignCenter)
        self.lineedit_HAVE_input.setClearButtonEnabled(False)
        self.lineedit_HAVE_input.setObjectName("lineedit_HAVE_input")
        self.verticalLayout.addWidget(self.groupbox_HAVE)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_change = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_change.setObjectName("button_change")
        self.horizontalLayout.addWidget(self.button_change)
        self.button_convert = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_convert.setObjectName("button_convert")
        self.horizontalLayout.addWidget(self.button_convert)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupbox_WANT = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupbox_WANT.setObjectName("groupbox_WANT")
        self.label_WANT_title_currencies = QtWidgets.QLabel(self.groupbox_WANT)
        self.label_WANT_title_currencies.setGeometry(QtCore.QRect(10, 30, 221, 21))
        self.label_WANT_title_currencies.setFrameShape(QtWidgets.QFrame.Box)
        self.label_WANT_title_currencies.setAlignment(QtCore.Qt.AlignCenter)
        self.label_WANT_title_currencies.setObjectName("label_WANT_title_currencies")
        self.label_WANT_title_crypto_currencies = QtWidgets.QLabel(self.groupbox_WANT)
        self.label_WANT_title_crypto_currencies.setGeometry(QtCore.QRect(230, 30, 221, 21))
        self.label_WANT_title_crypto_currencies.setFrameShape(QtWidgets.QFrame.Box)
        self.label_WANT_title_crypto_currencies.setAlignment(QtCore.Qt.AlignCenter)
        self.label_WANT_title_crypto_currencies.setObjectName("label_WANT_title_crypto_currencies")
        self.combobox_WANT_currencies = QtWidgets.QComboBox(self.groupbox_WANT)
        self.combobox_WANT_currencies.setGeometry(QtCore.QRect(10, 50, 221, 22))
        self.combobox_WANT_currencies.setObjectName("combobox_WANT_currencies")
        for icon_ in self.currency_icons:
            self.combobox_WANT_currencies.addItem(icon_, "")
        self.combobox_WANT_crypto_currencies = QtWidgets.QComboBox(self.groupbox_WANT)
        self.combobox_WANT_crypto_currencies.setGeometry(QtCore.QRect(230, 50, 221, 22))
        self.combobox_WANT_crypto_currencies.setObjectName("combobox_WANT_crypto_currencies")
        for icon_ in self.crypto_currency_icons:
            self.combobox_WANT_crypto_currencies.addItem(icon_, "")
        self.label_WANT_selected_currency = QtWidgets.QLabel(self.groupbox_WANT)
        self.label_WANT_selected_currency.setGeometry(QtCore.QRect(10, 90, 441, 21))
        self.label_WANT_selected_currency.setFrameShape(QtWidgets.QFrame.Box)
        self.label_WANT_selected_currency.setText("")
        self.label_WANT_selected_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.label_WANT_selected_currency.setObjectName("label_WANT_selected_currency")
        self.lineedit_WANT_output = QtWidgets.QLineEdit(self.groupbox_WANT)
        self.lineedit_WANT_output.setGeometry(QtCore.QRect(10, 110, 441, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineedit_WANT_output.setFont(font)
        self.lineedit_WANT_output.setInputMethodHints(QtCore.Qt.ImhDigitsOnly | QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineedit_WANT_output.setInputMask("")
        self.lineedit_WANT_output.setText("")
        self.lineedit_WANT_output.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineedit_WANT_output.setAlignment(QtCore.Qt.AlignCenter)
        self.lineedit_WANT_output.setReadOnly(True)
        self.lineedit_WANT_output.setClearButtonEnabled(False)
        self.lineedit_WANT_output.setObjectName("lineedit_WANT_output")
        self.verticalLayout.addWidget(self.groupbox_WANT)
        self.verticalLayout.setStretch(0, 45)
        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout.setStretch(2, 45)
        self.lbl_copyright = QtWidgets.QLabel(self.centralwidget)
        self.lbl_copyright.setGeometry(QtCore.QRect(0, 380, 501, 20))
        self.lbl_copyright.setStyleSheet("color: rgb(0, 0, 0);")
        self.lbl_copyright.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_copyright.setObjectName("lbl_copyright")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.combobox_HAVE_currencies.setCurrentIndex(-1)
        self.combobox_HAVE_crypto_currencies.setCurrentIndex(-1)
        self.combobox_WANT_currencies.setCurrentIndex(-1)
        self.combobox_WANT_crypto_currencies.setCurrentIndex(-1)
        self.combobox_HAVE_currencies.currentIndexChanged['QString'].connect(self.label_HAVE_selected_currency.setText)
        self.combobox_HAVE_crypto_currencies.currentIndexChanged['QString'].connect(
            self.label_HAVE_selected_currency.setText)
        self.combobox_WANT_currencies.currentIndexChanged['QString'].connect(self.label_WANT_selected_currency.setText)
        self.combobox_WANT_crypto_currencies.currentIndexChanged['QString'].connect(
            self.label_WANT_selected_currency.setText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Currency Converter"))
        self.groupbox_HAVE.setTitle(_translate("MainWindow", "Currency I Have"))
        self.label_HAVE_title_currencies.setText(_translate("MainWindow", "Currencies"))
        have_currencies_count = 0
        for currency in currencies.currencies:
            self.combobox_HAVE_currencies.setItemText(
                have_currencies_count,
                _translate("MainWindow", f"{currency['abbreviation'].upper()} - {currency['full name']}")
            )
            have_currencies_count += 1
        self.label_HAVE_title_crypto_currencies.setText(_translate("MainWindow", "Crypto Currencies"))
        have_crypto_currencies_count = 0
        for crypto_currency in currencies.crypto_currencies:
            self.combobox_HAVE_crypto_currencies.setItemText(
                have_crypto_currencies_count,
                _translate("MainWindow", f"{crypto_currency['abbreviation'].upper()} - {crypto_currency['full name']}")
            )
            have_crypto_currencies_count += 1
        self.lineedit_HAVE_input.setPlaceholderText(_translate("MainWindow", "0.00"))
        self.button_change.setText(_translate("MainWindow", "⇵"))
        self.button_convert.setText(_translate("MainWindow", "Convert"))
        self.groupbox_WANT.setTitle(_translate("MainWindow", "Currency I Want"))
        self.label_WANT_title_currencies.setText(_translate("MainWindow", "Currencies"))
        self.label_WANT_title_crypto_currencies.setText(_translate("MainWindow", "Crypto Currencies"))
        want_currencies_count = 0
        for currency in currencies.currencies:
            self.combobox_WANT_currencies.setItemText(
                want_currencies_count,
                _translate("MainWindow", f"{currency['abbreviation'].upper()} - {currency['full name']}")
            )
            want_currencies_count += 1
        want_crypto_currencies_count = 0
        for crypto_currency in currencies.crypto_currencies:
            self.combobox_WANT_crypto_currencies.setItemText(
                want_crypto_currencies_count,
                _translate("MainWindow", f"{crypto_currency['abbreviation'].upper()} - {crypto_currency['full name']}")
            )
            want_crypto_currencies_count += 1
        self.lbl_copyright.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-size:7pt; color:#000000;\">© Designed and Developed by </span><a href=\"https://github.com/mehmetguduk\"><span style=\" font-size:7pt; text-decoration: underline; color:#0000ff;\">Mehmet Güdük</span></a></p></body></html>"))


import images
