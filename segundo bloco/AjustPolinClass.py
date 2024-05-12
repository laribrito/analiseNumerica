import os
import matplotlib.pyplot as plt
import numpy as np
from validaParesClass import ValidaPares

class AjustPolin(ValidaPares):
    def __init__(self, allX: list, allY: list, indexCaso: int, pathSave) -> None:
        super().__init__(allX, allY)
        self.indexCaso = indexCaso
        self.pathGraph = pathSave

    def plot(self, labelFunc=None):
        # Avalia a função
        x = np.linspace(min(self.allX), max(self.allX), 100)
        y = eval(str(self.solution))

        # Plota a função
        plt.plot(x, y, label=labelFunc)

        # Plota os pontos
        plt.scatter(self.allX, self.allY, color='red', label='Pontos')

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Gráfico da Função e Pontos')
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join(self.pathGraph, f'grafico_caso{self.indexCaso}.png'))
        plt.clf()
