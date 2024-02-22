#classes e objetos
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        

    def parar (self):
        print("Parar")

    def correr (self):
        print("Pode correr")

    def buzinar(self):
        print("Pipi...")

    # muito util para fazer representação de classes esse método 
    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave, valor 
        in self.__dict__.items()])}"


bike_1 = Bicicleta("azul", "caloi 10", 1959, 260)
bike_1.buzinar()
bike_1.correr()
bike_1.parar()
print(bike_1.cor, bike_1.modelo, bike_1.valor, bike_1.ano)

bike_2 = Bicicleta("Preto", "speed", 2024, 300)
bike_2.buzinar()
bike_2.correr()
bike_2.parar()
print(bike_2.cor, bike_2.modelo, bike_2.valor, bike_2.ano)
