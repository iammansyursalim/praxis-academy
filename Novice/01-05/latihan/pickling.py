import pickle

class animal:
    def __init__(self,number_of_paws,color):
        self.number_f_paws = number_of_paws
        self.color = color
    
class sheep(animal):
    def __init__(self,color):
        animal.__init__(self,4,color)

mary = sheep("white")

print(str.format("my sheep mary is {0} and has {1} paws",mary.color,mary.number_f_paws))
my_picked_mary = pickle.dumps(mary)

print("would you like to see her pickled ? here she is")
print (my_picked_mary)

####################################

binary_file = open('my_pickled_mary.bin', mode='wb')
my_picked_mary = pickle.dump(mary, binary_file)
binary_file.close()