class Character:
    def __init__(self,level,atk,defence,name):
        self.level=level
        self.atk=atk
        self.defence=defence
        self.name = name
    def __str__(self):
        return f"{self.level}-{self.name}"
    def greet(self,name):
        return f"{self.name} salutes you {name}!"
    
    
class Warrior(Character):
    def __init__(self,level,atk,defence,name):
        super().__init__(level,atk,defence,name)
    def attack(self):
        return f"{self.name} slashed with {self.level * self.atk} damage"
class Assasin(Character):
    def __init__(self,level,atk,defence,name):
        super().__init__(level,atk,defence,name)
    def attack(self):
        return f"{self.name} cuts {self.level*self.atk} damage"
class Priest(Character):
    def __init__(self,level,atk,defence,name):
        super().__init__(level,atk,defence,name)
    def attack(self):
        return f"{self.name} attacks with {self.level*self.atk} damage"
class Mage(Character):
    def __init__(self,level,atk,defence,name):
        super().__init__(level,atk,defence,name)
    def attack(self):
        return f"{self.name} blazes with {self.level*self.atk} damage"

warrior = Warrior(100,10,20,"Jack")
assasin = Assasin(35,15,10,"Ezio")
priest = Priest(50,12,15,"Leona")
mage = Mage(75,20,12,"Vlad")
print(warrior.name)
print(warrior.greet("Vlad"))
print(warrior)
print(warrior.attack())
