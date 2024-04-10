class SolucoesSistema:
    def __init__(self, matriz) -> None:
        if not self.ehMatrizValida(matriz):
            raise Exception('Essa matriz não é quadrada ou o vetor B não foi passado')
        
        self.M, self.B = self.separarMatriz(matriz)
        self.k = len(matriz)

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
                
