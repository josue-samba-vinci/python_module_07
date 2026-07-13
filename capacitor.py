from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_creature(healing_factory: HealingCreatureFactory) -> None:
    healing_base_creature = healing_factory.create_base()
    healing_evolved_creature = healing_factory.create_evolved()
    print("Testing Creature with healing capability")
    print(" base")
    print(healing_base_creature.describe())
    print(healing_base_creature.attack())
    print(healing_base_creature.heal())
    print(" evolved")
    print(healing_evolved_creature.describe())
    print(healing_evolved_creature.attack())
    print(healing_evolved_creature.heal())
    print("")


def test_transform_creature(
        transform_factory: TransformCreatureFactory) -> None:
    transforming_base_creature = transform_factory.create_base()
    transforming_evolved_creature = transform_factory.create_evolved()
    print("Testing Creature with transform capability")
    print(" base")
    print(transforming_base_creature.describe())
    print(transforming_base_creature.attack())
    print(transforming_base_creature.transform())
    print(transforming_base_creature.attack())
    print(transforming_base_creature.revert())
    print(" evolved")
    print(transforming_evolved_creature.describe())
    print(transforming_evolved_creature.attack())
    print(transforming_evolved_creature.transform())
    print(transforming_evolved_creature.attack())
    print(transforming_evolved_creature.revert())


def main() -> None:
    test_healing_creature(HealingCreatureFactory())
    test_transform_creature(TransformCreatureFactory())


if __name__ == "__main__":
    main()
