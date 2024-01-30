from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyGraphicsView(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.left_sealing = False
        self.right_sealing = False
        self.scale_x = 1
        self.scale_y = 1
        self.indent = (0, 0)
        self.bars = []
        self.F = []
        self.qxs = []
        self.new_bars = []

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawSealings(qp)
        self.drawKernels(qp)
        self.drawRunning(qp)
        self.drawConcentrated(qp)
        qp.end()

    def drawSealings(self, qp):
        if self.left_sealing == True:
            pen = QPen(Qt.black, 2, Qt.SolidLine)
            qp.setPen(pen)
            qp.drawLine(40, 42, 40, 350)
            pen = QPen(Qt.black, 1, Qt.SolidLine)
            qp.setPen(pen)
            y = 42
            for i in range(16):
                qp.drawLine(40, y, 15, y + 10)
                y += 20
        if self.right_sealing == True:
            pen = QPen(Qt.black, 2, Qt.SolidLine)
            qp.setPen(pen)
            qp.drawLine(571, 42, 571, 350)
            pen = QPen(Qt.black, 1, Qt.SolidLine)
            qp.setPen(pen)
            y = 42
            for i in range(16):
                qp.drawLine(571, y + 10, 596, y)
                y += 20

    def drawKernels(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        scale_x = self.scale_x
        scale_y = self.scale_y
        length = 40

        for kern in self.bars:
            if kern != None:
                point1_x = length
                point1_y = 195 + (kern.area / 2) * scale_y
                point2_x = length
                point2_y = 195 - (kern.area / 2) * scale_y
                point3_x = length + (kern.length * scale_x)
                point3_y = point2_y = 195 - (kern.area / 2) * scale_y
                point4_x = length + (kern.length * scale_x)
                point4_y = point1_y = 195 + (kern.area / 2) * scale_y
                qp.drawLine(point1_x, point1_y, point2_x, point2_y)
                qp.drawLine(point2_x, point2_y, point3_x, point3_y)
                qp.drawLine(point3_x, point3_y, point4_x, point4_y)
                qp.drawLine(point4_x, point4_y, point1_x, point1_y)
                length += kern.length * scale_x

    def drawConcentrated(self, qp):
        pen = QPen(Qt.magenta, 3, Qt.SolidLine)
        qp.setPen(pen)
        scale_x = self.scale_x
        for power in self.F:
            length = 40
            if power.point == 0:
                length = 40
            else:
                counter = 0
                kern_count = 0
                while kern_count != power.point - 1 and counter != len(self.bars):
                    if self.bars[counter] != None:
                        length += self.bars[counter].length * scale_x
                        kern_count += 1
                        counter += 1
            pen = QPen(Qt.magenta, 6, Qt.SolidLine)
            qp.setPen(pen)
            if power.power > 0:
                qp.drawLine(length+2, 195, length + 33, 195)
                qp.drawLine(length + 35, 195, length + 25, 203)
                qp.drawLine(length + 35, 195, length + 25, 187)
            if power.power < 0:
                qp.drawLine(length-2, 195, length - 33, 195)
                qp.drawLine(length - 35, 195, length - 25, 203)
                qp.drawLine(length - 35, 195, length - 25, 187)

    def drawRunning(self, qp):
        pen = QPen(Qt.blue, 2, Qt.SolidLine)

        qp.setPen(pen)
        scale_x = self.scale_x
        scale_y = self.scale_y
        arrow_length = 28
        arrow_streak_x_margin = arrow_length * (6 / 20)
        arrow_streak_y_margin = arrow_length * (3 / 20)
        for power in self.qxs:
            length = 40
            counter = 0
            kern_count = 0
            while kern_count != power.bar - 1 and counter != len(self.bars):
                if self.bars[counter] != None:
                    length += self.bars[counter].length * scale_x
                    kern_count += 1
                    counter += 1
            power_length = self.bars[counter].length * scale_x
            arrow_count = int(power_length // arrow_length + 1)
            arrows_scale = power_length / (arrow_count * arrow_length)
            length_of_arrow_seq = length
            for i in range(arrow_count):
                if power.power > 0:
                    qp.drawLine(length_of_arrow_seq, 195, length_of_arrow_seq + arrow_length * arrows_scale, 195)
                    qp.drawLine(length_of_arrow_seq + arrow_length * arrows_scale, 195,
                                length_of_arrow_seq + arrow_length * arrows_scale - arrow_streak_x_margin * arrows_scale,
                                195 - arrow_streak_y_margin * arrows_scale)
                    qp.drawLine(length_of_arrow_seq + arrow_length * arrows_scale, 195,
                                length_of_arrow_seq + arrow_length * arrows_scale - arrow_streak_x_margin * arrows_scale,
                                195 + arrow_streak_y_margin * arrows_scale)
                elif power.power < 0:
                    qp.drawLine(length_of_arrow_seq, 195, length_of_arrow_seq + arrow_length * arrows_scale, 195)
                    qp.drawLine(length_of_arrow_seq, 195,
                                length_of_arrow_seq + arrow_streak_x_margin * arrows_scale,
                                195 - arrow_streak_y_margin * arrows_scale)
                    qp.drawLine(length_of_arrow_seq, 195,
                                length_of_arrow_seq + arrow_streak_x_margin * arrows_scale,
                                195 + arrow_streak_y_margin * arrows_scale)
                length_of_arrow_seq += arrow_length * arrows_scale
