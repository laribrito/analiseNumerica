import sys
import os
import copy

# Obtém o diretório atual do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from SolucoesSistemaClass import SolucoesSistema

class MatrizInversaGaussJordan(SolucoesSistema):
    def __init__(self, matriz) -> None:
        super().__init__(matriz)
        self.M_inversa = None

    def inversa(self):
        # Criar matriz identidade
        M = copy.deepcopy(self.M)

        matrizI = [[1 if i == j else 0 for j in range(self.k)] for i in range(self.k)]

        # Concatenar a matriz original com a matriz identidade
        matrizAumentada = [row + matrizI[i] for i, row in enumerate(M)]

        for col in range(self.k):
            pivot = col
            for i in range(col + 1, self.k):
                if abs(matrizAumentada[i][col]) > abs(matrizAumentada[pivot][col]):
                    pivot = i

            matrizAumentada[col], matrizAumentada[pivot] = matrizAumentada[pivot], matrizAumentada[col]

            valorPivot = matrizAumentada[col][col]
            for i in range(self.k * 2):
                matrizAumentada[col][i] /= valorPivot

            for i in range(self.k):
                if i != col:
                    fator = matrizAumentada[i][col]
                    for j in range(self.k * 2):
                        matrizAumentada[i][j] -= fator * matrizAumentada[col][j]

        # Retornar a parte direita da matriz aumentada (a inversa)
        self.M_inversa = [row[self.k:] for row in matrizAumentada]
        return self.M_inversa

    def resolve(self):
        # encontrar a matriz inversa
        self.inversa()

        x = MatrizInversaGaussJordan.multiMatrizes(self.M_inversa, [[item] for item in self.B])

        self.solution = [item[0] for item in x]

        avalicao = self.test()
        
        return f'{SolucoesSistema.MatrizParaStr(self.M_inversa)}\n{SolucoesSistema.vetorParaStr(self.solution)}\n{avalicao}'
    
    def multiMatrizes(a, b):
        result = [[0] * len(b[0]) for _ in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    result[i][j] += a[i][k] * b[k][j]
        return result
    
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
                resultado = MatrizInversaGaussJordan(matriz).resolve()
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
