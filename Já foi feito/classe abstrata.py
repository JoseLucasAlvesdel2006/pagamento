class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            return (f'Motor {self.tipo} de {self.potencia} foi ligado')
        return ('o Motor já está ligado')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            return (f'Motor {self.tipo} de {self.potencia} foi desligado')
        return (f'O motor está desligado')


class Carro:
    def __init__(self, marca, motor, num_p):
        self.marca = marca
        self.motor = motor
        self.num_p = num_p

    def abrir_porta(self, porta):
        if 1 <= porta <= self.num_p:
            return (f'Porta{porta} do {self.marca} aberta')
        return ('Número de porta invalido')


motor_v6 = Motor("V6", 450)
carro = Carro("BMW", motor_v6, 2)
print(carro.motor.ligar())