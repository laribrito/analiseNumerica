import sympy as sp
import sys
import os

# Obtém o diretório atual do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import EncontrarRaizClass
import OperacoesMatematicas as op

class Secante(EncontrarRaizClass.EncontrarRaiz):
    def __init__(self, equacao: str, tolerancia: float, x_k_menos_1: float, x_k: float) -> None:
        super().__init__(equacao, tolerancia, x_k_menos_1, x_k)
        self.x_k_mais_1 = None

    def calcProx(self):
        Fa = self.F(self.a)
        Fb = self.F(self.b)
        self.x_k_mais_1 = (self.a*Fb - self.b * Fa)/(Fb - Fa)

    def proxInt(self):
        self.a = self.b
        self.b = self.x_k_mais_1

    def resolve(self):
        try:
            raiz = None
            x = 0
            if self.ehRaiz(self.a):
                raiz = self.a
            
            elif self.ehRaiz(self.b):
                raiz = self.b

            while not raiz:
                x += 1
                self.calcProx()

                if self.ehRaiz(self.x_k_mais_1):
                    raiz = self.x_k_mais_1
                
                self.proxInt()

            return f'F({op.truncate(raiz, 10)}) = {self.F(raiz)} / encontrado com {x} interacoes'
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
        x_k_menos_1 = float(linhas[i+2].strip())
        x_k = float(linhas[i+3].strip())

        resultado = Secante(f_str, toleran, x_k_menos_1, x_k).resolve()
        # Escreve os resultados no arquivo out.txt
        with open(os.path.join(dir_path, 'out.txt'), 'w') as arquivo:
            arquivo.write(f_str + '\n')
            arquivo.write(str(resultado) + '\n\n')

        i += 5  # Incrementa o contador para ler a próxima função

if __name__ == '__main__':
    main()
