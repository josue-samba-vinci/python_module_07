from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, InvalidStrategyError
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle(
          opponents: list[tuple[CreatureFactory, BattleStrategy]]
          ) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print("")
    try:
        for i in range(len(opponents)):
            for j in range(i+1, len(opponents)):
                factory_1, strategy_1 = opponents[i]
                factory_2, strategy_2 = opponents[j]
                creature_1 = factory_1.create_base()
                creature_2 = factory_2.create_base()
                print("* Battle *")
                print(creature_1.describe())
                print(" vs.")
                print(creature_2.describe())
                print(" now fight!")
                strategy_1.act(creature_1)
                strategy_2.act(creature_2)
    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
        ])
    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ])
    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ])


if __name__ == "__main__":
    main()
