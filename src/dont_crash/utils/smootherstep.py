def smootherstep(t: float, duration: float = 1.0) -> float:
    """ Calculate a smooth interpolation value using the Smootherstep function.
    
    This function returns a smoothly interpolated value from 0 to 1 over the specified duration,
    using the Smootherstep (Perlin's improved Smoothstep) algorithm for smooth easing.

    Args:
        t (float): The elapsed time in seconds.
        duration (float): The total duration over which to interpolate from 0 to 1, in seconds. Defaults to 1.0.
    
    Returns:
        float: A value between 0 and 1, representing the interpolated position along the duration.
              Returns 0 at t=0, 1 at t=duration (or later), and smoothly transitions in between.
    """
    x = min(t / duration, 1.0)
    return x**3 * (x * (x * 6 - 15) + 10)
