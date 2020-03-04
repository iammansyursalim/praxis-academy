class person():
    def __init__(self,name):
        self.name = name
    
    def coba_hai(self):
        print('hello world',self.name)

p = person('oke')
p.coba_hai()