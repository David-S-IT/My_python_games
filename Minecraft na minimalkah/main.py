import pygame
from settings import *
from player import Player
from sprites import *
from rays import ray_casting
from draw import Drawing

pygame.init()
sc = pygame.display.set_mode((width, height))
map = pygame.Surface((width // map_scale, height // map_scale))

sprites = Sprites()
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, map)
pygame.display.set_caption('Minecraft')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    # sc.fill(black)

    drawing.background(player.angle)
    walls = ray_casting(player, drawing.textures)
    drawing.world(walls + [obj.object_locate(player, walls) for obj in sprites.list_of_objects])
    drawing.fps(clock)
    drawing.mini_map(player)

    pygame.display.flip()
    clock.tick()
