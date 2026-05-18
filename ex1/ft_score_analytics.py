import sys


def convert_to_int(args: list) -> list:
    scores_list: list = []
    score: int
    for arg in args:
        try:
            score = int(arg)
            scores_list.append(score)
        except ValueError:
            print(f"Invalid argument: '{arg}'"
                  "is not a numerical value\n")
    return scores_list


def ft_score_analytics(cleaned_args: list, players: int) -> None:
    scores_list: list
    try:
        scores_list = convert_to_int(cleaned_args)
    except ValueError as error:
        print(f"Error: {error}")
        return
    print(f"Number of players: {players}")
    print(f"Scores: {scores_list}")
    print(f"Min score: {min(scores_list)}")
    print(f"Max score: {max(scores_list)}")
    print(f"Total score: {sum(scores_list)}")
    print(f"Average score: {sum(scores_list) / players}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ac: int = len(sys.argv)
    args: list = sys.argv
    cleaned_args: list = args[1:]
    print(f"Program name: {sys.argv[0]}")
    if ac == 1:
        print("No arguments provided! Usage: "
              "/python3 <score 1> <score 2> ... <score n>")
    else:
        ft_score_analytics(cleaned_args, (ac - 1))
    print(f"Total arguments: {ac}")
