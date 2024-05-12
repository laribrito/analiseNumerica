import sys
import os

# Obtém o diretório atual do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import calculoAreaClass

class TrapezioSimples(calculoAreaClass.CalculoIntegral):
    def __init__(self, valoresX: list, valoresY: list, func) -> None:
        super().__init__(valoresX, valoresY, func)

    def resolve(self):
        a = self.allX[0]
        b = self.allX[1]
        fa = self.allY[0]
        fb = self.allY[1]

        self.result = (b-a)*((fa+fb)/2)

        response = f'{self.result}'

        erroEstimado = self.calcErroDiff()

        if erroEstimado:
            response += f'\nErro estimado: {erroEstimado}'

        erroPercent = self.calcErroPercent()

        if erroPercent:
            response += f'\nErro Percentual: {(TrapezioSimples.pNum(erroPercent))} %'

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
    while i < len(linhas):
        for _ in range(2):
            params = linhas[i].split()
            x = params[0]
            y = params[1]

            listX.append(float(x))
            listY.append(float(y))
            i+=1
        
        func = None
        if len(linhas[i]) > 1:
            func = linhas[i]
            i+=1
                
        try:
            obj = TrapezioSimples(listX, listY, func)
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
