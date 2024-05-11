import sys
import os

import numpy as np
from sympy import Symbol, zeros

# Obtém o diretório atual do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import AjustPolinClass

class MMQ_Discreto(AjustPolinClass.AjustPolin):
    def __init__(self, valoresX: list, valoresY: list) -> None:
        super().__init__(valoresX, valoresY)

    def resolve(self):
        x = Symbol("x")
        funcao = [1, eval("x"), eval("x**2")]
        tamFuncao = len(funcao)
        matrizUi = [self.qtdPares*[1]]
        
        listaAux = []
        for i in range(tamFuncao):
            aux = funcao[i]
            if(aux != 1):
                for elem in self.allX:
                    listaAux.append(aux.subs(x, elem))
                    
                matrizUi.append(listaAux)
                listaAux = []

        vetorF = zeros(tamFuncao, 1)
        matrizRes = zeros(tamFuncao)
        for i in range(tamFuncao):
            for j in range(tamFuncao):
                matrizRes[i,j] = sum(np.multiply(matrizUi[i], matrizUi[j]))
            vetorF[i] = sum(np.multiply(self.allY, matrizUi[i]))
        resultado = matrizRes.LUsolve(vetorF)

        potencializacao = 1
        resultado_final = 0
        for i in range(tamFuncao):
            resultado_final += round(resultado[i,0], 2) * potencializacao
            potencializacao *= x

        return resultado_final

def main():
    # Limpa o arquivo out.txt
    open(os.path.join(dir_path, 'out.txt'), 'w').close()

    # Abre o arquivo in.txt e lê as funções e parâmetros
    with open(os.path.join(dir_path,'in.txt'), 'r') as f:
        linhas = f.readlines()

    # Itera sobre as linhas do arquivo de entrada
    listX = []
    listY = []
    for l in linhas:
        try:
            params = l.split()
            x = params[0]
            y = params[1]

            listX.append(float(x))
            listY.append(float(y))
        except:
            resultado = MMQ_Discreto(listX, listY).resolve()
            # Escreve os resultados no arquivo out.txt
            with open(os.path.join(dir_path, 'out.txt'), 'a') as arquivo:
                arquivo.write(str(resultado) + '\n\n')

            listX.clear()
            listY.clear()

if __name__ == '__main__':
    main()
