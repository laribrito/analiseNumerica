class ValidaPares:
    def __init__(self, allX:list, allY:list) -> None:
        if ValidaPares.validaPares(allX, allY):
            self.allX = allX
            self.allY = allY
            self.qtdPares = len(allX)

        else:
            raise Exception('Os pares passados como parâmetro estão incompletos')

    def validaPares(allX, allY):
        return len(allX) == len(allY)