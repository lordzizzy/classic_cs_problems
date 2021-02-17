from functools import lru_cache
from typing import Generator
from typing import Dict
from typing import Callable
from termcolor import colored


class Solution:
    def __init__(self):
        self._cache: Dict[int, int] = {0: 0, 1: 1}

    def fib_recusive_mem(self, n: int) -> int:
        if n < 2:
            return n
        if n not in self._cache:
            self._cache[n] = self.fib_recusive_mem(n - 2) + self.fib_recusive_mem(n - 1)
        return self._cache[n]

    @lru_cache(maxsize=None)
    def fib_recursive_lru(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib_recursive_lru(n - 2) + self.fib_recursive_lru(n - 1)

    def fib_iterative(self, n: int) -> int:
        if n < 2:
            return n
        last: int = 0
        next: int = 1
        for _ in range(1, n):
            last, next = next, last + next
        return next

    def fib_coroutine(self, n: int) -> Generator[int, None, None]:
        yield 0
        if n > 0:
            yield 1
        last: int = 0
        next: int = 1
        for _ in range(1, n):
            last, next = next, last + next
            yield next


def test_solution(n: int, expected: int):
    def test_func(func: Callable[[int], int], n: int, expected: int):
        r = func(n)
        if r == expected:
            print(colored(f"PASSED - {func.__name__}({n}) = {r}", "green"))
        else:
            print(
                colored(
                    f"FAILED - {func.__name__}({n}) = {r}, but expected: {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_func(sln.fib_recusive_mem, n, expected)
    test_func(sln.fib_recursive_lru, n, expected)
    test_func(sln.fib_iterative, n, expected)


if __name__ == "__main__":
    test_solution(n=1, expected=1)
    test_solution(n=2, expected=1)
    test_solution(n=3, expected=2)
    test_solution(n=4, expected=3)
    test_solution(n=5, expected=5)
