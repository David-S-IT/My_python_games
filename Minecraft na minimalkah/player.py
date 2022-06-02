import pygame
from settings import *


class Player:

    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        sin = math.sin(self.angle)
        cos = math.cos(self.angle)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.x += player_speed * cos
            self.y += player_speed * sin
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.x += -player_speed * cos
            self.y += -player_speed * sin
        if keys[pygame.K_a]:
            self.x += player_speed * sin
            self.y += -player_speed * cos
        if keys[pygame.K_d]:
            self.x += -player_speed * sin
            self.y += player_speed * cos
        if keys[pygame.K_LEFT]:
            self.angle -= 0.04
        if keys[pygame.K_RIGHT]:
            self.angle += 0.04
        if keys[pygame.K_ESCAPE]:
            exit()

        self.angle %= double_pi