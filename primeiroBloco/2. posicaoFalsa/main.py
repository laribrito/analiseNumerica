import sys
import os

# Obtém o diretório atual do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import EncontrarRaizClass
import OperacoesMatematicas as op

class PosicaoFalsa(EncontrarRaizClass.EncontrarRaiz):
    def __init__(self, equacao: str, tolerancia: float, a: float, b: float) -> None:
        super().__init__(equacao, tolerancia, a, b)

    def resolve(self):
        if self.F(self.a) * self.F(self.b) > 0:
            return 'ERRO'
        
        x = 0
        c = 0
        achouRaiz = False
        while self.erroAbs() >= self.tolerancia and not achouRaiz:
            x += 1
            Fa = self.F(self.a)
            Fb = self.F(self.b)
            c = (self.a*Fb - self.b * Fa)/(Fb - Fa)

            # print(self.eq)
            # print('a - b - f(a) - f(b) - b-a - (b-a)/a - c - f(c)')
            # print(f'{self.a:.6f} - {self.b:.6f} - {self.F(self.a):.6f} - {self.F(self.b):.6f} - {self.erroAbs():.6f} - {self.erroRelativo():.6f} - {c:.6f} - {self.F(c):.6f}')
            # print()

            if self.ehRaiz(c):
                achouRaiz = True
            elif self.F(c) * self.F(self.a) < 0:
                self.b = c
            else:
                self.a = c

        return f'F({op.truncate(c, 10)}) = {self.F(c)} / encontrado com {x} interacoes'

def main():
    # Abre o arquivo in.txt e lê as funções e parâmetros
    with open(os.path.join(dir_path,'in.txt'), 'r') as f:
        linhas = f.readlines()

    # Itera sobre as linhas do arquivo de entrada e executa a bisseção para cada função
    i = 0
    while i < len(linhas):
        f_str = linhas[i].strip()
        toleran = float(linhas[i+1].strip())
        a = float(linhas[i+2].strip())
        b = float(linhas[i+3].strip())

        resultado = PosicaoFalsa(f_str, toleran, a, b).resolve()
        # Escreve os resultados no arquivo out.txt
        with open(os.path.join(dir_path, 'out.txt'), 'w') as arquivo:
            arquivo.write(f_str + '\n')
            arquivo.write(str(resultado) + '\n\n')

        i += 5  # Incrementa o contador para ler a próxima função

if __name__ == '__main__':
    main()
