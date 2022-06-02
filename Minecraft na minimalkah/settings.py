import math

# настройки окна
width = 1920
height = 1080
half_width = width // 2
half_height = height // 2
FPS = 60
fps_pos = (width - 120, 45)
tile = 120
# while width % tile != 0 and height % tile != 0:
#     tile += 1

# настройки миникарты
map_scale = 5
map_tile = tile // map_scale
map_pos = (0, height - height // map_scale)

# лучевые настройки
fov = math.pi / 3
half_fov = fov / 2
num_rays = 300
while width % num_rays != 0:
    num_rays += 1
max_depth = 800
delta_angle = fov / num_rays
dist = num_rays / (2 * math.tan(half_fov))
proj_coeff = 3 * dist * tile
scale = width // num_rays

# настройки спрайтов
double_pi = 2 * math.pi
center_ray = num_rays // 2 - 1
fake_rays = 200

# параметры для текстуры (1200, 1200)
texture_width = 1200
texture_height = 1200
texture_scale = texture_width // tile
# настройки игрока
# player_pos = (width // 2, height // 2)
# player_angle = 0
player_pos = (227, 250)
player_angle = 1.57
player_speed = 2

# цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (220, 0, 0)
green = (0, 220, 0)
blue = (0, 0, 220)
dark_gray = (110, 110, 110)
purple = (120, 0, 120)
sky_day = (30, 144, 255)
grass = (0, 150, 0)
yellow = (220, 220, 0)
orange = (255, 165, 0)
