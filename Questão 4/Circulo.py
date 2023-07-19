from Forma import Forma

class Circulo(Forma):
    def __init__(self, tipo, descricao, raio):
        super().__init__(tipo, descricao)
        self.raio = raio

    def calc_area(self):
        area = 3.14*(self.raio**2)
        return area

    def calc_perimetro(self):
        perimetro = 2*3.14*self.raio
        return perimetro
    