class carro:
    def __init__(self, marca, modelo, placa):
        self.__marca = marca
        self.__modelo = modelo
        self.__placa = placa
        self.__velocidade = 0

    def imprimir(self):
        print(f'Marca: {self.__marca}, modelo: {
              self.__modelo}, placa: {self.__placa}')

    def acelerar(self, incremento):
        self.__velocidade += incremento
        print(f'O carro acelerou para {self.__velocidade} km/h')

    def frear(self, decremento):
        self.__velocidade-=decremento
        if self.__velocidade<0:
            self.__velocidade=0
        print(f'O carro freou para {self.__velocidade} km\h') 

    def set_marca(self, marca):
        self.__marca=marca  

    def get_marca(self):
        return self.__marca     


c = carro('Vw', 'Gol', 'ABC10J10')
c.imprimir()
c.acelerar(50)
c.frear(20)
c.set_marca("FIAT")
print('A nova marca do carro é', c.get_marca())