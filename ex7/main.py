import sys
from math import log
import ui_file
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox



class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = ui_file.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.Integral)
        self.ui.action_2.triggered.connect(self.Info)

    def Info(self):
        QMessageBox.about(self, "Об авторе", "Программу выполнил студент 2023-ФГиИБ-ИСиТ-2б Утягулов Артем.")

    def Integral(self):
        a = int(self.ui.textEdit.toPlainText())
        b = int(self.ui.textEdit_2.toPlainText())
        eps = float(self.ui.textEdit_3.toPlainText())
        answer, iter = self.calculate(a, b, eps)
        answer_left, iter_left = self.calculate_left(a, b, eps)
        answer_right, iter_right = self.calculate_right(a, b, eps)
        self.ui.label_5.setText("{x:.3f}".format(x=answer) + " Итераций: " + str(iter))
        self.ui.label_9.setText("{x:.3f}".format(x=answer_right) + " Итераций: " + str(iter_right))
        self.ui.label_11.setText("{x:.3f}".format(x=answer_left) + " Итераций: " + str(iter_left))
        

    def f(self, x):
        return (0.5+x**0.5)/(1+log(x)**2)
    
    def get_area(self, a, b, n):
        deltaX = (b - a) / n
        
        multiplicator = 1
        if str(deltaX).count(".") != 0:
            multiplicator = 10**len(str(deltaX).split(".")[1])

        full_sum = 0
        for i in range(a*multiplicator+int(deltaX*multiplicator), b*multiplicator+1, int(deltaX*multiplicator)):
            i = i / multiplicator
            s = self.f(i-deltaX/2)*deltaX
            full_sum += s
        
        return full_sum
    
    def get_area_left(self, a, b, n):
        deltaX = (b - a) / n
        
        multiplicator = 1
        if str(deltaX).count(".") != 0:
            multiplicator = 10**len(str(deltaX).split(".")[1])

        full_sum = 0
        for i in range(a*multiplicator, b*multiplicator+1-int(deltaX*multiplicator), int(deltaX*multiplicator)):
            i = i / multiplicator
            s = self.f(i)*deltaX
            full_sum += s
        
        return full_sum
    
    def get_area_right(self, a, b, n):
        deltaX = (b - a) / n
        
        multiplicator = 1
        if str(deltaX).count(".") != 0:
            multiplicator = 10**len(str(deltaX).split(".")[1])

        full_sum = 0
        for i in range(a*multiplicator+int(deltaX*multiplicator), b*multiplicator+1, int(deltaX*multiplicator)):
            i = i / multiplicator
            s = self.f(i)*deltaX
            full_sum += s
        
        return full_sum
    
    def calculate(self, a, b, eps):
        done = False
        full_sum = 0
        n = 1

        iter = 0
        while done != True:
            S1 = self.get_area(a, b, n)
            n = n * 2
            S2 = self.get_area(a, b, n)
            iter += 1
            if abs(S2-S1) < eps:
                full_sum = S2
                done = True

        return full_sum, iter
    
    def calculate_left(self, a, b, eps):
        done = False
        full_sum = 0
        n = 1

        iter = 0
        while done != True:
            S1 = self.get_area_left(a, b, n)
            n = n * 2
            S2 = self.get_area_left(a, b, n)
            iter += 1
            if abs(S2-S1) < eps:
                full_sum = S2
                done = True

        return full_sum, iter
    
    def calculate_right(self, a, b, eps):
        done = False
        full_sum = 0
        n = 1

        iter = 0
        while done != True:
            S1 = self.get_area_right(a, b, n)
            n = n * 2
            S2 = self.get_area_right(a, b, n)
            iter += 1
            if abs(S2-S1) < eps:
                full_sum = S2
                done = True
                
        return full_sum, iter
    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())