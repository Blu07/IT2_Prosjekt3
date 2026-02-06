from src.dont_crash.models import Asteroid

def test_asteroid_initialization():
    asteroid = Asteroid(x=100, y=150, size=30, vel=50)
    
    assert asteroid.pos_x == 100
    assert asteroid.pos_y == 150
    assert asteroid.size == 30
    assert asteroid.vel == 50

def test_asteroid_update():
    asteroid = Asteroid(x=100, y=150, size=30, vel=50)
    
    # Simulate 1 second of movement
    asteroid.update(1.0)
    
    assert asteroid.pos_x == 150  # 100 + 50*1
    assert asteroid.pos_y == 150