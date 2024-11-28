class Motor:
    def __init__(self, tipo, potencia): 
        self.tipo = tipo 
        self.potencia = potencia
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            return f'Motor {self.tipo} de {self.potencia} foi ligado'
        return 'O motor já está ligado'

    def desligar(self):
        if self.ligado:
            self.ligado = False
            return f'Motor {self.tipo} de {self.potencia} foi desligado'
        return 'O motor está desligado'


class Carro:
    def __init__(self, marca, motor, num_p):
        self.marca = marca
        self.motor = motor
        self.num_p = num_p

    def abrir_porta(self, porta):
        if 1 <= porta <= self.num_p:
            return f'Porta {porta} do {self.marca} aberta'
        return 'Número de porta inválido'


class Veiculo:
    def __init__(self, marca, motor, ano, velocidade):
        self.marca = marca
        self.motor = motor
        self.ano = ano
        self.__velocidade = velocidade  # Inicializando self.__velocidade

    def mover(self, incremento):
        self.__velocidade += incremento
        print(f'O veículo moveu a {self.__velocidade} km/h')

    def parar(self, decremento):
        self.__velocidade -= decremento
        if self.__velocidade < 0:
            self.__velocidade = 0
        print(f'O veículo parou a {self.__velocidade} km/h')


motor_v6 = Motor("V6", 450)
carro = Carro("Ferrari", motor_v6, 2)
veiculo = Veiculo("Ferrari", motor_v6, 2021, 270)

veiculo.mover(10)
veiculo.parar(10)
print(carro.motor.ligar())      
print(carro.abrir_porta(1))      
print(carro.motor.desligar())
