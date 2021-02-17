from typing import Iterable, List, TypeVar
from shared.comparable import Comparable

C = TypeVar("C", bound="Comparable")


def linear_contains(it: Iterable[C], key: C) -> bool:
    for i in it:
        if i == key:
            return True
    return False


def test_linear_contains() -> None:
    nums = [1, 2, 3, 4, 5]
    key = 3
    assert linear_contains(nums, key) == True, f"{nums} should contain {key}"
