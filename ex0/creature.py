from ABC import abc, abstractmethod

class Creature(ABC):
    
    def __init__(self, name_creature: str, type_creature: str):
        self.name_creature = name_creature
        self.type_creature = type_creature

    @abstractmethod
    def attack(self) -> str
        pass

    def describe(self) -> str
        print(f"{self.name_creature} is a {self.type_creature} type Creature")

class Flameling(Creature)

    def __init__(self, name_creature: str, type_creature: str):
        super.__init__(name_creature, type_creature)

    def attack(self) -> str
        print(f"{self.name_creature} uses Ember!")

class Pyrodon(Creature)

    def __init__(self, name_creature: str, type_creature: str):
        super.__init__(name_creature, type_creature)

    def attack(self) -> str
        print(f"{self.name_creature} uses Flamethrower!")

class Aquabub(Creature)

    def __init__(self, name_creature: str, type_creature: str):
         super.__init__(name_creature, type_creature)

    def attack(self) -> str
         print(f"{self.name_creature} uses Water Gun!")

class Torragon(Creature)

    def __init__(self, name_creature: str, type_creature: str):
         super.__init__(name_creature, type_creature)

    def attack(self) -> str
         print(f"{self.name_creature} uses Hydro Pump!")

