import pickle

class my_zen_class:
    number_of_meditations = 0 

    def __init__(self,name):
        self.number_of_meditations = 0
        self.name = name
    
    def meditate(self):
        self.number_of_meditations = self.number_of_meditations + 1

    def __getstate__(self):
        state = self.__dict__.copy()

        del state['number_of_meditations']

        return state
    
    def __setstate__(self, state):
        self.__dict__.update(state)

my_zen_object = my_zen_class("dave")
for i in range(100):
    my_zen_object.meditate()

print(str.format("iam {0}, and i have meditated {1} times", my_zen_object.name, my_zen_object.number_of_meditations))
my_pickled_zen_object = pickle.dumps(my_zen_object)
my_zen_object = None

my_new_zen_object = pickle.loads(my_pickled_zen_object)

print(str.format("iam {0}, and i dont have a beginner mind yet because i have meditated only {1} times",my_new_zen_object.name, my_new_zen_object.number_of_meditations))