import sys
import os

# Obtém o diretório atual do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import interpolacaoClass

class RegressaoLinear(interpolacaoClass.Interpolacao):
    def __init__(self, valoresX: list, valoresY: list) -> None:
        super().__init__(valoresX, valoresY)

    def resolve(self):
        x = 0
        y = 0
        x_y = 0
        x_2 = 0

        x = sum(self.allX)
        y = sum(self.allY)
        for i in range (self.qtdPares):
            x_y += self.allX[i] * self.allY[i]
            x_2 += self.allX[i]**2

        b = (self.qtdPares*x_y-x*y)/(self.qtdPares*x_2-x**2)
        a = (y-b*x)/self.qtdPares
        b = round(b, 4)
        a = round(a, 4)

        labelA = ''
        if a > 0:
            labelA = f'+ {a}'
        elif a!=0:
            labelA = f'- {abs(a)}'

        return f'y = {b}x {labelA}'

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
            resultado = RegressaoLinear(listX, listY).resolve()
            # Escreve os resultados no arquivo out.txt
            with open(os.path.join(dir_path, 'out.txt'), 'a') as arquivo:
                arquivo.write(str(resultado) + '\n\n')

            listX.clear()
            listY.clear()

if __name__ == '__main__':
    main()
