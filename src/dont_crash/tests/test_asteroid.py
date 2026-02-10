from models import Asteroid

def test_asteroid_initialization():
    # Test simple initialization of an asteroid
    asteroid = Asteroid(x=100, y=150, size=30, vel=50)
    
    assert asteroid.pos_x == 100
    assert asteroid.pos_y == 150
    assert asteroid.size == 30
    assert asteroid.vel == 50

if __name__ == "__main__":
    test_asteroid_initialization()
    print("All tests passed!")