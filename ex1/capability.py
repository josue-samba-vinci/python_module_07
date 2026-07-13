from abc import ABC, abstractmethod
from ex0.creature import CreatureFactory, Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.isTranformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class HealingCreature(Creature, HealCapability, ABC):
    pass


class TransformingCreature(Creature, TransformCapability, ABC):
    pass


class Sproutling(HealingCreature):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(HealingCreature):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> HealingCreature:
        return Sproutling()

    def create_evolved(self) -> HealingCreature:
        return Bloomelle()


class Shiftling(TransformingCreature):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.isTranformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.isTranformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.isTranformed = False
        return f"{self.name} returns to normal."


class Morphagon(TransformingCreature):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.isTranformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.isTranformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.isTranformed = False
        return f"{self.name} stabilizes its form."


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> TransformingCreature:
        return Shiftling()

    def create_evolved(self) -> TransformingCreature:
        return Morphagon()
