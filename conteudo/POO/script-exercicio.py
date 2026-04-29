class Carro: # define a classe
    def __init__(self, marca, modelo, ano, cor): # __init__ é o construtor da classe (executado quando o objeto é criado), e self é a referência ao próprio objeto que será criado)
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        # self.marca, self.modelo, self.ano, self.cor são os atributos da classe

    def acelerar(self):
        print(f"O {self.marca} {self.modelo} está acelerando")

    def frear(self):
        print(f"O {self.marca} {self.modelo} está freando")

    def buzinar(self):
        print(f"O {self.marca} {self.modelo} está buzinando")

    def get_info(self):
        print(f"O {self.modelo} é um {self.marca} de {self.ano} e é da cor {self.cor}") 

carro1 = Carro("Mercedes", "AMG 45", 2020, "Branco") #nome_do_objeto = NomeDaClasse(parametros na ordem que foram definidos no construtor) 
carro2 = Carro("BMW", "M3", 2021, "Preto")

carro1.acelerar()
carro1.frear()
carro1.buzinar()
carro1.get_info()

carro2.acelerar()
carro2.frear()
carro2.buzinar()
carro2.get_info()