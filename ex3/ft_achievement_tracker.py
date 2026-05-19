import random


ACHIEVEMENTS: tuple = (
    "1 / 900",
    "42",
    "Archaeologist",
    "Around the world in 90 seconds",
    "Die hard",
    "From the Hearth to the Moon",
    "Ghosts in the Machine",
    "Hotshot",
    "It belongs in a museum!",
    "Mmmm, Carcinogens",
    "Oof Ouch, My Bones",
    "Pchooooooo!",
    "Space Exploredinaire",
    "Strike!",
    "The Grate Filter",
    "Zip Zoom",
)


def gen_player_achievements() -> set:
    random_number_ach: int = random.randint(1, len(ACHIEVEMENTS))
    choosen_achievements: list = random.sample(ACHIEVEMENTS, random_number_ach)
    return set(choosen_achievements)


if __name__ == "__main__":
    print("=== Achievement tracker ===")
    p1: set = gen_player_achievements()
    p2: set = gen_player_achievements()
    p3: set = gen_player_achievements()
    p4: set = gen_player_achievements()

    players: list = [p1, p2, p3, p4]

    all_achievements = p1.union(p2).union(p3).union(p4)
    print(f"=== All achievements between players: {all_achievements}\n")

    shared = set.intersection(p1, p2, p3, p4)
    if not shared:
        print("=== Common achievements: None")
    else:
        print(f"=== Common achievements: {shared}")

    print("\n=== All uniques achievements per player:")
    i: int = 1
    for player in players:
        others: set = set().union(*(p for p in players if p is not player))

        exclusive: set = set.difference(player, others)
        n_exclusive: int = len(exclusive)

        if not exclusive:
            print(f"* Exclusive {n_exclusive} achievements:"
                  " None")
        else:
            print(f"* Exclusive {n_exclusive} achievements"
                  f" for PLAYER {i}: {exclusive}")
        i += 1

    print("\n=== Missing achievements per player:")
    i = 1
    for player in players:

        missing: set = set.difference(set(ACHIEVEMENTS), player)
        n_missing: int = len(missing)

        if not missing:
            print(f"- Missing {n_missing} achievements:"
                  " None")
        else:
            print(f"- Missing {n_missing} achievements"
                  f" for PLAYER {i}: {missing}")
        i += 1

    print("\nEnd of program")
