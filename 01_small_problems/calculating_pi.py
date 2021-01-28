from termcolor import colored


def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi


def test_calculate_pi(n_terms: int, expected: float):
    r = calculate_pi(n_terms)
    if r == expected:
        print(colored(f"PASSED - pi in {n_terms} terms is {r}", "green"))
    else:
        print(
            colored(f"FAILED - pi in {n_terms} terms is {r}, but expected: {expected}", "red"))


if __name__ == "__main__":
    test_calculate_pi(n_terms=1, expected=4.0)
    test_calculate_pi(n_terms=2, expected=2.666666666666667)
    test_calculate_pi(n_terms=3, expected=3.466666666666667)
    test_calculate_pi(n_terms=1000000, expected=3.1415916535897743)
