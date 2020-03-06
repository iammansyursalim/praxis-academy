class animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("subsclass must implement abstract method")

class dog(animal):
    def speak(self):
        return self.name+' says wolf'

class cat(animal):
    def speak(self):
        return self.name+' says cat'

fido = dog('fido')
haha = cat('haha')

print(fido.speak())
print(haha.speak())