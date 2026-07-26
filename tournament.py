import ex0
import ex1
import ex2


def battle(
          opponents: list[tuple[ex0.CreatureFactory, ex2.BattleStrategy]]
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
                print()
                print("* Battle *")
                print(creature_1.describe())
                print(" vs.")
                print(creature_2.describe())
                print(" now fight!")
                strategy_1.act(creature_1)
                strategy_2.act(creature_2)
    except ex2.InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (ex0.FlameFactory(), ex2.NormalStrategy()),
        (ex1.HealingCreatureFactory(), ex2.DefensiveStrategy())
        ])
    print()
    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (ex0.FlameFactory(), ex2.AggressiveStrategy()),
        (ex1.HealingCreatureFactory(), ex2.DefensiveStrategy())
    ])
    print()
    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (ex0.AquaFactory(), ex2.NormalStrategy()),
        (ex1.HealingCreatureFactory(), ex2.DefensiveStrategy()),
        (ex1.TransformCreatureFactory(), ex2.AggressiveStrategy())
    ])


if __name__ == "__main__":
    main()
