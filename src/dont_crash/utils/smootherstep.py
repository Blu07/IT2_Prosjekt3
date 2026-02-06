def smootherstep(t: float, duration: float = 1.0) -> float:
    # t in seconds
    x = min(t / duration, 1.0)
    return x**3 * (x * (x * 6 - 15) + 10)
