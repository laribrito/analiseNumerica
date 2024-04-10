import sympy as sp
import sys
import os

# Obtém o diretório atual do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import EncontrarRaizClass
import OperacoesMatematicas as op

class NewtonRaphson(EncontrarRaizClass.EncontrarRaiz):
    def __init__(self, equacao: str, tolerancia: float, x1: float) -> None:
        super().__init__(equacao, tolerancia, x1, None)

    def dxF_num(self, x, h=1e-5):
        return (self.F(x + h) - self.F(x - h)) / (2 * h)

    def calcProx(self):
        self.b = self.a - (self.F(self.a)/self.dxF_num(self.a))

    def resolve(self):
        try:
            achouRaiz = True
            x = 0
            if not self.ehRaiz(self.a):
                achouRaiz = False

            while not achouRaiz:
                x += 1
                self.calcProx()
                self.a = self.b

                if self.ehRaiz(self.a):
                    achouRaiz = True

            return f'F({op.truncate(self.a, 10)}) = {self.F(self.a)} / encontrado com {x} interacoes'
        except Exception as e:
            return f'ERRO: {e}'

def main():
    # Abre o arquivo in.txt e lê as funções e parâmetros
    with open(os.path.join(dir_path,'in.txt'), 'r') as f:
        linhas = f.readlines()

    # Itera sobre as linhas do arquivo de entrada e executa a bisseção para cada função
    i = 0
    while i < len(linhas):
        f_str = linhas[i].strip()
        toleran = float(linhas[i+1].strip())
        x1 = float(linhas[i+2].strip())

        resultado = NewtonRaphson(f_str, toleran, x1).resolve()
        # Escreve os resultados no arquivo out.txt
        with open(os.path.join(dir_path, 'out.txt'), 'w') as arquivo:
            arquivo.write(f_str + '\n')
            arquivo.write(str(resultado) + '\n\n')

        i += 4  # Incrementa o contador para ler a próxima função

if __name__ == '__main__':
    main()
