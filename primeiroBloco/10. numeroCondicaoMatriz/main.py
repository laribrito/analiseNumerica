import sys
import os
import copy

# Obtém o diretório atual do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Adiciona o diretório eliminacaoGauss do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '9. matrizInversa')))

from SolucoesSistemaClass import SolucoesSistema
from main9 import MatrizInversaGaussJordan

class NumCondicaoMatriz():
    def __init__(self, matriz) -> None:
        if not self.ehMatrizValida(matriz):
            raise Exception('Essa matriz não é quadrada')
        
        self.M = matriz
        self.k = len(matriz)

    def ehMatrizValida(self, matriz):
        qtdLinhas = len(matriz)
        for i in matriz:
            if len(i) != qtdLinhas:
                return False
        
        return True

    def resolve(self):
        # encontrar a matriz inversa
        matr = [ i + [0] for i in self.M]
        inversa = MatrizInversaGaussJordan(matr).inversa()

        x = MatrizInversaGaussJordan.multiMatrizes(self.M, inversa)

        # Calcular a norma de Frobenius das matrizes
        norma_M = self.normaFrobenius(self.M)
        norma_inversa = self.normaFrobenius(inversa)

        # Calcular o número de condição
        numero_condicao = norma_M * norma_inversa

        return f'{numero_condicao}'

    def normaFrobenius(self, matriz):
        # Implemente aqui o cálculo da norma de Frobenius da matriz
        # Por exemplo, para uma matriz A, a norma de Frobenius é a raiz quadrada da soma dos quadrados dos elementos da matriz
        soma_quadrados = sum(sum(x**2 for x in linha) for linha in matriz)
        norma = soma_quadrados ** 0.5
        return norma

def main():
    # Limpa o arquivo out.txt
    open(os.path.join(dir_path, 'out.txt'), 'w').close()

    # Abre o arquivo in.txt e lê as funções e parâmetros
    with open(os.path.join(dir_path,'in.txt'), 'r') as f:
        linhas = f.readlines()

    matriz = []
    for index, i in enumerate(linhas):
        linha = [float(j) for j in i.split()]
        
        if not len(linha) or len(linhas) == index:
            try:
                resultado = NumCondicaoMatriz(matriz).resolve()
            except Exception as e:
                resultado = f'ERRO: {e}'

            # Escreve os resultados no arquivo out.txt
            with open(os.path.join(dir_path, 'out.txt'), 'a') as arquivo:
                arquivo.write(resultado + '\n\n')
            matriz.clear()
        else:
            matriz.append(linha)

if __name__ == '__main__':
    main()
