import sys
import os

# Obtém o diretório atual do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import EncontrarRaizClass
import OperacoesMatematicas as op

class Bisseccao(EncontrarRaizClass.EncontrarRaiz):
    def __init__(self, equacao: str, tolerancia: float, a: float, b: float) -> None:
        super().__init__(equacao, tolerancia, a, b)

    def resolve(self):
        raiz = None
        if self.ehRaiz(self.a):
            raiz = self.a

        if self.ehRaiz(self.b):
            raiz = self.b
        
        if self.F(self.a) * self.F(self.b) > 0:
            return 'ERRO'
        
        x = 0
        c = 0
        while self.erroRelativo() >= self.tolerancia and not raiz:
            x += 1
            c = (self.a + self.b) / 2.0
            
            if self.ehRaiz(c):
                raiz = c
            elif self.F(c) * self.F(self.a) < 0:
                self.b = c
            else:
                self.a = c

        return f'F({op.truncate(raiz, 10)}) = {self.F(raiz)} / encontrado com {x} interacoes'

def main():
    # Limpa o arquivo out.txt
    open(os.path.join(dir_path, 'out.txt'), 'w').close()

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

        resultado = Bisseccao(f_str, toleran, a, b).resolve()
        # Escreve os resultados no arquivo out.txt
        with open(os.path.join(dir_path, 'out.txt'), 'a') as arquivo:
            arquivo.write(f_str + '\n')
            arquivo.write(str(resultado) + '\n\n')

        i += 5  # Incrementa o contador para ler a próxima função

if __name__ == '__main__':
    main()
