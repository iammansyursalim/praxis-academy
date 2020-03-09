from collections import namedtuple
verbTenses = namedtuple('verbtenses', ['past','present','future'])
print(verbTenses)

print()

class verbTenses(object):
    def __init__(self,past,present,future):
        self.past = past
        self.present = present
        self.future = future

print()

class Bus(object):
     passengers = set()
     def add_passenger(self, person):
        self.passengers.add(person)

bus1 = Bus()
bus2 = Bus()
bus1.add_passenger('abe')
bus2.add_passenger('bertha')
print(bus1.passengers)  # returns ['abe', 'bertha']
print(bus2.passengers)  # also ['abe', 'bertha']