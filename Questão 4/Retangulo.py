from Forma import Forma

class Retangulo(Forma):
    def __init__(self, tipo, descricao, lado1, lado2):
        super().__init__(tipo, descricao)
        self.lado1 = lado1
        self.lado2 = lado2

    def calc_area(self):
        area = self.lado1*self.lado2
        return area

    def calc_perimetro(self):
        perimetro = 2*(self.lado1 + self.lado2)
        return perimetro
