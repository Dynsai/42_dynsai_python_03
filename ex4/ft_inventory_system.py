import sys


class DuplicatedItem(Exception):
    def __init__(self, message: str = "Duplicated item. Discarding") -> None:
        super().__init__(message)


class NotAnItem(Exception):
    def __init__(self, message: str = "Not an item. Discarding") -> None:
        super().__init__(message)


ITEMS: tuple = (
    "sword",
    "staff",
    "spear",
    "book",
    "sling",
    "bow",
    "helmet",
    "wand",
    "super-mega-ultra-duper-doom-creator"
)


def inventory_logic(inventory: dict) -> None:
    if not inventory:
        print("=  Inventory is empty")
    else:
        print(f"Tu inventario es: {inventory}\n")
    t_key: int = len(inventory.keys())
    t_value: int = sum(inventory.values())
    print(f"Total quantity of the {t_key} items: {t_value}")
    total: int = sum(inventory.values())
    for item, qty in inventory.items():
        percentaje: int = qty / total * 100
        print(f"Item {item} representes"
              f" {percentaje:.1f}%")
    most_item, most_qty = max(inventory.items(), key=lambda x: x[1])
    least_item, least_qty = min(inventory.items(), key=lambda x: x[1])
    print(f"Most abundant item is {most_item} with {most_qty}")
    print(f"Least abundant item is {least_item} with {least_qty}")


def parsing_arguments(argument: str, inventory: dict) -> dict:
    name: str
    qty_s: str
    if ":" not in argument:
        raise ValueError("Missing ':' value")
    name, qty_s = argument.split(":", 1)
    if name not in ITEMS:
        raise NotAnItem(f"'{name}' is not a valid item")
    if not qty_s.isdigit():
        raise ValueError(f"Quantity error. {qty_s} is not numerical")
    qty: int = int(qty_s)
    if name in inventory:
        raise DuplicatedItem()
    print(f"Adding {qty} {name} to inventory")
    inventory.update({name: qty})
    return inventory


def dictionary_arguments(arguments: list) -> None:
    inventory: dict[str, int] = {}
    for arg in arguments:
        try:
            inventory = parsing_arguments(arg, inventory)
        except (Exception, DuplicatedItem, NotAnItem, ValueError) as e:
            print(f"*  Error: {e}")
    inventory_logic(inventory)
    new_item: str = input("\n===  Introduce new item: ")
    try:
        parsing_arguments(new_item, inventory)
    except (Exception, DuplicatedItem, NotAnItem, ValueError) as e:
        print(f"*  Error: {e}")
    print(f"{inventory}")


if __name__ == "__main__":
    print("===  Inventory System Analysis  ===")
    print("=  Inventory is empty")
    ac: int = len(sys.argv)
    if ac == 1:
        print("Input can't be blank. Input items with format"
              "'item:quantity' pls")
    else:
        dictionary_arguments(sys.argv[1:])
    print("\nEnd of program")
