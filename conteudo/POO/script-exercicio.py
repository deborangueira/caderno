# CONCEITOS BASICOS

class Veiculo: # define a classe
    def __init__(self, marca, modelo, ano, cor): # __init__ é o construtor da classe (executado quando o objeto é criado), e self é a referência ao próprio objeto que será criado)
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        # self.marca, self.modelo, self.ano, self.cor são os atributos da classe

    def mover(self):
        print(f"O veículo está se movendo")

    def get_info(self):
        print(f"{self.modelo} é um {self.marca} {self.cor} de {self.ano}") 

# HERANÇA 

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor, cavalos):
        super().__init__(marca, modelo, ano, cor) # atributos herdados da classe Veiculo
        self.cavalos = cavalos # atributo adicional, exclusivo da classe Carro
    def mover(self):
        print(f"O carro {self.modelo} está se movendo") # override do método mover da classe Veiculo adaptado para a classe Carro

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cor, cilindrada):
        super().__init__(marca, modelo, ano, cor)
        self.cilindrada = cilindrada
    def mover(self):
        print(f"A moto {self.modelo} está se movendo") # override do método mover da classe Veiculo adaptado para a classe Moto

carro1 = Carro("Mercedes", "AMG 45", 2020, "Branco", 400) #nome_do_objeto = NomeDaClasse(parametros na ordem que foram definidos no construtor) 
carro2 = Carro("BMW", "M3", 2021, "Preto", 10000)
moto1 = Moto("Honda", "CBR 1000RR", 2020, "Vermelha", 1000)
moto2 = Moto("Yamaha", "YZF R1", 2021, "Azul", 1000)

veiculos = [carro1, moto1, moto2, carro2]

for veiculo in veiculos:
    veiculo.get_info()
    veiculo.mover()

# ENCAPSULAMENTO -> quando a classe vira responsável por PROTEGER seus próprios dados. Isso é feito com o uso de atributos privados (__preco) e o uso de getters e setters. Sem isso o código pode apresentar inconsistência e comportamento imprevisível pois diferentes partes do codigo poderiam alterar o valor de um atributo de forma independente e sem controle. A classe nesse sentido se torna a "fonte de verdade" para os dados. Isso contribui para o conceito de Domain Driven Design com POO que foca em representar regras de negócio (fluxos, dados, comportamentos) em objetos de software, não apenas tabelas de banco de dados. Ela utiliza entidades, agregados e value objects para encapsular regras próximo aos dados, evitando modelos anêmicos e promovendo a coesão no sistema.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco # __preco é um atributo privado (não pode ser acessado fora da classe)

    def get_preco(self): # Getter, método para acessar o atributo privado
        return self.__preco

    def set_preco(self, preco): # Setter, método para alterar o atributo privado
        if preco > 0:
            self.__preco = preco
        else:
            print("O preço deve ser maior que 0")

produto1 = Produto("Camiseta", 100)
print(produto1.get_preco())
produto1.set_preco(200)
print(produto1.get_preco())