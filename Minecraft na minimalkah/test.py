# import pygame
#
# pygame.init()
# sc = pygame.display.set_mode((1920, 1080))
# clock = pygame.time.Clock()
# pygame.display.set_caption('Minecraft')
# height = 150
# height_pos = 540
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#     sc.fill((30, 144, 255))
#     pygame.draw.rect(sc, (0, 0, 0), (960, height_pos, 150, height))
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP]:
#         height += 1
#         height_pos -= 1
#     if keys[pygame.K_DOWN]:
#         height -= 1
#         height_pos += 1
#     print(height_pos, height)
#     pygame.display.flip()
#     clock.tick()
import pygame
import math
from pygame.locals import *

# vars
W = 400
H = 400

WHITE = (255, 255, 255)

angle = 0

# init game
pygame.init()

sc = pygame.display.set_mode((W, H))

car_surf = pygame.image.load('car.png').convert()
car_surf.set_colorkey(WHITE)

car_rect = car_surf.get_rect(center=(W // 2, H // 2))

sc.fill(WHITE)

sc.blit(car_surf, car_rect)

while 1:

    keys = pygame.key.get_pressed()

    # process button press
    if (keys[K_UP]):
        car_rect.move_ip(math.sin(angle) * -5, math.cos(angle) * -5)

    if (keys[K_DOWN]):
        car_rect.move_ip(math.sin(angle) * 5, math.cos(angle) * 5)

    if (keys[K_LEFT]):
        angle += math.pi / 36

    if (keys[K_RIGHT]):
        angle -= math.pi / 36

    events = pygame.event.get()
    pygame.display.update()

    for event in events:
        if (event.type == QUIT):
            exit()

    # render new frame
    car_surf = pygame.transform.rotate(pygame.image.load('car.png').convert(), angle * 180 / math.pi)
    sc.fill(WHITE)
    car_rect = car_surf.get_rect(center=car_rect.center)
    sc.blit(car_surf, car_rect)

    pygame.time.delay(50)