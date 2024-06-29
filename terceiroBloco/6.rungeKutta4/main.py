import sys
import os

import sympy as sp
from tabulate import tabulate


# Obtém o diretório atual do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from base1Class import Base1

class RungeKutta4(Base1):
    def __init__(self, funcao: str, h: int, pontoXInicial:list, maxX:int, pathSave:str)  -> None:
        super().__init__(funcao, h, pontoXInicial, maxX, pathSave)
        self.resultado = [self.y0]

    def proxItem(self, yi, x):
        # Passo 1: Calcule k1
        k1 = self.h * self.resolverFunc(x, yi)
        
        # Passo 2: Calcule k2
        k2 = self.h * self.resolverFunc(x + self.h / 2, yi + k1 / 2)
        
        # Passo 3: Calcule k3
        k3 = self.h * self.resolverFunc(x + self.h / 2, yi + k2 / 2)
        
        # Passo 4: Calcule k4
        k4 = self.h * self.resolverFunc(x + self.h, yi + k3)
        
        # Passo 5: Calcule o próximo valor de y usando a combinação ponderada de k1, k2, k3 e k4
        result = yi + (1/6) * k1 + (1/3) * k2 + (1/3) * k3 + (1/6) * k4
        
        return result

    def resolve(self):
        self.findRealSolution()

        x_values = self.valoresX()

        for i in range(len(x_values)-1):
            self.resultado.append(self.proxItem(self.resultado[i], x_values[i]))

        self.addColumn(self.resultado, 'yCalculado')

        # calc erros
        self.calcularErroGlobal()
        self.calcularErroLocal()

        return self.parseTable()

def main():
    # Limpa o arquivo out.txt
    open(os.path.join(dir_path, 'out.txt'), 'w').close()

    # Abre o arquivo in.txt e lê as funções e parâmetros
    with open(os.path.join(dir_path,'in.txt'), 'r') as f:
        linhas = f.read()
    linhas = linhas.split('\n')

    # Itera sobre as linhas do arquivo de entrada
    index = 0
    while index + 1 < len(linhas):
        func = linhas[index]
        index+=1
        pontoX = [float(x) for x in linhas[index].split()]
        index+=1
        maxX = float(linhas[index])
        index+=1
        h = float(linhas[index])
        index+=1

        obj = RungeKutta4(func, h, pontoX, maxX, dir_path)
        resultado = obj.resolve()
        # obj.plot()

        # Escreve os resultados no arquivo out.txt
        with open(os.path.join(dir_path, 'out.txt'), 'a') as arquivo:
            arquivo.write(str(resultado) + '\n\n')

if __name__ == '__main__':
    main()
