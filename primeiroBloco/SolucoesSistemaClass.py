class SolucoesSistema:
    tolerance = 1e-6

    def __init__(self, matriz) -> None:
        if not self.ehMatrizValida(matriz):
            raise Exception('Essa matriz não é quadrada ou o vetor B não foi passado')
        
        self.M, self.B = self.separarMatriz(matriz)
        self.k = len(matriz)
        self.solution = None

    def MatrizParaStr(matriz):
        cols = len(matriz)
        rows = len(matriz[0])

        txt = ''
        for i in range(rows):
            txt+='['
            for j in range(cols):
                txt+=f'{matriz[i][j]:4.5f}, '
            txt=txt[:-2]
            txt+=']\n'
        return txt[:-1]
    
    def variacaoAbs(self, a:list, b:list):
        for ax, bx in zip(a, b):
            if abs(ax - bx) > SolucoesSistema.tolerance:
                return False
        return True

    def variacaoRel(self, a:list, b:list):
        maxVar = max(a)
        for ax, bx in zip(a, b):
            if abs((ax - bx)/maxVar) > SolucoesSistema.tolerance:
                return False
        return True

    def vetorParaStr(v, sep=' '):
        lista_de_strings = [str(numero) for numero in v]
        string = sep.join(lista_de_strings)
        return string

    def test(self):
        if self.solution:
            for n, linha, esperado in zip(range(self.k), self.M, self.B):
                result = 0
                for sol, lin in zip(self.solution, linha):
                    result += sol * lin


                delta = abs(result - esperado)
                delta2 = abs(delta - SolucoesSistema.tolerance)
                
                txtExtra = f'x({n+1}) esperava {esperado} mas foi calculado como {result}'

                if delta2>SolucoesSistema.tolerance:
                    return f'{txtExtra}\nO vetor encontrado não pode ser considerado solução'

                if delta>SolucoesSistema.tolerance:
                    return 'O vetor encontrado está bem próximo da solução'
            return 'O vetor encontrado é uma solução é suficientemente boa'
            
        return 'Não há solução'

    def separarMatriz(self, matriz):
        m = []
        vetorF = []
        for linha in matriz:
            m.append(linha[:-1])
            vetorF.append(linha[-1])

        return m, vetorF

    def ehMatrizValida(self, matriz):
        qtdLinhas = len(matriz)
        for i in matriz:
            if len(i) != qtdLinhas + 1:
                return False
        
        return True
    
    def resolve(self):
        raise NotImplementedError("Deve implementar o método resolve() de acordo com a estratégia devida")
                
