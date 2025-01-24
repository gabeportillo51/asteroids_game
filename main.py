import pygame                # allows use of pygame's modules
from constants import *   # imports variables from constants.py
from player import *     # imports player class in player.py

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    while pygame.get_init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = game_clock.tick(60) / 1000
        screen.fill((0, 0, 0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()