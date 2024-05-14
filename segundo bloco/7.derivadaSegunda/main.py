import sys
import os

# Obtém o diretório atual do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import calculoDerivadaClass

class SegundaDerivada(calculoDerivadaClass.CalculoDerivada):
    def __init__(self, valoresX: list, valoresY: list, index, func) -> None:
        super().__init__(valoresX, valoresY, func)
        if not self.validaIndex(index):
            raise Exception('Index escolhido não é válido')
        self.index = index - 1
        
    def validaIndex(self, index):
        if index - 1 >= 1 and index <= len(self.allX) - 1:
            return True
        return False    
    
    def derivadaProgressiva(self, py_mais2, py_mais1, py):
        return (py_mais2 - 2* py_mais1 + py) / (self.h**2)

    def derivadaCentrada(self, py_mais1, py, py_menos1):
        return (py_mais1 - 2* py + py_menos1) / (self.h**2)

    def derivadaRegressiva(self, py, py_menos1, py_mais2):
        return (py - 2* py_menos1 + py_mais2) / (self.h**2)
    
    def getStrResult(self):
        response = f'{self.result}'

        erroEstimado = self.calcErroDiff(2)
        if erroEstimado:
            response += f'\nErro estimado: {erroEstimado}'

        erroPercent = self.calcErroPercent(2)
        if erroPercent:
            response += f'\nErro Percentual: {(SegundaDerivada.pNum(erroPercent))} %'

        return response + '\n'

    def resolve(self):
        index = self.index
        py_mais1 = self.allY[index + 1]
        py = self.allY[index]
        py_menos1 = self.allY[index - 1]
        py_mais2 = self.allY[index + 2]

        response = 'Derivada Centrada: '

        self.result = self.derivadaCentrada(py_mais1, py, py_menos1)
        
        response += self.getStrResult()

        response += '\nDerivada Progressiva: '

        self.result = self.derivadaProgressiva(py_mais2, py_mais1, py)
        
        response += self.getStrResult()

        response += '\nDerivada Regressiva: '

        self.result = self.derivadaRegressiva(py, py_menos1, py_mais2)
        
        response += self.getStrResult()

        return response 

def main():
    # Limpa o arquivo out.txt
    open(os.path.join(dir_path, 'out.txt'), 'w').close()

    # Abre o arquivo in.txt e lê as funções e parâmetros
    with open(os.path.join(dir_path,'in.txt'), 'r') as f:
        linhas = f.readlines()

    # Itera sobre as linhas do arquivo de entrada
    listX = []
    listY = []
    i = 0
    index = 0
    while i < len(linhas):
        n = int(linhas[i])
        i+=1

        for _ in range(n):
            params = linhas[i].split()
            x = params[0]
            y = params[1]

            listX.append(float(x))
            listY.append(float(y))
            i+=1

        index = int(linhas[i])
        i+=1

        func = None
        if len(linhas[i]) > 1:
            func = linhas[i]
            i+=1
                
        try:
            obj = SegundaDerivada(listX, listY, index, func)
            resultado = obj.resolve()
        except Exception as e:
            resultado = f'ERRO: {e}'

        # Escreve os resultados no arquivo out.txt
        with open(os.path.join(dir_path, 'out.txt'), 'a') as arquivo:
            arquivo.write(str(resultado) + '\n\n')

        listX.clear()
        listY.clear()
        i+=1

if __name__ == '__main__':
    main()
