
def balls_collide(x1: float, y1: float, r1: float, x2: float, y2: float, r2: float) -> bool:
    """ Check if two circles (balls) are colliding based on their positions and radii.

    Args:
        x1 (float): The x-coordinate of the first circle's center.
        y1 (float): The y-coordinate of the first circle's center.
        r1 (float): The radius of the first circle.
        x2 (float): The x-coordinate of the second circle's center.
        y2 (float): The y-coordinate of the second circle's center.
        r2 (float): The radius of the second circle.
    
    Returns:
        bool: True if the circles are colliding (distance between centers <= sum of radii), False otherwise.
    """
    dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
    radius_sum = r1 + r2
    return dist_sq <= radius_sum ** 2