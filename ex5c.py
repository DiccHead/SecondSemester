class FifthC:
    def __init__(self, x0, xn, deltaX):
        self.x0 = x0
        self.xn = xn
        self.deltaX = deltaX
    
    def program(self):
        if self.deltaX < 1:
            self.x0 = int(self.x0 / self.deltaX)
            self.xn = int(self.xn / self.deltaX)
        self.all_x = []
        self.all_y = []
        for x in range(self.x0, self.xn+1):
            if self.deltaX < 1:
                x *= self.deltaX
            if x > 1.75:
                if x != 2 and x != -3:
                    y = ((x + 5) * (x - 6)) / ((x - 2)*(x + 3))
                    self.all_x.append(x)
                    self.all_y.append("{j:.3f}".format(j = y))
                else:
                    self.all_x.append(x)
                    self.all_y.append("none")
            if x <= 1.75:
                if x != 1:
                    y = (x*x + 2*x + 4)/(x*x - 2*x +1)
                    self.all_x.append(x)
                    self.all_y.append("{j:.3f}".format(j = y))
                else:
                    self.all_x.append(x)
                    self.all_y.append("none")
    

    def print_all(self):
        for i in range(len(self.all_x)):
            print(f"x = {self.all_x[i]}, y = {self.all_y[i]}")


x0 = -10
xn = 10
deltaX = 0.25

ekz = FifthC(x0, xn, deltaX)
ekz.program()
ekz.print_all()

