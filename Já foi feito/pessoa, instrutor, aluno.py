class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass


class Cachorro(Animal):
    def fazer_som(self):
        return (f'{self.nome} diz: Auau')


class Gato(Animal):
    def fazer_som(self):
        return (f'{self.nome} diz: Miau')

dog = Cachorro("Bug")
print(dog.fazer_som())

cat = Gato("Faisca")
print(cat.fazer_som())