# Adding type hints with variable length parameters of different types
def greet_typing(*params: tuple[str, str, int]) -> None:
    for param in params:
        print(f"Parameter : {param}")


# Example usage:
greet_typing("Alice", "Bob", 25, "Charlie", "David", 30)


def greet_typing_2(*params: str) -> None:
    for param in params:
        print(f"Parameter : {param}")


greet_typing_2(25, 26)
