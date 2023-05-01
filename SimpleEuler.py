import math
from decimal import Decimal

class SimpleEuler:
    def __init__(self, equation, x0, y0, domain, h):
        self.original_equation = equation
        self.equation = equation.replace("raiz", "math.sqrt").replace("^","**")
        self.x0 = x0
        self.y0 = y0
        self.domain = domain
        self.h = h
        self.listXn=[]
        self.listYn=[]
        self.f=[]
        self._euler()
        
    def _f(self,xn, yn):
        x=xn
        y=yn
        self.f.append(str(  round(eval(self.equation),8)  ))
        return eval(self.equation)
        
    def _euler(self):
        self.listXn.append(self.x0)
        self.listYn.append(self.y0)

        while True:
            self.listXn.append(  str(Decimal(self.listXn[-1]) +  Decimal(self.h))  )
            resultF= self._f(float(self.listXn[-1]), float(self.listYn[-1]))
            self.listYn.append( str(  round( eval(str(self.listYn[-1]) + "+" + str(self.h) + "*" + str(resultF)), 8 ) )   )
            if float(self.listXn[-1]) >= float(self.domain):
                break
    def getAll(self):
        return {
            "x" : self.listXn,
            "y" : self.listYn,
            "f" : self.f,
            "domain" : self.domain,
            "equation" : self.original_equation,
            "x0" : self.x0,
            "y0" : self.y0,
            "h" : self.h
        }
    def getListX(self):
        return self.listXn
    def getListY(self):
        return self.listYn
    def getListXY(self):
        return {
            "x": self.listXn,
            "y": self.listYn
        }
    def getDomain(self):
        return self.domain
    def getEquation(self):
        return self.original_equation
    def getX0(self):
        return self.x0
    def getY0(self):
        return self.y0
    def getH(self):
        return self.h
    def getF(self):
        return self.f


