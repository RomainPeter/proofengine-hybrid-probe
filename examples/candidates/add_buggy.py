def add(a: int, b: int) -> int:
    # Bug: clamps negatives unnecessarily
    s = a + b
    return 0 if s < 0 else s
