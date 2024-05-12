from validaParesClass import ValidaPares
import sympy as sp

class CalculoIntegral(ValidaPares):
    def __init__(self, listX, listY,f=None) -> None:
        super().__init__(listX, listY)
        self.func = f
        self.result = None

    def integralReal(self):
        if self.func:
            x = sp.symbols('x')
            
            # Integre a expressão simbólica
            return sp.integrate(self.func, (x, self.allX[0], self.allX[-1]))

    def calcErro(self):
        if self.result and self.func:
            return self.integralReal() - self.result