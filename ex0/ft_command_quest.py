import sys


def ft_command_quest(arg: str, index: int) -> None:
    print(f"Argument {index}: {arg}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    ac: int = len(sys.argv)
    print(f"Program name: {sys.argv[0]}\n")
    print(f"Arguments recieved: {ac - 1}")
    if ac == 1:
        print("No arguments provided!")
    index: int = 1
    for argument in sys.argv[1:]:
        ft_command_quest(argument, index)
        index += 1
    print(f"Total arguments: {ac}")
