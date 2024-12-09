from PyQt6 import QtCore, QtWidgets
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from View.user_info_w_service import *
from View.time_sheet_window import Time_Sheet

class UserInfoWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.User_Ui()

    def User_Ui(self):
        self.resize(657, 430)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.label_full_name = QtWidgets.QLabel(self.centralwidget)
        self.label_full_name.setGeometry(QtCore.QRect(20, 40, 290, 30))
        self.label_full_name.setObjectName("label_full_name")

        self.label_role = QtWidgets.QLabel(self.centralwidget)
        self.label_role.setGeometry(QtCore.QRect(20, 80, 290, 30))
        self.label_role.setObjectName("label_role")

        self.label_phone_number = QtWidgets.QLabel(self.centralwidget)
        self.label_phone_number.setGeometry(QtCore.QRect(20, 120, 290, 30))
        self.label_phone_number.setObjectName("label_phone_number")

        self.label_birthday = QtWidgets.QLabel(self.centralwidget)
        self.label_birthday.setGeometry(QtCore.QRect(20, 160, 290, 30))
        self.label_birthday.setObjectName("label_birthday")

        self.label_family = QtWidgets.QLabel(self.centralwidget)
        self.label_family.setGeometry(QtCore.QRect(20, 200, 290, 30))
        self.label_family.setObjectName("label_family")

        self.label_conscription = QtWidgets.QLabel(self.centralwidget)
        self.label_conscription.setGeometry(QtCore.QRect(20, 240, 290, 30))
        self.label_conscription.setObjectName("label_conscription")

        self.label_education = QtWidgets.QLabel(self.centralwidget)
        self.label_education.setGeometry(QtCore.QRect(20, 280, 290, 30))
        self.label_education.setObjectName("label_education")

        self.label_passport = QtWidgets.QLabel(self.centralwidget)
        self.label_passport.setGeometry(QtCore.QRect(350, 40, 290, 30))
        self.label_passport.setObjectName("label_passport")

        self.label_place_of_registration = QtWidgets.QLabel(self.centralwidget)
        self.label_place_of_registration.setGeometry(QtCore.QRect(350, 80, 300, 30))
        self.label_place_of_registration.setObjectName("label_place_of_registration")

        self.label_place_of_residence = QtWidgets.QLabel(self.centralwidget)
        self.label_place_of_residence.setGeometry(QtCore.QRect(350, 120, 300, 30))
        self.label_place_of_residence.setObjectName("label_place_of_residence")

        self.button_tabel = QtWidgets.QPushButton("Табель учета", self.centralwidget)
        self.button_tabel.setGeometry(QtCore.QRect(510, 50, 141, 32))
        self.button_tabel.setObjectName("button_tabel")
        self.button_tabel.clicked.connect(self.open_time_sheet_window)

        self.button_add_activity = QtWidgets.QPushButton("Добавить занятия", self.centralwidget)
        self.button_add_activity.setGeometry(QtCore.QRect(510, 10, 141, 32))
        self.button_add_activity.setObjectName("button_add_activity")
        self.button_add_activity.clicked.connect(self.open_activities_window)

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def open_time_sheet_window(self):
        user_service = User_Service()
        current_user = user_service.authorised_user
        if current_user:
            self.time_sheet_window = Time_Sheet(current_user.Login)
            self.time_sheet_window.show()
            self.close()

    def open_activities_window(self):
        from View.activities_window import Activities_Window
        self.activities_window = Activities_Window()
        self.activities_window.show()
        self.close()