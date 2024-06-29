from tabulate import tabulate
import sympy as sp

class Base0:
    def __init__(self)  -> None:
        self.headers = ['x']
        self.x0 = 0
        self.xf = 0
        self.table = []
        self.headers = []

    def addColumn(self, array, label):
        if self.table:
            self.table = [row + [array[i]] for i, row in enumerate(self.table)]
        else:
            self.table = [[row] for row in array]
        self.headers.append(label)

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
     
    def parseTable(self):
        if self.table:
            return tabulate(self.table, headers=self.headers , tablefmt="pipe")

