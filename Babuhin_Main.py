from PyQt5 import QtCore, QtGui, QtWidgets
from interfase import *
import sys
import pandas as pd
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from calculation import *
from Vision import *


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 981, 1171))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName("tabWidget")
        self.construction_CN = QtWidgets.QWidget()
        self.construction_CN.setObjectName("construction_CN")



        ### XS ##########################################################################################################################################################
        self.box_XS = QtWidgets.QGroupBox(self.construction_CN)
        self.box_XS.setGeometry(QtCore.QRect(110, 0, 681, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.box_XS.setFont(font)
        self.box_XS.setObjectName("box_XS")
        self.table_XS = NewTableWidget(self.box_XS)
        self.table_XS.setGeometry(QtCore.QRect(15, 25, 591, 171))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.table_XS.setFont(font)
        self.table_XS.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_XS.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_XS.setAlternatingRowColors(False)
        self.table_XS.setWordWrap(True)
        self.table_XS.setRowCount(0)
        self.table_XS.setObjectName("table_XS")
        self.table_XS.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(195, 183, 200))
        self.table_XS.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(195, 183, 200))
        self.table_XS.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_XS.horizontalHeader().setStyleSheet("::section{Background-color:rgb(195, 183, 200)}")
        self.table_XS.setHorizontalHeaderItem(2, item)
        self.table_XS.horizontalHeader().setCascadingSectionResizes(True)
        self.table_XS.horizontalHeader().setSortIndicatorShown(False)
        self.table_XS.horizontalHeader().setStretchLastSection(True)
        self.table_XS.verticalHeader().setCascadingSectionResizes(True)
        self.table_XS.verticalHeader().setStretchLastSection(False)
        self.add_XS = QtWidgets.QPushButton(self.box_XS)
        self.add_XS.setGeometry(QtCore.QRect(620, 60, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.add_XS.setFont(font)
        self.add_XS.setObjectName("add_XS")
        self.delete_XS = QtWidgets.QPushButton(self.box_XS)
        self.delete_XS.setGeometry(QtCore.QRect(620, 130, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.delete_XS.setFont(font)
        self.delete_XS.setObjectName("delete_XS")



        ### QR2 ##########################################################################################################################################################
        self.box_QR_2 = QtWidgets.QGroupBox(self.construction_CN)
        self.box_QR_2.setGeometry(QtCore.QRect(110, 230, 681, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.box_QR_2.setFont(font)
        self.box_QR_2.setObjectName("box_QR_2")
        self.delete_QR_2 = QtWidgets.QPushButton(self.box_QR_2)
        self.delete_QR_2.setGeometry(QtCore.QRect(620, 130, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.delete_QR_2.setFont(font)
        self.delete_QR_2.setObjectName("delete_QR_2")
        self.add_QR_2 = QtWidgets.QPushButton(self.box_QR_2)
        self.add_QR_2.setGeometry(QtCore.QRect(620, 60, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.add_QR_2.setFont(font)
        self.add_QR_2.setObjectName("add_QR_2")
        self.table_QR_2 = NewTableWidget(self.box_QR_2)
        self.table_QR_2.setGeometry(QtCore.QRect(15, 25, 591, 171))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.table_QR_2.setFont(font)
        self.table_QR_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_QR_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_QR_2.setAlternatingRowColors(False)
        self.table_QR_2.setWordWrap(True)
        self.table_QR_2.setRowCount(0)
        self.table_QR_2.setObjectName("table_QR_2")
        self.table_QR_2.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(195, 183, 200))
        self.table_QR_2.horizontalHeader().setStyleSheet("::section{Background-color:rgb(195, 183, 200)}")
        self.table_QR_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(195, 183, 200))
        self.table_QR_2.setHorizontalHeaderItem(1, item)
        self.table_QR_2.horizontalHeader().setCascadingSectionResizes(True)
        self.table_QR_2.horizontalHeader().setSortIndicatorShown(False)
        self.table_QR_2.horizontalHeader().setStretchLastSection(True)
        self.table_QR_2.verticalHeader().setCascadingSectionResizes(True)
        self.table_QR_2.verticalHeader().setStretchLastSection(False)

        self.right_support_2 = QtWidgets.QCheckBox(self.box_QR_2)
        self.right_support_2.setGeometry(QtCore.QRect(380, 190, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.right_support_2.setFont(font)
        self.right_support_2.setObjectName("right_support_2")
        self.left_support_2 = QtWidgets.QCheckBox(self.box_QR_2)
        self.left_support_2.setGeometry(QtCore.QRect(70, 190, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.left_support_2.setFont(font)
        self.left_support_2.setObjectName("left_support_2")




        ### XC ##########################################################################################################################################################
        self.box_XC = QtWidgets.QGroupBox(self.construction_CN)
        self.box_XC.setGeometry(QtCore.QRect(110, 460, 681, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.box_XC.setFont(font)
        self.box_XC.setObjectName("box_XC")
        self.table_XC = NewTableWidget(self.box_XC)
        self.table_XC.setGeometry(QtCore.QRect(15, 25, 591, 171))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.table_XC.setFont(font)
        self.table_XC.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_XC.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_XC.setAlternatingRowColors(False)
        self.table_XC.setWordWrap(True)
        self.table_XC.setRowCount(0)
        self.table_XC.setObjectName("table_XC")
        self.table_XC.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(195, 183, 200))
        self.table_XC.setHorizontalHeaderItem(0, item)
        self.table_XC.horizontalHeader().setStyleSheet("::section{Background-color:rgb(195, 183, 200)}")
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(195, 183, 200))
        self.table_XC.setHorizontalHeaderItem(1, item)
        self.table_XC.horizontalHeader().setCascadingSectionResizes(True)
        self.table_XC.horizontalHeader().setSortIndicatorShown(False)
        self.table_XC.horizontalHeader().setStretchLastSection(True)
        self.table_XC.verticalHeader().setCascadingSectionResizes(True)
        self.table_XC.verticalHeader().setStretchLastSection(False)
        self.add_XC = QtWidgets.QPushButton(self.box_XC)
        self.add_XC.setGeometry(QtCore.QRect(620, 60, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.add_XC.setFont(font)
        self.add_XC.setObjectName("add_XC")
        self.delete_XC = QtWidgets.QPushButton(self.box_XC)
        self.delete_XC.setGeometry(QtCore.QRect(620, 130, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.delete_XC.setFont(font)
        self.delete_XC.setObjectName("delete_XC")



        ### QS #######################################################################################################################################################
        self.box_QS_2 = QtWidgets.QGroupBox(self.construction_CN)
        self.box_QS_2.setGeometry(QtCore.QRect(110, 690, 681, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.box_QS_2.setFont(font)
        self.box_QS_2.setObjectName("box_QS_2")
        self.table_QS_2 = NewTableWidget(self.box_QS_2)
        self.table_QS_2.setGeometry(QtCore.QRect(15, 25, 591, 171))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.table_QS_2.setFont(font)
        self.table_QS_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_QS_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_QS_2.setAlternatingRowColors(False)
        self.table_QS_2.setWordWrap(True)
        self.table_QS_2.setRowCount(0)
        self.table_QS_2.setObjectName("table_QS_2")
        self.table_QS_2.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(195, 183, 200))
        self.table_QS_2.horizontalHeader().setStyleSheet("::section{Background-color:rgb(195, 183, 200)}")
        self.table_QS_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(195, 183, 200))
        self.table_QS_2.setHorizontalHeaderItem(1, item)
        self.table_QS_2.horizontalHeader().setCascadingSectionResizes(True)
        self.table_QS_2.horizontalHeader().setSortIndicatorShown(False)
        self.table_QS_2.horizontalHeader().setStretchLastSection(True)
        self.table_QS_2.verticalHeader().setCascadingSectionResizes(True)
        self.table_QS_2.verticalHeader().setStretchLastSection(False)
        self.add_QS_2 = QtWidgets.QPushButton(self.box_QS_2)
        self.add_QS_2.setGeometry(QtCore.QRect(620, 60, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.add_QS_2.setFont(font)
        self.add_QS_2.setObjectName("add_QS_2")
        self.delete_QS_2 = QtWidgets.QPushButton(self.box_QS_2)
        self.delete_QS_2.setGeometry(QtCore.QRect(620, 130, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.delete_QS_2.setFont(font)
        self.delete_QS_2.setObjectName("delete_QS_2")
        self.tabWidget.addTab(self.construction_CN, "")





#############################################################################################################################################################################
        self.drawing = QtWidgets.QWidget()
        self.drawing.setObjectName("drawing")
        self.draw_button = QtWidgets.QPushButton(self.drawing)
        self.draw_button.setGeometry(QtCore.QRect(20, 20, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.draw_button.setFont(font)
        self.draw_button.setObjectName("draw_button")
        self.drawing_canvas = MyGraphicsView(self.drawing)
        self.drawing_canvas.setGeometry(QtCore.QRect(30, 100, 1000, 680))
        self.drawing_canvas.setObjectName("drawing_canvas")
        self.post_graphs = QtWidgets.QGroupBox(self.drawing)
        self.post_graphs.setGeometry(QtCore.QRect(0, 630, 971, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.post_graphs.setFont(font)
        self.post_graphs.setObjectName("post_graphs")
        self.graph_NX = QtWidgets.QPushButton(self.post_graphs)
        self.graph_NX.setGeometry(QtCore.QRect(10, 40, 301, 81))
        self.graph_NX.setObjectName("graph_NX")


        self.graph_sigma = QtWidgets.QPushButton(self.post_graphs)
        self.graph_sigma.setGeometry(QtCore.QRect(320, 40, 301, 81))
        self.graph_sigma.setObjectName("graph_sigma")
        self.graph_UX = QtWidgets.QPushButton(self.post_graphs)
        self.graph_UX.setGeometry(QtCore.QRect(630, 40, 301, 81))
        self.graph_UX.setObjectName("graph_UX")
        self.tabWidget.addTab(self.drawing, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.post_tables = QtWidgets.QGroupBox(self.tab)
        self.post_tables.setGeometry(QtCore.QRect(0, 0, 981, 771))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.post_tables.setFont(font)
        self.post_tables.setTitle("")
        self.post_tables.setObjectName("post_tables")
        self.table_NX = QtWidgets.QPushButton(self.post_tables)
        self.table_NX.setGeometry(QtCore.QRect(220, 80, 521, 81))
        self.table_NX.setObjectName("table_NX")
        self.table_sigma = QtWidgets.QPushButton(self.post_tables)
        self.table_sigma.setGeometry(QtCore.QRect(220, 210, 521, 81))
        self.table_sigma.setObjectName("table_sigma")
        self.table_UX = QtWidgets.QPushButton(self.post_tables)
        self.table_UX.setGeometry(QtCore.QRect(220, 370, 521, 81))
        self.table_UX.setObjectName("table_UX")
        self.table_all = QtWidgets.QPushButton(self.post_tables)
        self.table_all.setGeometry(QtCore.QRect(220, 530, 521, 81))
        self.table_all.setObjectName("table_all")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.create_button = QtWidgets.QAction(MainWindow)
        self.create_button.setObjectName("create_button")
        self.open_button = QtWidgets.QAction(MainWindow)
        self.open_button.setObjectName("open_button")
        self.save_button = QtWidgets.QAction(MainWindow)
        self.save_button.setObjectName("save_button")
        self.menu.addAction(self.save_button)
        self.menu.addAction(self.create_button)
        self.menu.addAction(self.open_button)
        self.menubar.addAction(self.menu.menuAction())

        self.save_button.triggered.connect(lambda: self.write_settings(MainWindow))
        self.open_button.triggered.connect(lambda: self.read_settings(MainWindow))
        self.create_button.triggered.connect(lambda: self.new_settings(MainWindow))

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.add_XC.clicked.connect(self.table_XC._addRow)
        self.delete_XC.clicked.connect(self.table_XC._removeRow)

        self.add_XS.clicked.connect(self.table_XS._addRow)
        self.delete_XS.clicked.connect(self.table_XS._removeRow)

        self.add_QR_2.clicked.connect(self.table_QR_2._addRow)
        self.delete_QR_2.clicked.connect(self.table_QR_2._removeRow)

        self.add_QS_2.clicked.connect(self.table_QS_2._addRow)
        self.delete_QS_2.clicked.connect(self.table_QS_2._removeRow)

        self.draw_button.clicked.connect(self.makeDraw)
        self.table_NX.clicked.connect(lambda: self.makeDraw())
        self.table_NX.clicked.connect(lambda: self.tableN(
            calculateNx(self.drawing_canvas.new_bars, self.drawing_canvas.F, self.drawing_canvas.left_sealing,
                        self.drawing_canvas.right_sealing), self.drawing_canvas.new_bars))

        self.table_sigma.clicked.connect(lambda: self.makeDraw())
        self.table_sigma.clicked.connect(lambda: self.tableSigma(
            calculateNx(self.drawing_canvas.new_bars, self.drawing_canvas.F, self.drawing_canvas.left_sealing,
                        self.drawing_canvas.right_sealing), self.drawing_canvas.new_bars))

        self.table_UX.clicked.connect(lambda: self.makeDraw())
        self.table_UX.clicked.connect(lambda: self.tableU(
            calculateUx(self.drawing_canvas.new_bars, self.drawing_canvas.F, self.drawing_canvas.left_sealing,
                        self.drawing_canvas.right_sealing), self.drawing_canvas.new_bars))

        self.table_all.clicked.connect(lambda: self.makeDraw())
        self.table_all.clicked.connect(lambda: self.make_all(
            calculateNx(self.drawing_canvas.new_bars, self.drawing_canvas.F, self.drawing_canvas.left_sealing,
                        self.drawing_canvas.right_sealing),
            calculateUx(self.drawing_canvas.new_bars, self.drawing_canvas.F, self.drawing_canvas.left_sealing,
                        self.drawing_canvas.right_sealing), self.drawing_canvas.new_bars, MainWindow))

        self.graph_NX.clicked.connect(lambda: self.makeDraw())
        self.graph_NX.clicked.connect(lambda: self.graphicNx(
            calculateNx(self.drawing_canvas.new_bars, self.drawing_canvas.F, self.drawing_canvas.left_sealing,
                        self.drawing_canvas.right_sealing), self.drawing_canvas.new_bars))

        self.graph_sigma.clicked.connect(lambda: self.makeDraw())
        self.graph_sigma.clicked.connect(lambda: self.graphicSigma(
            calculateNx(self.drawing_canvas.new_bars, self.drawing_canvas.F, self.drawing_canvas.left_sealing,
                        self.drawing_canvas.right_sealing), self.drawing_canvas.new_bars))

        self.graph_UX.clicked.connect(lambda: self.makeDraw())
        self.graph_UX.clicked.connect(lambda: self.graphicUx(
            calculateUx(self.drawing_canvas.new_bars, self.drawing_canvas.F, self.drawing_canvas.left_sealing,
                        self.drawing_canvas.right_sealing), self.drawing_canvas.new_bars))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clean(self, widget):
        if isinstance(widget, QtWidgets.QTableWidget):
            widget.setRowCount(0)
        if isinstance(widget, QtWidgets.QCheckBox):
            widget.setChecked(False)

    def save_data_as_csv(self, df, MainWindow):
        name = QFileDialog.getSaveFileName(MainWindow, 'Save File', filter='*.csv')
        df.to_csv(name[0], index=False)

    def write_settings(self, MainWindow):
        path = QFileDialog.getSaveFileName(MainWindow, 'Save File', '', 'INI(*.ini)')
        settings = QSettings(path[0], QSettings.IniFormat)
        if path[0] != "" and path[1] != "":
            for children in MainWindow.findChildren(QtWidgets.QWidget):
                if children.objectName():
                    self.write(children, settings)
            settings.sync()

    def read_settings(self, MainWindow):
        path = QFileDialog.getOpenFileName(MainWindow, 'Open File', '', 'INI(*.ini)')
        settings = QSettings(path[0], QSettings.IniFormat)
        if path[0] != "" and path[1] != "":
            for children in MainWindow.findChildren(QtWidgets.QWidget):
                if children.objectName():
                    self.read(children, settings)

    def new_settings(self, MainWindow):
        for children in MainWindow.findChildren(QtWidgets.QWidget):
            if children.objectName():
                self.clean(children)
        self.drawing_canvas.bars = []
        self.drawing_canvas.F = []
        self.drawing_canvas.qxs = []
        self.drawing_canvas.left_sealing = False
        self.drawing_canvas.right_sealing = False
        self.drawing_canvas.update()

    def write(self, widget, settings):
        settings.beginGroup(widget.objectName())
        if isinstance(widget, QtWidgets.QTableWidget):
            settings.setValue("rowCount", widget.rowCount())
            settings.setValue("columnCount", widget.columnCount())
            items = QtCore.QByteArray()
            stream = QtCore.QDataStream(items, QtCore.QIODevice.WriteOnly)
            for i in range(widget.rowCount()):
                for j in range(widget.columnCount()):
                    it = widget.item(i, j)
                    if it is not None:
                        stream.writeInt(i)
                        stream.writeInt(j)
                        stream << it
            settings.setValue("items", items)
        if isinstance(widget, QtWidgets.QCheckBox):
            settings.setValue("isChecked", widget.isChecked())
        settings.endGroup()

    def read(self, widget, settings):
        settings.beginGroup(widget.objectName())
        if isinstance(widget, QtWidgets.QTableWidget):
            rowCount = settings.value("rowCount", type=int)
            columnCount = settings.value("columnCount", type=int)
            widget.setRowCount(rowCount)
            widget.setColumnCount(columnCount)
            items = settings.value("items")
            stream = QtCore.QDataStream(items, QtCore.QIODevice.ReadOnly)
            while not stream.atEnd():
                it = QtWidgets.QTableWidgetItem()
                i = stream.readInt()
                j = stream.readInt()
                stream >> it
                widget.setItem(i, j, it)
        if isinstance(widget, QtWidgets.QCheckBox):
            boolCheck = settings.value("isChecked", type=bool)
            widget.setChecked(boolCheck)
        settings.endGroup()
    def scale_make(self):
        x_max = 0
        y_max = 0
        for kern in self.drawing_canvas.bars:
            if kern != None:
                if kern.area > y_max:
                    y_max = kern.area
                x_max += kern.length
        scale_x = 531 / x_max if x_max != 0 else 1
        scale_y = 150 / y_max if y_max != 0 else 1
        self.drawing_canvas.scale_x = scale_x
        self.drawing_canvas.scale_y = scale_y
        return scale_x, scale_y

    def makeDraw(self):

        try:
            self.drawing_canvas.left_sealing = self.left_support_2.isChecked()
            self.drawing_canvas.right_sealing = self.right_support_2.isChecked()


            if (self.drawing_canvas.left_sealing == False) and (self.drawing_canvas.right_sealing == False):
                raise "НЕ МОЖЕТ БЫТЬ 0 СТЕРЖНЕЙ"


            bars = []
            for i in range(self.table_XS.rowCount()):
                bar = BarItem()
                bar.length = int(self.table_XS.item(i, 0).text())
                bar.area = int(self.table_XS.item(i, 1).text())
                bars.append(bar)
            self.drawing_canvas.bars = bars
            self.scale_make()
            powers = []
            for i in range(self.table_QR_2.rowCount()):
                power = PowerItem()
                power.point = int(self.table_QR_2.item(i, 0).text())
                power.power = int(self.table_QR_2.item(i, 1).text())
                powers.append(power)
            self.drawing_canvas.F = powers

            qxs = []
            for i in range(self.table_QS_2.rowCount()):
                qx = QxItem()
                qx.bar = int(self.table_QS_2.item(i, 0).text())
                qx.power = int(self.table_QS_2.item(i, 1).text())
                qxs.append(qx)
            self.drawing_canvas.qxs = qxs

            self.drawing_canvas.new_bars = self.make_new_bars()
            self.drawing_canvas.update()
        except:
            pass

    def make_new_bars(self):
        bars1 = []
        for i in range(self.table_XS.rowCount()):
            bar1 = BarItem()
            material = int(self.table_XS.item(i, 2).text())
            bar1.L = float(self.table_XS.item(i, 0).text())
            bar1.A = float(self.table_XS.item(i, 1).text())
            bar1.E = float(self.table_XC.item(material - 1, 0).text())
            bars1.append(bar1)


            print(f'{float(self.table_XS.item(i, 1).text())=}')



        for item in self.drawing_canvas.qxs:
            if item != None and item.bar != 0 and item.bar != None:
                bars1[int(item.bar) - 1].Q = item.power

        return bars1





    def tableN(self, N, kernels):
        try:
            fig, ax = plt.subplots()

            fig.patch.set_visible(False)
            ax.axis('off')
            ax.axis('tight')

            sumL = 0
            totable = []
            for i in range(len(kernels)):
                x = np.linspace(0, kernels[i].L, 8)
                for _x in x:
                    totable.append([round(_x + sumL, 2), round(N[i][0] + _x * N[i][1], 2)])
                sumL += kernels[i].L
            df = pd.DataFrame(totable,
                              columns=['L (длина)', 'Nx'])

            table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center',
                             bbox=[0, 0, 1, 1])
            table.scale(1, 2)

            fig.tight_layout()
            plt.show()
        except:
            pass

    def tableSigma(self, N, kernels):
        try:
            fig, ax = plt.subplots()

            fig.patch.set_visible(False)
            ax.axis('off')
            ax.axis('tight')

            sumL = 0
            totable = []
            for i in range(len(kernels)):
                x = np.linspace(0, kernels[i].L, 8)
                for _x in x:
                    totable.append([round(_x + sumL, 2), round((N[i][0] + _x * N[i][1]) / kernels[i].A, 2)])
                sumL += kernels[i].L
            df = pd.DataFrame(totable,
                              columns=['L (длина)', 'σ'])

            table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center',
                             bbox=[0, 0, 1, 1])
            table.scale(1, 2)

            fig.tight_layout()
            plt.show()
        except:
            pass

    def tableU(self, U, kernels):
        try:
            fig, ax = plt.subplots()

            fig.patch.set_visible(False)
            ax.axis('off')
            ax.axis('tight')

            sumL = 0
            totable = []
            for i in range(len(kernels)):
                x = np.linspace(0, kernels[i].L, 8)
                for _x in x:
                    totable.append([round(_x + sumL, 2), round(U[i][0] + _x * U[i][1] + (_x ** 2) * U[i][2], 2)])
                sumL += kernels[i].L
            df = pd.DataFrame(totable,
                              columns=['L (длина)', 'Ux'])

            table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center',
                             bbox=[0, 0, 1, 1])
            table.scale(1, 2)

            fig.tight_layout()
            plt.show()
        except:
            pass

    def graphicNx(self, N, kernels):
        try:
            sumL = 0
            for kern in kernels:
                sumL += kern.L
            y = []
            for i in range(len(kernels)):
                x = np.linspace(0, kernels[i].L, int(round(500 * kernels[i].L / sumL)))
                y += [N[i][0] + _x * N[i][1] for _x in x]
            x1 = np.linspace(0, sumL, len(y))
            plt.title("N(X)")
            plt.xlabel("L")
            plt.ylabel("N(x)")
            plt.grid()
            plt.plot(x1, y, 'r-')
            plt.show()
        except:
            pass

    def graphicUx(self, U, kernels):
        try:
            sumL = 0
            for kern in kernels:
                sumL += kern.L
            y = []
            for i in range(len(kernels)):
                x = np.linspace(0, kernels[i].L, int(round(500 * kernels[i].L / sumL)))
                y += [U[i][0] + _x * U[i][1] + (_x ** 2) * U[i][2] for _x in x]
            x1 = np.linspace(0, sumL, len(y))
            plt.title("U(X)")
            plt.xlabel("L")
            plt.ylabel("U(x)")
            plt.grid()
            plt.plot(x1, y, 'r-')
            plt.show()
        except:
            pass

    def graphicSigma(self, N, kernels):
            sumL = 0
            for kern in kernels:
                sumL += kern.L
            y = []
            for i in range(len(kernels)):
                x = np.linspace(0, kernels[i].L, int(round(500 * kernels[i].L / sumL)))

                y += [(N[i][0] + _x * N[i][1]) / float(self.table_XS.item(i, 1).text()) for _x in x]

                print(kernels[i].A)
                print(float(self.table_XS.item(i, 1).text()))


            x1 = np.linspace(0, sumL, len(y))
            plt.title("σ(X)")
            plt.xlabel("L")
            plt.ylabel("σ")
            plt.grid()
            plt.plot(x1, y, 'r-')
            plt.show()

    def make_all(self, N, U, kernels, MainWindow):
        try:
            sumL = 0
            totable = []
            for i in range(len(kernels)):
                x = np.linspace(0, kernels[i].L, 8)
                for _x in x:
                    totable.append([round(_x + sumL, 2), round(N[i][0] + _x * N[i][1], 2)])
                sumL += kernels[i].L
            df = pd.DataFrame(totable,
                              columns=['L', 'Nx'])

            sumL = 0
            totable = []
            for i in range(len(kernels)):
                x = np.linspace(0, kernels[i].L, 8)
                for _x in x:
                    totable.append([round((N[i][0] + _x * N[i][1]) / kernels[i].A, 2)])
                sumL += kernels[i].L
            df1 = pd.DataFrame(totable,
                               columns=['q'])

            sumL = 0
            totable = []
            for i in range(len(kernels)):
                x = np.linspace(0, kernels[i].L, 8)
                for _x in x:
                    totable.append([round(U[i][0] + _x * U[i][1] + (_x ** 2) * U[i][2], 2)])
                sumL += kernels[i].L
            df2 = pd.DataFrame(totable,
                               columns=['Ux'])

            frames = [df, df1, df2]
            result = pd.concat(frames, axis=1)
            self.save_data_as_csv(result, MainWindow)
        except:
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Babunih"))
        self.box_XC.setTitle(_translate("MainWindow", "Основные характеристики стержней (XC)"))
        item = self.table_XC.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Модуль упругости (Ei)"))
        item = self.table_XC.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Допускаемое напряжение (σi)"))
        self.add_XC.setText(_translate("MainWindow", "+"))
        self.delete_XC.setText(_translate("MainWindow", "-"))
        self.box_XS.setTitle(_translate("MainWindow", "Создание стержней (XS)"))
        item = self.table_XS.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Длина (Li)"))
        item = self.table_XS.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Площадь п. сеч. (Ai)"))
        item = self.table_XS.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Свойства (XC)"))
        self.add_XS.setText(_translate("MainWindow", "+"))
        self.delete_XS.setText(_translate("MainWindow", "-"))
        self.box_QR_2.setTitle(_translate("MainWindow", "Нагрузки на узлы (QR)"))
        self.delete_QR_2.setText(_translate("MainWindow", "-"))
        self.add_QR_2.setText(_translate("MainWindow", "+"))
        item = self.table_QR_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Узел №"))
        item = self.table_QR_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Нагрузка F"))
        self.right_support_2.setText(_translate("MainWindow", "Опора в правой части"))
        self.left_support_2.setText(_translate("MainWindow", "Опора в левой части"))
        self.box_QS_2.setTitle(_translate("MainWindow", "Нагрузки на стержни (QS)"))
        item = self.table_QS_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Стержень №"))
        item = self.table_QS_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Нагрузка qx"))
        self.add_QS_2.setText(_translate("MainWindow", "+"))
        self.delete_QS_2.setText(_translate("MainWindow", "-"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.construction_CN), _translate("MainWindow", "Препроцессор"))
        self.draw_button.setText(_translate("MainWindow", "¯\_(ツ)_/¯"))
        self.post_graphs.setTitle(_translate("MainWindow", "Графики постпроцессора"))
        self.graph_NX.setText(_translate("MainWindow", "Продольные силы"))
        self.graph_sigma.setText(_translate("MainWindow", "Нормальные напряжения"))
        self.graph_UX.setText(_translate("MainWindow", "Перемещения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.drawing), _translate("MainWindow", "Изображение"))
        self.table_NX.setText(_translate("MainWindow", "Продольные силы"))
        self.table_sigma.setText(_translate("MainWindow", "Нормальные напряжения"))
        self.table_UX.setText(_translate("MainWindow", "Перемещения"))
        self.table_all.setText(_translate("MainWindow", "Все данные"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Таблицы постпроцессора"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.create_button.setText(_translate("MainWindow", "Создать"))
        self.create_button.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.open_button.setText(_translate("MainWindow", "Открыть"))
        self.open_button.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.save_button.setText(_translate("MainWindow", "Сохранить"))
        self.save_button.setShortcut(_translate("MainWindow", "Ctrl+S"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
