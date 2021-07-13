# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json


# region FUNCTIONS FOR CLEAR BUTTON
def Clear_Action(self):
    return self.clear()


def Clear_Button(self):
    self.point = Clear_Action(self.label_1.text(''))
    return self.point
# endregion


class Ui_MainWindow(object):

    def search_func(self):
        url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/northamerica"

        headers = {
            'x-rapidapi-key': "543e54c744msha7971f8ca4fada5p1ff971jsn7f52d8a38f3a",
            'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        data = json.loads(response.text)

        point = self.input.text()

        for i in data:
            if i['Country'] == point:
                self.label_1.setText('\t\t\t     {}\n\t\t\t     TotalDeaths: {}'.format(
                    i['Country'], i['TotalDeaths']))
                break
        else:
            self.label_1.setText('\t\t\t             Undefined')

    def update_func(self):
        url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/northamerica"

        headers = {
            'x-rapidapi-key': "543e54c744msha7971f8ca4fada5p1ff971jsn7f52d8a38f3a",
            'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        data = json.loads(response.text)

        self.label_2.setText("\t\t\t" "     Country: USA" "\n" "\t\t\t" "     Continent: North America" "\n" "\t\t\t" "     TotalDeaths: {} " "\n"
                             "\n\n"
                             "\t\t\t" "     Country: Mexico" "\n" "\t\t\t" "     Continent: North America" "\n" "\t\t\t" "     TotalDeaths: {}" "\n"
                             "\n\n"
                             "\t\t\t" "     Country: Canada" "\n" "\t\t\t" "     Continent: North America" "\n" "\t\t\t" "     TotalDeaths: {}" "\n"
                             "\n\n"
                             "\t\t\t" "     Country: Panama" "\n" "\t\t\t" "     Continent: North America" "\n" "\t\t\t" "     TotalDeaths: {}" "\n"
                             "\n\n"
                             "\t\t\t" "     Country: Costa Rica" "\n" "\t\t\t" "     Continent: North America" "\n" "\t\t\t" "     TotalDeaths: {}" .format(data[0]['TotalDeaths'], data[1]['TotalDeaths'], data[2]['TotalDeaths'], data[3]['TotalDeaths'], data[4]['TotalDeaths']))

    def setupUi(self, MainWindow):

        # region MAINWINDOW
        MainWindow.setObjectName("MainWindow")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #282a36;\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # endregion

        # region INPUT
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(20, 30, 581, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.input.setFont(font)
        self.input.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input.setStyleSheet("background-color: #242631;\n"
                                 "border: 1px solid #20222c;\n"
                                 "border-radius: 30;\n"
                                 "color: #d6ddd8;\n"
                                 "\n"
                                 "\n"
                                 "")
        self.input.setLocale(QtCore.QLocale(
            QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.input.setText("")
        self.input.setMaxLength(20)
        self.input.setAlignment(QtCore.Qt.AlignCenter)
        self.input.setReadOnly(False)
        self.input.setObjectName("input")
        # endregion

        # region SEARCH
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(540, 40, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.search.setFont(font)
        self.search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search.setStyleSheet("QPushButton {\n"
                                  "    background-color: none;\n"
                                  "    border: none;\n"
                                  "    border-radius: 10;\n"
                                  "    color: #b9bbbe;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::pressed {\n"
                                  "    background-color: #282a36;\n"
                                  "}")
        self.search.setObjectName("search")
        # endregion

        # region UPDATE
        self.update = QtWidgets.QPushButton(self.centralwidget)
        self.update.setGeometry(QtCore.QRect(40, 130, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.update.setFont(font)
        self.update.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.update.setStyleSheet("QPushButton {\n"
                                  "    background-color: #242631;\n"
                                  "    border: 1px solid #20222c;\n"
                                  "    border-radius: 20;\n"
                                  "    color: #6fc58d;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::pressed {\n"
                                  "    background-color: none;\n"
                                  "}")
        self.update.setLocale(QtCore.QLocale(
            QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.update.setObjectName("update")
        # endregion

        # region CLEAR
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(380, 130, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clear.setFont(font)
        self.clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear.setStyleSheet("QPushButton {\n"
                                 "    background-color: #242631;\n"
                                 "    border: 1px solid #20222c;\n"
                                 "    border-radius: 20;\n"
                                 "    color: #f77d42;\n"
                                 "}\n"
                                 "QPushButton::pressed {\n"
                                 "    background-color: none;\n"
                                 "}")
        self.clear.setLocale(QtCore.QLocale(
            QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.clear.setObjectName("clear")
        # endregion

        # region LABEL_1
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setGeometry(QtCore.QRect(10, 230, 601, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_1.setFont(font)
        self.label_1.setContentsMargins(10, 40, 10, 10)
        self.label_1.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_1.setStyleSheet("color: #2d68be;\n"
                                   "background-color: #242631;\n"
                                   "border: 1px solid #20222c;")
        self.label_1.setLocale(QtCore.QLocale(
            QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_1.setText("")
        self.label_1.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_1.setIndent(0)
        self.label_1.setObjectName("label_1")
        MainWindow.setCentralWidget(self.centralwidget)
        # endregion

        # region LABEL_2
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 380, 601, 521))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setContentsMargins(10, 15, 10, 10)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_2.setStyleSheet("color: #b48900;\n"
                                   "background-color: #242631;\n"
                                   "border: 1px solid #20222c;")
        self.label_2.setLocale(QtCore.QLocale(
            QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_2.setText("")
        self.label_2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        # endregion

        # region BUTTON INTERACTION
        self.update_func()
        self.clear.clicked.connect(self.label_1.clear)
        self.search.clicked.connect(self.search_func)
        self.update.clicked.connect(self.update_func)
        # endregion

        # region NECESSARY THINGS
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.search, self.input)
        # endregion

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "COVID-19 NA"))
        self.search.setText(_translate("MainWindow", "🔍"))
        self.update.setText(_translate("MainWindow", "Update"))
        self.clear.setText(_translate("MainWindow", "Clear"))
