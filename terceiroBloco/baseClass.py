from tabulate import tabulate
import sympy as sp

class Base:
    def __init__(self, funcao: str, h: int, pontoXInicial:list, maxX:int, pathSave:str)  -> None:
        self.f = funcao
        self.h = h
        self.x0 = pontoXInicial[0]
        self.y0 = pontoXInicial[1]
        self.xf = maxX
        self.pathToSave = pathSave
        self.parsedResult = ''
        self.headers = ['x', 'yVerdadeiro']
        self.resultado = None

    def addColumn(self, array, label):
        self.table = [row + [array[i]] for i, row in enumerate(self.table)]
        self.headers.append(label)

    def resolverFunc(self, xValue, yValue):
        x, y = sp.symbols('x y')
        return self.func.subs({x: xValue, y: yValue})

    def transformFunction(self):
        x = sp.symbols('x')

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

    def valoresX(self):
        intervaloX = self.xf - self.x0
        qtd = intervaloX / self.h
        lista = [self.x0]
        x = self.x0
        while x < self.xf:
            x += self.h
            lista.append(x)

        lista[-1] = self.xf
        
        return lista
    
    def encontraFuncaoDerivada(self):
        x = sp.symbols('x')
        
        self.transformFunction()

        F = sp.integrate(self.func, x)

        C = sp.symbols('C')
        F = F + C

        C_value = sp.solve(F.subs(x, self.x0) - self.y0, C)[0]

        F = F.subs(C, C_value)

        return F

    def findRealSolution(self):
        if self.f:
            x = sp.symbols('x')

            F = self.encontraFuncaoDerivada()

            x_values = self.valoresX()

            self.realSolution = [F.subs(x, val) for val in x_values]

            self.table = [[x, y] for x, y in zip(x_values, self.realSolution)]
        
    def parseTable(self):
        if self.table:
            return tabulate(self.table, headers=self.headers , tablefmt="pipe")

