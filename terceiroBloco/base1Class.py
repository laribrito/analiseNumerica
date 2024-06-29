from tabulate import tabulate
import sympy as sp

from base0Class import Base0

class Base1(Base0):
    def __init__(self, funcao: str, h: int, pontoXInicial:list, maxX:int, pathSave:str)  -> None:
        self.f = funcao
        self.h = h
        self.x0 = pontoXInicial[0]
        self.y0 = pontoXInicial[1]
        self.xf = maxX
        self.pathToSave = pathSave
        self.parsedResult = ''
        self.headers = ['x', 'yVerdadeiro']
        self.vars = sp.symbols('x y')
        self.resultado = None

    def resolverFunc(self, xValue, yValue):
        x, y = self.vars
        return self.func.subs({x: xValue, y: yValue})

    def transformFunction(self):
        x, y = self.vars

        self.func = sp.sympify(self.f)

    def calcularErroGlobal(self):
        if self.resultado and self.realSolution:
            self.erroGlobal = []
            x_values = self.valoresX()
            for i in range(len(x_values)):
                erro = ((self.realSolution[i]-self.resultado[i])/self.realSolution[i])*100
                self.erroGlobal.append(erro)

            self.erroGlobal[0] = 0
            self.addColumn(self.erroGlobal, 'Erro Global')

    def calcularErroLocal(self):
        # if self.erroGlobal:
        #     self.erroLocal = [0]
        #     for x in range(1, len(self.erroGlobal)):
        #         r1 = self.realSolution[x]
        #         r2 = self.resultado[x]
        #         erro = (r1 - r2)/((r1+r2)/2)*100
        #         self.erroLocal.append(erro)

        #     self.addColumn(self.erroLocal, 'Erro Local')
        pass
 
    def encontraFuncaoDerivada(self):
        x, y = sp.symbols('x y')
        
        self.transformFunction()
        
        # Integrando a função
        F = sp.integrate(self.func, x)
        
        # Adicionando a constante de integração
        C = sp.symbols('C')
        F = F + C
        
        # Substituindo os valores de x e y para resolver C
        C_value = sp.solve(F.subs({x: self.x0, y: self.y0}) - self.y0, C)[0]
        
        # Substituindo C na função
        F = F.subs(C, C_value)
        
        return F

    def findRealSolution(self):
        if self.f:
            x, y = self.vars

            F = self.encontraFuncaoDerivada()

            x_values = self.valoresX()

            self.realSolution = [self.y0]
            for index, x_i in enumerate(x_values[1:]):
                self.realSolution.append(F.subs({x: x_i, y: self.realSolution[index]}))

            self.table = [[x, y] for x, y in zip(x_values, self.realSolution)]
