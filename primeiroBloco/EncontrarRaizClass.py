import math

class EncontrarRaiz:
    def __init__(self, equacao:str, tolerancia:float, a:float, b:float) -> None:
        self.eq = equacao
        eq = equacao.split('=')
        self.eq_a_esquerda = self.eq_a_direita = None
        if len(eq) == 2:
            self.eq_a_esquerda = eq[0]
            self.eq_a_direita = eq[1]
        self.tolerancia = tolerancia
        self.a = a
        self.b = b
    
    def _funcao_esquerda(self, x):
        return eval(self.eq_a_esquerda)

    def _funcao_direita(self, x):
        return eval(self.eq_a_direita)

    # método que representa a equação
    def F(self, x):
        if self.eq_a_direita and self.eq_a_esquerda:
            return self._funcao_esquerda(x) - self._funcao_direita(x)
        return eval(self.eq)

    def erroAbs(self):
        return abs(self.b - self.a)
    
    def erroRelativo(self):
        return abs(self.b - self.a/self.a)
    
    def ehRaiz(self, c):
        return abs(self.F(c)) <= self.tolerancia
    
    def resolve(self):
        raise NotImplementedError("Deve implementar o método resolve() de acordo com a estratégia devida")