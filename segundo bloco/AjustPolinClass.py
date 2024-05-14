import os
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from validaParesClass import ValidaPares

class AjustPolin(ValidaPares):
    def __init__(self, allX: list, allY: list, indexCaso: int, pathSave) -> None:
        super().__init__(allX, allY)
        self.indexCaso = indexCaso
        self.pathGraph = pathSave

    def plot(self, labelFunc=None):
        # Avalia a função
        x = np.linspace(min(self.allX), max(self.allX), 100)

        func = sp.sympify(self.solution)
        xSympy = sp.Symbol("x")
        y = [func.subs(xSympy, x_val) for x_val in x]

        plt.plot(x, y, label = labelFunc)
        plt.scatter(self.allX, self.allY, color = 'red', label = 'Pontos de dados')

        # Configurando os limites do eixo Y
        padding = 2
        plt.ylim(min(self.allY)-padding, max(self.allY)+padding)

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Gráfico da Função e Pontos')
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join(self.pathGraph, f'grafico_caso{self.indexCaso}.png'))
        plt.clf()
