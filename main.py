import pygame                # allows use of pygame's modules
from constants import *      # imports variables from constants.py
from player import *        # imports player class in player.py
from asteroid import *       # imports the asteroid class in asteroid.py
from asteroidfield import *   # imports the asteroid field class in asteroidfield.py
def main():

    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    

    while pygame.get_init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = game_clock.tick(60) / 1000
        screen.fill((0, 0, 0))
        for item in updatable:
            item.update(dt)
        for item in asteroids:
            if item.collision(player):
                print("Game over!")
                exit()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()