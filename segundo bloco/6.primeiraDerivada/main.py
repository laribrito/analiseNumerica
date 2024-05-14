import sys
import os

# Obtém o diretório atual do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import calculoDerivadaClass

class PrimeiraDerivada(calculoDerivadaClass.CalculoDerivada):
    def __init__(self, valoresX: list, valoresY: list, index, func) -> None:
        super().__init__(valoresX, valoresY, func)
        if not self.validaIndex(index):
            raise Exception('Index escolhido não é válido')
        self.index = index - 1
        
    def validaIndex(self, index):
        if index - 1 >= 1 and index <= len(self.allX):
            return True
        return False    
    
    def derivadaCentrada(self, py_mais1, py_menos1, px, px_menos1):
        return (py_mais1 - py_menos1) / (2 * (px - px_menos1))

    def derivadaProgressiva(self, py_mais1, py, px, px_menos1):
        return (py_mais1 - py) / (px - px_menos1)

    def derivadaRetardada(self, py, py_menos1, px, px_menos1):
        return (py - py_menos1) / (px - px_menos1)
    
    def getStrResult(self):
        response = f'{self.result}'

        erroEstimado = self.calcErroDiff()
        if erroEstimado:
            response += f'\nErro estimado: {erroEstimado}'

        erroPercent = self.calcErroPercent()
        if erroPercent:
            response += f'\nErro Percentual: {(PrimeiraDerivada.pNum(erroPercent))} %'

        return response + '\n'

    def resolve(self):
        index = self.index
        py_mais1 = self.allY[index + 1]
        py = self.allY[index]
        py_menos1 = self.allY[index - 1]
        px = self.allX[index]
        px_menos1 = self.allX[index-1]

        response = 'Derivada Centrada: '

        self.result = self.derivadaCentrada(py_mais1, py_menos1, px, px_menos1)
        
        response += self.getStrResult()

        response += '\nDerivada Progressiva: '

        self.result = self.derivadaProgressiva(py_mais1, py, px, px_menos1)
        
        response += self.getStrResult()

        response += '\nDerivada Retardada: '

        self.result = self.derivadaRetardada(py, py_menos1, px, px_menos1)
        
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
        
        func = None
        if len(linhas[i]) > 1:
            i+=1
            func = linhas[i]
            i+=1
                
        try:
            obj = PrimeiraDerivada(listX, listY, index, func)
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
