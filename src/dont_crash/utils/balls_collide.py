
def balls_collide(x1: float, y1: float, r1: float, x2: float, y2: float, r2: float) -> bool:
    dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
    radius_sum = r1 + r2
    return dist_sq <= radius_sum ** 2