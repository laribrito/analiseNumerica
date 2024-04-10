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
from main5 import EliminacaoGauss

class FatoracaoLu(SolucoesSistema):
    def __init__(self, matriz) -> None:
        super().__init__(matriz)

    def resolve(self):
        j = 0
        M = copy.deepcopy(self.M)
        B = copy.deepcopy(self.B)
        
        # inicialização de LU
        U = [[0] * self.k for _ in range(self.k)]
        L = [[0] * self.k for _ in range(self.k)]

        for i in range(len(L)):
            L[i][i] = 1
            if i != 0:
                L[i][0] = M[i][0]/M[0][0]
        

        # completa LU
        for i in range(self.k):
            for j in range(self.k):
                if i <= j:
                    sum = 0
                    for k in range(i):
                        sum +=L[i][k]*U[k][j]
                    U[i][j] = M[i][j] - sum
                else:
                    sum = 0
                    for k in range(j):
                        sum +=L[i][k]*U[k][j]
                    L[i][j] = (M[i][j] - sum) / U[j][j]
        self.L = copy.deepcopy(L)
        self.U = copy.deepcopy(U)
        LU = self.LUparaStr()

        # encontrar o vetor Y
        for linha, b in zip(L, B):
            linha.reverse()
            linha.append(b)
        L.reverse()

        try:
            resultadoY = EliminacaoGauss(L)
            resultadoY.resolve()
        except Exception as e:
            return f'ERRO: {e}'
        
        self.Y = resultadoY.solution
        self.Y.reverse()

        # encontrar resultado final
        for linha, b in zip(U, self.Y):
            linha.append(b)

        try:
            objX = EliminacaoGauss(U)
            objX.resolve()
        except Exception as e:
            return f'ERRO: {e}'
        
        self.solution = objX.solution

        avalicao = self.test()
        
        return f'{LU}\n{self.vetorParaStr(self.Y)}\n{self.vetorParaStr(self.solution)}\n{avalicao}'
    
    def LUparaStr(self):
        txt = ''
        for i in range(self.k):
            txt+='['
            for j in range(self.k):
                txt+=f'{self.L[i][j]:4.5f}, '
            txt=txt[:-2]
            txt+=']'
            txt+=' '*2
            txt+='['
            for j in range(self.k):
                txt+=f'{self.U[i][j]:4.5f}, '
            txt=txt[:-2]
            txt+=']\n'
        return txt[:-1]

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
                resultado = FatoracaoLu(matriz).resolve()
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
