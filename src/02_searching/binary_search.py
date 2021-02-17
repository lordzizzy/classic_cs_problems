from typing import Sequence, TypeVar

from shared.comparable import Comparable

C = TypeVar("C", bound="Comparable")


def binary_contains(seq: Sequence[C], key: C) -> bool:
    low = 0
    high = len(seq) - 1
    while low <= high:
        mid = (low + high) // 2
        if seq[mid] < key:
            low = mid + 1
        elif seq[mid] > key:
            high = mid - 1
        else:
            return True
    return False


def test_binary_contains() -> None:
    nums = [1, 3, 4, 6, 7]
    key = 4
    assert binary_contains(nums, key) == True, f"{nums} should contain {key}"
