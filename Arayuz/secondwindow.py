# Form implementation generated from reading ui file 'C:/Everything-Python/QtDesigner-Projects/secondwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(903, 716)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        SecondWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plotWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.plotWidget.setGeometry(QtCore.QRect(30, 130, 811, 151))
        self.plotWidget.setObjectName("plotWidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 90, 531, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 320, 621, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 370, 861, 71))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(24)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(23, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 500, 811, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 530, 341, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(14)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.evet_pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.evet_pushButton.setObjectName("evet_pushButton")
        self.horizontalLayout.addWidget(self.evet_pushButton)
        self.hayir_pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.hayir_pushButton.setObjectName("hayir_pushButton")
        self.horizontalLayout.addWidget(self.hayir_pushButton)
        SecondWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "SecondWindow"))
        self.label.setText(_translate("SecondWindow", "Merhaba, sizin için özelleştirilmiş ısıtma/soğutma sistemine hoşgeldiniz."))
        self.label_2.setText(_translate("SecondWindow", "Yarına ait tahmin edilen sıcaklık değerleri aşağıda gösterilen şekildedir."))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("SecondWindow", "Sıcaklık (°C)"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SecondWindow", "00:00"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SecondWindow", "01:00"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SecondWindow", "02:00"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SecondWindow", "03:00"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("SecondWindow", "04:00"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("SecondWindow", "05:00"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("SecondWindow", "06:00"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("SecondWindow", "07:00"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("SecondWindow", "08:00"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("SecondWindow", "09:00"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("SecondWindow", "10:00"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("SecondWindow", "11:00"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("SecondWindow", "12:00"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("SecondWindow", "13:00"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("SecondWindow", "14:00"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("SecondWindow", "15:00"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("SecondWindow", "16:00"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("SecondWindow", "17:00"))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("SecondWindow", "18:00"))
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("SecondWindow", "19:00"))
        item = self.tableWidget.horizontalHeaderItem(20)
        item.setText(_translate("SecondWindow", "20:00"))
        item = self.tableWidget.horizontalHeaderItem(21)
        item.setText(_translate("SecondWindow", "21:00"))
        item = self.tableWidget.horizontalHeaderItem(22)
        item.setText(_translate("SecondWindow", "22:00"))
        item = self.tableWidget.horizontalHeaderItem(23)
        item.setText(_translate("SecondWindow", "23:00"))
        self.label_3.setText(_translate("SecondWindow", "Isıtma/Soğutma sisteminin otomatik bir şekilde ayarlanmasını ister misiniz?"))
        self.evet_pushButton.setText(_translate("SecondWindow", "Evet"))
        self.hayir_pushButton.setText(_translate("SecondWindow", "Hayır"))
