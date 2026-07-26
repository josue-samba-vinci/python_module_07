import ex0


def test_factory(factory: ex0.CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print("Testing factory")
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print("")


def test_battle(
        factory1: ex0.CreatureFactory, factory2: ex0.CreatureFactory
        ) -> None:
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()
    print("Testing battle")
    print(creature1.describe())
    print("vs.")
    print(creature2.describe())
    print(" fight!")
    print(creature1.attack())
    print(creature2.attack())


def main() -> None:
    test_factory(ex0.FlameFactory())
    test_factory(ex0.AquaFactory())
    test_battle(ex0.FlameFactory(), ex0.AquaFactory())


if __name__ == "__main__":
    main()
