class Bicicleta:
    def __init__(self, marca, ano, cor):
        print("iniciando a classe...")
        self.marca = marca
        self.ano = ano
        self.cor = cor

    def __del__(self):
        print("Removendo a instâcia da classe")   
    
    def correr(self):
        print("correr...")    

bike = Bicicleta("honda", 2024, "azul")
bike.correr()