import random


PLAYERS: tuple = (
    "Jopaz-su",
    "Alegalve",
    "Aruisnav",
    "jorpere2",
    "parenas-",
    "lodazan",
    "Arogarc",
    "gapostig"
)


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    all_players: list = list(PLAYERS)
    print(f"Initial list of players: {all_players}\n")
    capitalized: list = [name for name in PLAYERS if name[0].isupper()]
    print(f"Players with first letter in uppercase: {capitalized}\n")
    minus: list = [name for name in PLAYERS if name[0].islower()]
    print(f"Players with first letter in lowercase: {minus}\n")
    scores: dict[str, int] = {name: random.randint(0, 1000)
                              for name in capitalized}
    print(f"Players with random scores: {scores}\n")
    total: int = sum(scores.values())
    players_capitalized: int = len(scores)
    avg: float = round((total / players_capitalized), 2)
    print(f"Average score: {avg}")
    high_scores: dict[str, int] = {name: value for name, value in
                                   scores.items() if value > avg}
    print(f"High scores: {high_scores}")
    print("\nEnd of program")
