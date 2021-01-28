
from typing import List
from termcolor import colored


def hanoi(start: List[int], end: List[int], temp: List[int], n: int) -> None:
    if n == 1:
        end.append(start.pop())
    else:
        hanoi(start, temp, end, n - 1)
        hanoi(start, end, temp, 1)
        hanoi(temp, end, start, n - 1)


if __name__ == "__main__":
    num_discs: int = 3
    tower_a: List[int] = []
    tower_b: List[int] = []
    tower_c: List[int] = []
    for i in range(1, num_discs+1):
        tower_a.append(i)
    print(
        f"Before => tower_a: {tower_a}, tower_b: {tower_b}, tower_c: {tower_c}")

    hanoi(start=tower_a, end=tower_c, temp=tower_b, n=num_discs)

    print(
        colored(f"After => tower_a: {tower_a}, tower_b: {tower_b}, tower_c: {tower_c}", "green")
    )
