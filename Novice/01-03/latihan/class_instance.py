class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    #buat array kosong untuk setiap trick anjing

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over') #tambah trik untuk fido
e.add_trick('play dead') #tambah trik untuk buddy
print(d.tricks)
print(e.tricks)