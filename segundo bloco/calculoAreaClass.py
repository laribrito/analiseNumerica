from validaParesClass import ValidaPares
from sympy import integrate, Symbol

class CalculoIntegral(ValidaPares):
    def __init__(self, listX, listY,f=None) -> None:
        super().__init__(listX, listY)
        self.func = f

    def calcErro(self):
        if self.func:
            x = Symbol('x')
            return integrate(self.func, (x, self.allX[0], self.allX[-1]))