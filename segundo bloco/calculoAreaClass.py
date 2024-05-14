from validaParesClass import ValidaPares
import sympy as sp

class CalculosErros:
    def __init__(self,allX, f=None) -> None:
            self.func = f
            self.result = None
            self.allX = allX

    def integralReal(self):
        if self.func:
            x = sp.symbols('x')
            
            # Integre a expressão simbólica
            return sp.integrate(self.func, (x, self.allX[0], self.allX[-1])).evalf()

    def calcErroDiff(self):
        if self.result and self.func:
            x = self.integralReal()
            return self.integralReal() - self.result
        
    def calcErroPercent(self):
        if self.result and self.func:
            return self.calcErroDiff() / self.result * 100

class CalculoIntegral(ValidaPares, CalculosErros):
    def __init__(self, listX, listY,f=None) -> None:
        ValidaPares.__init__(self, listX, listY)
        CalculosErros.__init__(self, listX, f)
        self.func = f
        self.result = None

    def resolve(self):
        raise Exception('Implemente o método resolve')
