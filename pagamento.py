from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def processar_pagamento(self):
        pass

    def validar_cartao(self):
        return "Pago"

class PagamentoBoleto(Pagamento):
    def __init__(self, valor):
        self.valor = valor

    def valor(self):
        return self.valor

    def processar_pagamento(self):
        return self.valor

    def codigo_de_barras(self):
        return 3 * self.valor

    def gerar_boleto(self):
        return f"Boleto gerado com valor {self.valor}"

class PagamentoCartao(Pagamento):
    def __init__(self, pago):
        self.pago = pago

    def valor(self):
        return self.pago

    def processar_pagamento(self):
        return f"Pagamento de {self.pago} processado"

    def validar_cartao(self):
        return "Cartão validado"

# Corrigindo a instância e chamada de métodos
r = PagamentoBoleto(10)
print(r.processar_pagamento())
print(r.codigo_de_barras())
print(r.gerar_boleto())
