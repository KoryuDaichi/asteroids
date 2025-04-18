import pygame
from constants import *
from circleshape import *

# Shot class
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def move(self, player, dt):
        forward = pygame.Vector2(0, 1).rotate(player.rotation)
        self.position += forward * PLAYER_SHOOT_SPEED * dt

    def update(self, dt):
        self.position += self.velocity * dt
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()