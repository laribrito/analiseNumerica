from validaParesClass import ValidaPares
import sympy as sp

class CalculoDerivada(ValidaPares):
    def __init__(self, allX: list, allY: list, func=None) -> None:
        super().__init__(allX, allY)
        self.func = func
        self.index = 0

    def derivadaReal(self, grauDerivada=1):
        if self.func:
            x = sp.symbols('x')
            f = sp.sympify(self.func)

            derivada = f
            for _ in range(grauDerivada):
                derivada = sp.diff(derivada, x)

            f_lambda = sp.lambdify(x, derivada)

            derivada_no_ponto = f_lambda(self.allX[self.index])
            
            return derivada_no_ponto

    def calcErroDiff(self, grauDerivada=1):
        if self.result and self.func:
            x = self.derivadaReal(grauDerivada)
            return self.derivadaReal(grauDerivada) - self.result
        
    def calcErroPercent(self, grauDerivada=1):
        if self.result and self.func:
            return self.calcErroDiff(grauDerivada) / self.result * 100