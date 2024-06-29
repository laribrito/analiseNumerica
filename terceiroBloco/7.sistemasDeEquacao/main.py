import sys
import os
import sympy as sp
from tabulate import tabulate

# Obtém o diretório atual do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Adiciona o diretório extra do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '6.rungeKutta4')))

from base0Class import Base0

class SistemaEquacaoDiferencial(Base0):
    def __init__(self, listFuncao: list, h: float, listPontoXInicial: list, maxX: float, pathSave: str) -> None:
        super().__init__()
        self.funcList = listFuncao
        self.pontoInicialList = listPontoXInicial
        self.h = h
        self.x0 = self.pontoInicialList[0][0]
        self.xf = maxX
        self.pathToSave = pathSave
        self.resultado = [[ponto[1] for ponto in self.pontoInicialList]]
        self.ordem = len(self.funcList)
        
        # Converte as funções em expressões simbólicas
        # self.exprList = [sp.sympify(func) for func in self.funcList]
        self.funcs = [sp.sympify(func) for func in self.funcList]
        self.vars = sp.symbols('x ' + ' '.join(f'y{i+1}' for i in range(self.ordem)))
        # self.funcs = [sp.lambdify(self.vars, expr) for expr in self.exprList]

    def resolverFunc(self, xValue, yI, yList, indexY):
        # Mapeia x para xValue
        substituicoes = {self.vars[0]: xValue}
        
        # Mapeia yi para yI
        substituicoes[self.vars[indexY + 1]] = yI
        
        # Mapeia os demais yi para os valores correspondentes em yList
        for i in range(len(yList)):
            if i != indexY:
                substituicoes[self.vars[i + 1]] = yList[i]

        # Realiza as substituições nas funções simbólicas
        return self.funcs[indexY].subs(substituicoes)

    def proxItem(self, yi:list, x:float):
        result = yi.copy()

        for index, y in enumerate(yi):
            k1 = self.h * self.resolverFunc(x, y, yi, index)
        
            k2 = self.h * self.resolverFunc(x + self.h / 2, y + k1 / 2, yi, index)
        
            k3 = self.h * self.resolverFunc(x + self.h / 2, y + k2 / 2, yi, index)
        
            k4 = self.h * self.resolverFunc(x + self.h, y + k3, yi, index)
        
            r = y + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

            result[index] = r
        
        return result

    def resolve(self):
        x_values = self.valoresX()

        for i in range(1, len(x_values)):
            self.resultado.append(self.proxItem(self.resultado[-1], x_values[i-1]))

        self.addColumn(x_values, 'x')
        # adiciona cada variável na tabela de resultados
        for index, var in enumerate(self.vars[1:]):
            self.addColumn([y[index] for y in self.resultado], var)

        return self.parseTable()

def main():
    # Limpa o arquivo out.txt
    open(os.path.join(dir_path, 'out.txt'), 'w').close()

    # Abre o arquivo in.txt e lê as funções e parâmetros
    with open(os.path.join(dir_path,'in.txt'), 'r') as f:
        linhas = f.read().split('\n')

    # Itera sobre as linhas do arquivo de entrada
    index = 0
    while index + 1 < len(linhas):
        qtdFunc = int(linhas[index])
        index += 1
        funcList = []
        pontoXList = []
        for _ in range(qtdFunc):
            func = linhas[index]
            funcList.append(func)
            index += 1
            pontoX = [float(x) for x in linhas[index].split()]
            pontoXList.append(pontoX)
            index += 1
        maxX = float(linhas[index])
        index += 1
        h = float(linhas[index])
        index += 1

        obj = SistemaEquacaoDiferencial(funcList, h, pontoXList, maxX, dir_path)
        resultado = obj.resolve()
       
        # Escreve os resultados no arquivo out.txt
        with open(os.path.join(dir_path, 'out.txt'), 'a') as arquivo:
            arquivo.write(str(resultado) + '\n\n')

if __name__ == '__main__':
    main()
