from validaParesClass import ValidaPares
import sympy as sp

class CalculoDerivada(ValidaPares):
    def __init__(self, allX: list, allY: list, func=None) -> None:
        super().__init__(allX, allY)
        self.func = func
        self.index = 0

    def derivadaReal(self):
        if self.func:
            x = sp.symbols('x')
            f = sp.sympify(self.func)

            derivada = sp.diff(f, x)

            f_lambda = sp.lambdify(x, derivada)

            derivada_no_ponto = f_lambda(self.allX[self.index])
            
            return derivada_no_ponto

    def calcErroDiff(self):
        if self.result and self.func:
            x = self.derivadaReal()
            return self.derivadaReal() - self.result
        
    def calcErroPercent(self):
        if self.result and self.func:
            return self.calcErroDiff() / self.result * 100