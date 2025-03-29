# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *



def main():
    pygame.init()
    gameclock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color="black")
        for thing in drawable:
            thing.draw(screen)
        updateable.update(dt)

        pygame.display.flip()
        dt = gameclock.tick(60) / 1000
                
        
if __name__ == "__main__":
    main()