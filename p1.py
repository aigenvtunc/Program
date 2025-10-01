class Character:
    def __init__(self,char_class,level,atk,name):
        self.char_class = char_class
        self.level = level
        self.atk = atk
        self.name=name
    def __str__(self):
        return f"{self.char_class}{self.level},{self.atk}"
    def attack(self):
        if self.char_class == "Warrior":
            return f"{self.char_class} dealt {self.level * self.atk} Damage"
        elif self.char_class =="Assasin":
            return f"{self.char_class} dealt {self.level * self.atk} Damage"
        elif self.char_class =="Priest":
            return f"{self.char_class} heals {self.level * self.atk} Hp"
        elif self.char_class =="Mage":
            return f"{self.char_class} dealt {self.level * self.atk} Damage"
        else:
            return f"Unknown"
warrior1 = Character("Warrior",25,10,"Jack")
assasin1 = Character("Assasin",35,15,"Jack")
priest1 = Character("Priest",20,10,"Jack")
mage1 = Character("Mage",37,12,"Jack")

print(warrior1.attack())
print(assasin1.attack())
print(priest1.attack())
print(mage1.attack())






