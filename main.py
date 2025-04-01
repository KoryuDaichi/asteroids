# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


# main program  functions
def main():
    
# initialize Pygame
    pygame.init()
    
# print starting data
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

# set up Game Clock, dt, and groups
    gameclock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Shot.containers = (updateable, drawable)

# set up the screen size and initialize the player
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    
# game loop
    while True:
        
    # check for exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
    # Create the background
        pygame.Surface.fill(screen, color="black")
        
    # iterate over the drawables group and draw each
        for thing in drawable:
            thing.draw(screen)
        
    # update all of the items in the updatable group
        updateable.update(dt)

    # Check for player asteroid collision
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()
            

    # update the game screen at a set frequency
        pygame.display.flip()
        dt = gameclock.tick(60) / 1000
                
# lock program run to this file        
if __name__ == "__main__":
    main()