# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlg_config(object):
    def setupUi(self, dlg_config):
        dlg_config.setObjectName("dlg_config")
        dlg_config.resize(293, 331)
        self.buttonBox = QtWidgets.QDialogButtonBox(dlg_config)
        self.buttonBox.setGeometry(QtCore.QRect(50, 290, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.btn_add = QtWidgets.QPushButton(dlg_config)
        self.btn_add.setGeometry(QtCore.QRect(240, 200, 51, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        self.btn_add.setObjectName("btn_add")
        self.btn_edit = QtWidgets.QPushButton(dlg_config)
        self.btn_edit.setGeometry(QtCore.QRect(240, 225, 51, 32))
        self.btn_edit.setObjectName("btn_edit")
        self.btn_del = QtWidgets.QPushButton(dlg_config)
        self.btn_del.setGeometry(QtCore.QRect(240, 250, 51, 32))
        self.btn_del.setObjectName("btn_del")
        self.formLayoutWidget = QtWidgets.QWidget(dlg_config)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 221, 277))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txt_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_name.setObjectName("txt_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_name)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txt_description = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_description.setObjectName("txt_description")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_description)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.cbo_type = QtWidgets.QComboBox(self.formLayoutWidget)
        self.cbo_type.setObjectName("cbo_type")
        self.cbo_type.addItem("")
        self.cbo_type.addItem("")
        self.cbo_type.addItem("")
        self.cbo_type.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cbo_type)
        self.lblDefault_bool = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblDefault_bool.setObjectName("lblDefault_bool")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblDefault_bool)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.ck_optional = QtWidgets.QCheckBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ck_optional.sizePolicy().hasHeightForWidth())
        self.ck_optional.setSizePolicy(sizePolicy)
        self.ck_optional.setText("")
        self.ck_optional.setObjectName("ck_optional")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.ck_optional)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lst_enum = QtWidgets.QListWidget(self.formLayoutWidget)
        self.lst_enum.setObjectName("lst_enum")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lst_enum)
        self.txt_default = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_default.setObjectName("txt_default")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_default)
        self.lblDefault_txt = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblDefault_txt.setObjectName("lblDefault_txt")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblDefault_txt)
        self.ck_default = QtWidgets.QCheckBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ck_default.sizePolicy().hasHeightForWidth())
        self.ck_default.setSizePolicy(sizePolicy)
        self.ck_default.setText("")
        self.ck_default.setChecked(False)
        self.ck_default.setObjectName("ck_default")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ck_default)

        self.retranslateUi(dlg_config)
        self.buttonBox.accepted.connect(dlg_config.accept)
        self.buttonBox.rejected.connect(dlg_config.reject)
        QtCore.QMetaObject.connectSlotsByName(dlg_config)
        dlg_config.setTabOrder(self.lst_enum, self.btn_add)
        dlg_config.setTabOrder(self.btn_add, self.btn_edit)
        dlg_config.setTabOrder(self.btn_edit, self.btn_del)

    def retranslateUi(self, dlg_config):
        _translate = QtCore.QCoreApplication.translate
        dlg_config.setWindowTitle(_translate("dlg_config", "Add or Edit Configs"))
        self.btn_add.setText(_translate("dlg_config", "Add"))
        self.btn_edit.setText(_translate("dlg_config", "Edit"))
        self.btn_del.setText(_translate("dlg_config", "Del"))
        self.label.setText(_translate("dlg_config", "name:"))
        self.label_2.setText(_translate("dlg_config", "description:"))
        self.label_3.setText(_translate("dlg_config", "type:"))
        self.cbo_type.setItemText(0, _translate("dlg_config", "string"))
        self.cbo_type.setItemText(1, _translate("dlg_config", "number"))
        self.cbo_type.setItemText(2, _translate("dlg_config", "integer"))
        self.cbo_type.setItemText(3, _translate("dlg_config", "boolean"))
        self.lblDefault_bool.setText(_translate("dlg_config", "default:"))
        self.label_6.setText(_translate("dlg_config", "optional:"))
        self.label_4.setText(_translate("dlg_config", "enum:"))
        self.lblDefault_txt.setText(_translate("dlg_config", "default:"))
