# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manifest.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Gear Builder")
        MainWindow.resize(670, 647)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 621, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tb_manifest = QtWidgets.QWidget()
        self.tb_manifest.setObjectName("tb_manifest")
        self.btn_input_delete = QtWidgets.QPushButton(self.tb_manifest)
        self.btn_input_delete.setGeometry(QtCore.QRect(230, 340, 61, 32))
        self.btn_input_delete.setObjectName("btn_input_delete")
        self.label_9 = QtWidgets.QLabel(self.tb_manifest)
        self.label_9.setGeometry(QtCore.QRect(80, 320, 60, 16))
        self.label_9.setObjectName("label_9")
        self.btn_config_edit = QtWidgets.QPushButton(self.tb_manifest)
        self.btn_config_edit.setGeometry(QtCore.QRect(180, 420, 51, 32))
        self.btn_config_edit.setObjectName("btn_config_edit")
        self.txt_label = QtWidgets.QLineEdit(self.tb_manifest)
        self.txt_label.setGeometry(QtCore.QRect(70, 90, 113, 21))
        self.txt_label.setObjectName("txt_label")
        self.txt_name = QtWidgets.QLineEdit(self.tb_manifest)
        self.txt_name.setGeometry(QtCore.QRect(70, 50, 113, 21))
        self.txt_name.setObjectName("txt_name")
        self.label = QtWidgets.QLabel(self.tb_manifest)
        self.label.setGeometry(QtCore.QRect(220, 30, 81, 16))
        self.label.setObjectName("label")
        self.lblName = QtWidgets.QLabel(self.tb_manifest)
        self.lblName.setGeometry(QtCore.QRect(70, 30, 60, 16))
        self.lblName.setObjectName("lblName")
        self.rdo_analysis = QtWidgets.QRadioButton(self.tb_manifest)
        self.rdo_analysis.setGeometry(QtCore.QRect(320, 200, 100, 20))
        self.rdo_analysis.setChecked(True)
        self.rdo_analysis.setObjectName("rdo_analysis")
        self.txt_description = QtWidgets.QPlainTextEdit(self.tb_manifest)
        self.txt_description.setGeometry(QtCore.QRect(220, 50, 221, 61))
        self.txt_description.setObjectName("txt_description")
        self.txt_suite = QtWidgets.QLineEdit(self.tb_manifest)
        self.txt_suite.setGeometry(QtCore.QRect(430, 130, 125, 21))
        self.txt_suite.setObjectName("txt_suite")
        self.layoutWidget = QtWidgets.QWidget(self.tb_manifest)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 130, 78, 174))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.btn_config_add = QtWidgets.QPushButton(self.tb_manifest)
        self.btn_config_add.setGeometry(QtCore.QRect(130, 420, 51, 32))
        self.btn_config_add.setObjectName("btn_config_add")
        self.btn_config_delete = QtWidgets.QPushButton(self.tb_manifest)
        self.btn_config_delete.setGeometry(QtCore.QRect(230, 420, 61, 32))
        self.btn_config_delete.setObjectName("btn_config_delete")
        self.btn_input_add = QtWidgets.QPushButton(self.tb_manifest)
        self.btn_input_add.setGeometry(QtCore.QRect(130, 340, 51, 32))
        self.btn_input_add.setObjectName("btn_input_add")
        self.rdo_utility = QtWidgets.QRadioButton(self.tb_manifest)
        self.rdo_utility.setGeometry(QtCore.QRect(320, 180, 100, 20))
        self.rdo_utility.setObjectName("rdo_utility")
        self.btn_make_manifest_2 = QtWidgets.QPushButton(self.tb_manifest)
        self.btn_make_manifest_2.setGeometry(QtCore.QRect(200, 490, 113, 32))
        self.btn_make_manifest_2.setObjectName("btn_make_manifest_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tb_manifest)
        self.layoutWidget_2.setGeometry(QtCore.QRect(160, 130, 135, 171))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.txt_author = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txt_author.setObjectName("txt_author")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.txt_author)
        self.txt_maintainer = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txt_maintainer.setObjectName("txt_maintainer")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.txt_maintainer)
        self.txt_license = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txt_license.setObjectName("txt_license")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.txt_license)
        self.txt_url = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txt_url.setObjectName("txt_url")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.txt_url)
        self.txt_source = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txt_source.setObjectName("txt_source")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.txt_source)
        self.txt_cite = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txt_cite.setObjectName("txt_cite")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.txt_cite)
        self.txt_version = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txt_version.setObjectName("txt_version")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.txt_version)
        self.btn_input_edit = QtWidgets.QPushButton(self.tb_manifest)
        self.btn_input_edit.setGeometry(QtCore.QRect(180, 340, 51, 32))
        self.btn_input_edit.setObjectName("btn_input_edit")
        self.cmbo_inputs = QtWidgets.QComboBox(self.tb_manifest)
        self.cmbo_inputs.setGeometry(QtCore.QRect(130, 320, 171, 26))
        self.cmbo_inputs.setObjectName("cmbo_inputs")
        self.chk_flywheel = QtWidgets.QCheckBox(self.tb_manifest)
        self.chk_flywheel.setGeometry(QtCore.QRect(320, 130, 111, 20))
        self.chk_flywheel.setObjectName("chk_flywheel")
        self.btn_make_manifest = QtWidgets.QPushButton(self.tb_manifest)
        self.btn_make_manifest.setGeometry(QtCore.QRect(90, 490, 113, 32))
        self.btn_make_manifest.setObjectName("btn_make_manifest")
        self.cmbo_config = QtWidgets.QComboBox(self.tb_manifest)
        self.cmbo_config.setGeometry(QtCore.QRect(130, 400, 171, 26))
        self.cmbo_config.setObjectName("cmbo_config")
        self.lblLabel = QtWidgets.QLabel(self.tb_manifest)
        self.lblLabel.setGeometry(QtCore.QRect(70, 70, 60, 16))
        self.lblLabel.setObjectName("lblLabel")
        self.label_10 = QtWidgets.QLabel(self.tb_manifest)
        self.label_10.setGeometry(QtCore.QRect(80, 400, 60, 16))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tb_manifest, "")
        self.tb_dockerfile = QtWidgets.QWidget()
        self.tb_dockerfile.setObjectName("tb_dockerfile")
        self.label_11 = QtWidgets.QLabel(self.tb_dockerfile)
        self.label_11.setGeometry(QtCore.QRect(160, 20, 181, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tb_dockerfile)
        self.label_12.setGeometry(QtCore.QRect(160, 60, 201, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tb_dockerfile)
        self.label_13.setGeometry(QtCore.QRect(160, 100, 201, 16))
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.tb_dockerfile, "")
        self.scripts = QtWidgets.QWidget()
        self.scripts.setObjectName("scripts")
        self.label_14 = QtWidgets.QLabel(self.scripts)
        self.label_14.setGeometry(QtCore.QRect(40, 20, 451, 391))
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.scripts, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gear Builder"))
        self.btn_input_delete.setText(_translate("MainWindow", "Delete"))
        self.label_9.setText(_translate("MainWindow", "inputs:"))
        self.btn_config_edit.setText(_translate("MainWindow", "Edit"))
        self.txt_label.setText(_translate("MainWindow", "Test Gear"))
        self.txt_name.setText(_translate("MainWindow", "test-gear"))
        self.label.setText(_translate("MainWindow", "Description:"))
        self.lblName.setText(_translate("MainWindow", "name:"))
        self.rdo_analysis.setText(_translate("MainWindow", "Analysis"))
        self.txt_description.setPlainText(_translate("MainWindow", "This is a Test Gear. Use with caution."))
        self.txt_suite.setText(_translate("MainWindow", "One Suite World"))
        self.label_2.setText(_translate("MainWindow", "Author:"))
        self.label_3.setText(_translate("MainWindow", "maintainer:"))
        self.label_4.setText(_translate("MainWindow", "License:"))
        self.label_5.setText(_translate("MainWindow", "url:"))
        self.label_6.setText(_translate("MainWindow", "source:"))
        self.label_7.setText(_translate("MainWindow", "cite:"))
        self.label_8.setText(_translate("MainWindow", "version:"))
        self.btn_config_add.setText(_translate("MainWindow", "Add"))
        self.btn_config_delete.setText(_translate("MainWindow", "Delete"))
        self.btn_input_add.setText(_translate("MainWindow", "Add"))
        self.rdo_utility.setText(_translate("MainWindow", "Utility"))
        self.btn_make_manifest_2.setText(_translate("MainWindow", "load manifest"))
        self.txt_author.setText(_translate("MainWindow", "Flywheel"))
        self.txt_maintainer.setText(_translate("MainWindow", "Flywheel <support@flywheel.io>"))
        self.txt_license.setText(_translate("MainWindow", "Other"))
        self.txt_url.setText(_translate("MainWindow", "https://github.com/flywheel-apps/test-gear"))
        self.txt_version.setText(_translate("MainWindow", "0.0.1"))
        self.btn_input_edit.setText(_translate("MainWindow", "Edit"))
        self.chk_flywheel.setText(_translate("MainWindow", "flywheel suite"))
        self.btn_make_manifest.setText(_translate("MainWindow", "save manifest"))
        self.lblLabel.setText(_translate("MainWindow", "label:"))
        self.label_10.setText(_translate("MainWindow", "config:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tb_manifest), _translate("MainWindow", "Manifest"))
        self.label_11.setText(_translate("MainWindow", "Select Source Image:"))
        self.label_12.setText(_translate("MainWindow", "Indicate apt-get dependencies:"))
        self.label_13.setText(_translate("MainWindow", "Indicate python dependencies:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tb_dockerfile), _translate("MainWindow", "Dockerfile"))
        self.label_14.setText(_translate("MainWindow", "Provide the base run.py and utils package.\n"
"Creating build/validate/execute functional modules around specific command-line programs.\n"
"Add a command-line \"switch-detector\" to populate the manifest config with values to loop through.\n"
"Provide a library of code-blocks that facilitate certain functionality\n"
"module-based log reporting\n"
"bids functionality\n"
"verbose config validation against manifest\n"
"compress working directory to a file in output\n"
"notify on pep8 violations(??)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scripts), _translate("MainWindow", "Script Management"))
