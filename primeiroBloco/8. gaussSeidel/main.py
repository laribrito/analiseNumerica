import sys
import os
import copy

# Obtém o diretório atual do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Adiciona o diretório eliminacaoGauss do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '5. eliminacaoDeGauss')))

from SolucoesSistemaClass import SolucoesSistema

class GaussSeidel(SolucoesSistema):
    def __init__(self, matriz) -> None:
        super().__init__(matriz)

    def xN(self, n):
        sum = 0
        for i in range(self.k):
            if i != n:
                sum+=self.M[n][i]*self.X[i]
        xn = (self.B[n] - sum)/self.M[n][n]
        return xn
    
    def getNewX(self):
        for i in range(self.k):
            self.X[i] = self.xN(i)
        return self.X

    def resolve(self):
        j = 0
        M = copy.deepcopy(self.M)
        B = copy.deepcopy(self.B)
        self.X = [0] * self.k

        X = self.getNewX()

        while not self.variacaoAbs(X, self.X) and not self.variacaoRel(X, self.X):
            self.X = X.copy()
            X = self.getNewX()
        
        self.solution = self.X.copy()

        avalicao = self.test()
        
        return f'{self.vetorParaStr(self.solution)}\n{avalicao}'
    
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
                resultado = GaussSeidel(matriz).resolve()
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
