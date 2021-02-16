from typing import Sequence, TypeVar

from shared.comparable import Comparable

C = TypeVar("C", bound="Comparable")


def binary_contains(seq: Sequence[C], key: C) -> bool:
    """
    >>> binary_contains([1,3,4,6,7], 4)
    True
    >>> binary_contains([1,3,4,6,7], 2)
    False
    """
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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
