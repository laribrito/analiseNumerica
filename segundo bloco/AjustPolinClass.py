import os
import matplotlib.pyplot as plt
import numpy as np

class AjustPolin:
    def __init__(self, allX:list, allY:list, indexCaso:int, path:str) -> None:
        if AjustPolin.validaPares(allX, allY):
            self.allX = allX
            self.allY = allY
            self.qtdPares = len(allX)
            self.solution = None
            self.indexCaso = indexCaso
            self.pathGraph = path

        else:
            raise Exception('Os pares passados como parâmetro estão incompletos')

    def validaPares(allX, allY):
        return len(allX) == len(allY)

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
    
    '''
    parse num
    '''
    def pNum(num):
        return f'{num:.5f}'
