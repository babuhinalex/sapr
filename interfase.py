from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class AlignDelegate(QItemDelegate):
    def paint(self, painter, option, index):
        option.displayAlignment = Qt.AlignCenter
        QItemDelegate.paint(self, painter, option, index)


class NewTableWidget(QTableWidget):
    def __init__(self, QGroupBox):
        super().__init__(QGroupBox)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setItemDelegate(AlignDelegate())


    def from_df(self,df):
        self.setRowCount(0)
        self.setRowCount(len(df.index))
        for row_num, row in enumerate(df.index):
            for col_num, col in enumerate(df.columns):
                item = QTableWidgetItem(str(df.loc[row, col]))
                item.setTextAlignment(Qt.AlignCenter)
                self.setItem(row_num, col_num, item)  # +++


    def _addRow(self):
        rowCount = self.rowCount()
        self.insertRow(rowCount )

    def _removeRow(self):
        if self.rowCount() > 0:
            self.removeRow(self.currentRow())

            
class BarItem(object):
    def __init__(self, length: float = 0, area: float = 0.0, e: float = 0, q: float = 0):
        self.length = length
        self.area = area

        self.L = length
        self.A = area
        self.E = e
        self.Q = q


class PowerItem(object):
    def __init__(self, point = 0, power = 0):
        self.point = point
        self.power = power


class QxItem(object):
    def __init__(self, bar = None, power = 0):
        self.bar = bar
        self.power = power
