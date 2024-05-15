import sys
import os

import sympy as sp

# Obtém o diretório atual do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import AjustPolinClass

class InterpolacaoNewton(AjustPolinClass.AjustPolin):
    def __init__(self, valoresX: list, valoresY: list, index:int, pathSave:str) -> None:
        super().__init__(valoresX, valoresY, index, pathSave)
    
    def b(self, i:list):
        if len(i) == 1:
            return self.allY[0]
        
        if len(i) == 2:
            return (self.allY[i[0]] - self.allY[i[1]] )/(self.allX[i[0]] - self.allX[i[1]])
        
        return (self.b(i[:-1]) - self.b(i[1:]))/(self.allX[i[0]] - self.allX[i[-1]])


    def polinomioNewton(self):
        f = ''

        for i in range(self.qtdPares):
            f += f'{self.b(list(range(i, -1, -1)))} *'
            for j in range(i):
                f += f'(x - {self.allX[j]}) *'
            
            f = f[:-1]
            f += '+'

        return f[:-1]

    def resolve(self):
        numerador = self.polinomioNewton()
        f = f'{numerador}/({self.allX[0]} - {self.allX[self.qtdPares-1]})'

        exp = sp.sympify(f)
        self.solution = sp.expand(exp)

        return f'{self.solution}'       

def main():
    # Limpa o arquivo out.txt
    open(os.path.join(dir_path, 'out.txt'), 'w').close()

    # Abre o arquivo in.txt e lê as funções e parâmetros
    with open(os.path.join(dir_path,'in.txt'), 'r') as f:
        linhas = f.readlines()

    # Itera sobre as linhas do arquivo de entrada
    listX = []
    listY = []
    index = 0
    for l in linhas:
        try:
            params = l.split()
            x = params[0]
            y = params[1]

            listX.append(float(x))
            listY.append(float(y))
        except:
            index += 1
            obj = InterpolacaoNewton(listX, listY, index, dir_path)
            resultado = obj.resolve()
            obj.plot()
            # Escreve os resultados no arquivo out.txt
            with open(os.path.join(dir_path, 'out.txt'), 'a') as arquivo:
                arquivo.write(str(resultado) + '\n\n')

            listX.clear()
            listY.clear()

if __name__ == '__main__':
    main()
