from tabulate import tabulate
import sympy as sp

class Base0:
    def __init__(self)  -> None:
        self.headers = ['x']

    def addColumn(self, array, label):
        self.table = [row + [array[i]] for i, row in enumerate(self.table)]
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

