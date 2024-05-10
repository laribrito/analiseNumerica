import sys
import os

import sympy as sy

# Obtém o diretório atual do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import AjustPolinClass

class RegressaoLinear(AjustPolinClass.AjustPolin):
    def __init__(self, valoresX: list, valoresY: list) -> None:
        super().__init__(valoresX, valoresY)
    
    def polinomioLagrange(self, index):
        denominador = 1
        strNumerador = ''

        # numerador
        for i in range(self.qtdPares):
            if i != index:
                strNumerador += f'(x - {self.allX[i]}) *'
        strNumerador = strNumerador[:-1] 

        # denominador
        for i in range(self.qtdPares):
            if i != index:
                denominador *= self.allX[index] - self.allX[i]

        return f'({strNumerador})/{denominador}'

    def resolve(self):
        func = ''
        x = sy.Symbol('x')

        for i in range(self.qtdPares):
            func += f'{self.allY[i]}*({self.polinomioLagrange(i)}) +'
        func = func[:-1]

        exp = sy.sympify(func)
        simplificado = sy.expand(exp)

        return f'{simplificado}'

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
