class car:
    def __init__(self,wheels=4):
        self.wheels = wheels

class gasoline(car):
    def __init__(self,engine='gasoline',tank_cap=20):
        car.__init__(self)
        self.engine = engine
        self.tank_cap = tank_cap
        self.tank = 0
    
    def refuel(self):
        self.tank = self.tank_cap

class electric(car):
    def __init__(self,engine='electric',kwh_cap=60):
        car.__init__(self)
        self.engine = engine
        self.kwh_cap = kwh_cap
        self.kwh = 0
    
    def recharge(self):
        self.kwh = self.kwh_cap

class hybrid(gasoline, electric):
    def __init__(self,engine='Hybrid',tank_cap=11,kWh_cap=5):
        gasoline.__init__(self,engine,tank_cap)
        electric.__init__(self,engine,kWh_cap)
        
        
prius = hybrid()
print(prius.tank)
print(prius.kwh)
print()
prius.recharge()
print(prius.kwh)