import pygame
from settings import *
from map import world_map


def mapping(xo, yo):
    return (xo // tile) * tile, (yo // tile) * tile


def ray_casting(player, textures):
    walls = []
    xo, yo = player.pos
    xm, ym = mapping(xo, yo)
    cur_angle = player.angle - half_fov
    for ray in range(num_rays):
        sin = math.sin(cur_angle)
        cos = math.cos(cur_angle)

        # вертикали
        x, dx = (xm + tile, 1) if cos >= 0 else (xm, -1)
        for i in range(0, width, tile):
            depth_v = (x - xo) / cos
            yv = yo + depth_v * sin
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            x += dx * tile

        # горизонтали
        y, dy = (ym + tile, 1) if sin >= 0 else (ym, -1)
        for i in range(0, height, tile):
            depth_h = (y - yo) / sin
            xh = xo + depth_h * cos
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            y += dy * tile

        # проекция
        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        offset = int(offset) % tile
        depth *= math.cos(player.angle - cur_angle)
        depth = max(depth, 0.00001)
        proj_height = min(int(proj_coeff / depth), 2 * height)

        wall_column = textures[texture].subsurface(offset * texture_scale, 0, texture_scale, texture_height)
        wall_column = pygame.transform.scale(wall_column, (scale, proj_height))
        wall_pos = (ray * scale, half_height - proj_height // 2)

        walls.append((depth, wall_column, wall_pos))
        cur_angle += delta_angle
    return walls
