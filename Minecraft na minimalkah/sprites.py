import pygame
from settings import *


class Sprites:
    def __init__(self):
        self.sprite_types = {
            "barrel": pygame.image.load('sprites/barrel/stiv_with_diamond_sword.jpg').convert(),
            "pedestal": pygame.image.load('sprites/pedestal/0.png').convert_alpha(),
            "devil": [pygame.image.load(f'sprites/devil/{i}.png').convert_alpha() for i in range(8)]

        }
        self.sprite_types["barrel"].set_colorkey((255, 255, 255))
        self.list_of_objects = [
            SpriteObject(self.sprite_types["barrel"], True, (8.1, 2.1), -0.5, 3.0),
            SpriteObject(self.sprite_types["barrel"], True, (5.7, 2.1), 10.0, 0.1),
            SpriteObject(self.sprite_types["pedestal"], True, (8.8, 2.1), 1.6, 0.5),
            SpriteObject(self.sprite_types["pedestal"], True, (8.8, 5.6), 1.6, 0.5),
            SpriteObject(self.sprite_types["devil"], False, (9, 3), -0.2, 0.7)

        ]


class SpriteObject:
    def __init__(self, object, static, pos, shift, scale):
        self.object = object
        self.static = static
        self.pos = self.x, self.y = pos[0] * tile, pos[1] * tile
        self.shift = shift
        self.scale = scale

        if not static:
            self.sprite_angles = [frozenset(range(i, i + 45)) for i in range(0, 360, 45)]
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.object)}

    def object_locate(self, player, walls):
        fake_walls0 = [walls[0] for i in range(fake_rays)]
        fake_walls1 = [walls[-1] for i in range(fake_rays)]
        fake_walls = fake_walls0 + walls + fake_walls1

        dx, dy = self.x - player.x, self.y - player.y
        distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)

        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += double_pi

        delta_rays = int(gamma / delta_angle)
        current_ray = center_ray + delta_rays
        distance_to_sprite *= math.cos(half_fov - current_ray * delta_angle)

        fake_ray = current_ray + fake_rays
        if 0 <= fake_ray <= num_rays - 1 + 2 * fake_rays and distance_to_sprite < fake_walls[fake_ray][0]:
            proj_height = min(int(proj_coeff / distance_to_sprite * self.scale), 2 * height)
            half_proj_height = proj_height // 2
            shift = half_proj_height * self.shift

            if not self.static:
                if theta < 0:
                    theta += double_pi
                theta = 360 - int(math.degrees(theta))

                for angles in self.sprite_angles:
                    if theta in angles:
                        self.object = self.sprite_positions[angles]
                        break

            sprite_pos = (current_ray * scale - half_proj_height, half_height - half_proj_height + shift)
            sprite = pygame.transform.scale(self.object, (proj_height, proj_height))
            return (distance_to_sprite, sprite, sprite_pos)
        else:
            return (False,)
