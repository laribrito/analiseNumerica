import sys
import os

# Obtém o diretório atual do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Adiciona o diretório extra do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '9.trapezioComposto')))

import calculoAreaClass
from main9 import TrapezioComposto

class ExtrapolacaoRichards(calculoAreaClass.CalculosErros):
    def __init__(self, sol1: calculoAreaClass.CalculoIntegral, sol2: calculoAreaClass.CalculoIntegral, func) -> None:
        self.sol1 = sol1
        self.sol2 = sol2
        if self.validaIntervalo():
            super().__init__(self.sol1.allX, func)
            sol1.resolve()
            sol2.resolve()
    
    def validaIntervalo(self):
        if self.sol1.allX[0] != self.sol2.allX[0] or \
           self.sol1.allX[-1] != self.sol2.allX[-1]:
            raise Exception('O intervalo calculado tem que ser o mesmo')
        return True

    def resolve(self):
        h1 = self.sol1.h
        result1 = self.sol1.result

        h2 = self.sol2.h
        result2 = self.sol2.result

        self.result = result2 + (1 / ((h1 / h2) * (h1 / h2) - 1)) * (result2 - result1)

        response = f'{self.result}'

        erroEstimado = self.calcErroDiff()

        if erroEstimado:
            response += f'\nErro estimado: {erroEstimado}'

        erroPercent = self.calcErroPercent()

        if erroPercent:
            response += f'\nErro Percentual: {(calculoAreaClass.CalculoIntegral.pNum(erroPercent))} %'

        return response     

def main():
    # Limpa o arquivo out.txt
    open(os.path.join(dir_path, 'out.txt'), 'w').close()

    # Abre o arquivo in.txt e lê as funções e parâmetros
    with open(os.path.join(dir_path,'in.txt'), 'r') as f:
        linhas = f.readlines()

    # Itera sobre as linhas do arquivo de entrada
    listX = [[], []]
    listY = [[], []]
    i = -1
    while i < len(linhas)-1:
        for j in range(2):
            i+=1
            n = int(linhas[i])
            i+=1

            for _ in range(n):
                params = linhas[i].split()
                x = params[0]
                y = params[1]

                listX[j].append(float(x))
                listY[j].append(float(y))
                i+=1
            
        
        func = None
        if len(linhas[i]) > 1:
            func = linhas[i]
            i+=1
                
        res1 = TrapezioComposto(listX[0], listY[0], None)
        res2 = TrapezioComposto(listX[1], listY[1], None)

        try:
            obj = ExtrapolacaoRichards(res1, res2, func)
            resultado = obj.resolve()
        except Exception as e:
            resultado = f'ERRO: {e}'

        # Escreve os resultados no arquivo out.txt
        with open(os.path.join(dir_path, 'out.txt'), 'a') as arquivo:
            arquivo.write(str(resultado) + '\n\n')

        listX = [[], []]
        listY = [[], []]

if __name__ == '__main__':
    main()
