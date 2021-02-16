from __future__ import annotations
from typing import Any, Protocol


class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        ...

    def __lt__(self, other: Comparable) -> bool:
        ...

    def __gt__(self, other: Comparable) -> bool:
        return (not self < other) and self != other

    def __le__(self, other: Comparable) -> bool:
        return (self < other) or self == other

    def __ge__(self, other: Comparable) -> bool:
        return not self < other
