import random
from candidates.impl import add


def test_identity():
    for a in [0, 1, 2, 10, -3, 999]:
        assert add(a, 0) == a


def test_commutative():
    for _ in range(50):
        a = random.randint(-1000, 1000)
        b = random.randint(-1000, 1000)
        assert add(a, b) == add(b, a)


def test_associative_samples():
    for _ in range(50):
        a = random.randint(-100, 100)
        b = random.randint(-100, 100)
        c = random.randint(-100, 100)
        assert add(add(a, b), c) == add(a, add(b, c))
