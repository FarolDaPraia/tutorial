class MostrarValores():
    def show(self):
        print('este é o valor')

class Adicionar():
    def add(self, mostrar):
        print(1 + 1)
        mostrar.show()

d = MostrarValores()
# d.show()

e = Adicionar()
e.add(d)
