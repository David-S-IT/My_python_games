import pygame
from settings import *
from rays import ray_casting
from map import mini_map


class Drawing:
    def __init__(self, sc, map):
        self.sc = sc
        self.map = map
        self.font = pygame.font.SysFont("Open Sans", 75, bold=True)
        self.textures = {'1': pygame.image.load('textures/kamennaya_kladka.jpg').convert(),
                         '2': pygame.image.load('textures/doska.png').convert(),
                         'sky': pygame.image.load('textures/sky.png').convert()
                         }

    def background(self, angle):
        sky_offset = -10 * math.degrees(angle) % width
        self.sc.blit(self.textures['sky'], (sky_offset, 0))
        self.sc.blit(self.textures['sky'], (sky_offset - width, 0))
        self.sc.blit(self.textures['sky'], (sky_offset + width, 0))
        pygame.draw.rect(self.sc, grass, (0, half_height, width, half_height))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.sc.blit(object, object_pos)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, red)
        self.sc.blit(render, fps_pos)

    def mini_map(self, player):
        self.map.fill(grass)
        map_x, map_y = player.x // map_scale, player.y // map_scale
        pygame.draw.line(self.map, yellow, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                            map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.map, red, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.map, orange, (x, y, map_tile, map_tile))
        self.sc.blit(self.map, map_pos)
