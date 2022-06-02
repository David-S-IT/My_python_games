import pygame, random
from pygame import mixer

moshno = 0
mixer.pre_init(44100, -16, 2, 1411)
mixer.init()
auch = mixer.Sound('sounds/hurt.ogg')
plus_ochki = mixer.Sound('sounds/orb.ogg')
victory = mixer.Sound('sounds/Victory.mp3')
lose = mixer.Sound('sounds/Lose.mp3')
victory_yes = mixer.Sound('sounds/yes.ogg')
lose_death = mixer.Sound('sounds/death.ogg')

display_w = 800
display_h = 900
game_exit = False

pygame.init()
game_display = pygame.display.set_mode((display_w, display_h))
shrift = pygame.font.Font('fonts/Pixel.ttf', 30)


# глобальные переменные будут здесь
class Car:
    x = 410
    y = display_h * 0.5
    image = pygame.image.load('textures/car.png')
    speed = 0

    def draw(self, display):
        self.y += self.speed
        display.blit(self.image, (self.x, self.y))


class WragCar(Car):

    def __init__(self, polosa):
        if polosa < 5:
            self.y = -98
            self.speed = 4
            self.x = 335
            self.image = pygame.image.load('textures/car_red2.png')
        else:
            self.y = display_h - 1
            self.speed = -4
            self.x = 410
            self.image = pygame.image.load('textures/car_red1.png')

    def draw(self, display):
        self.y += self.speed

        if self.y <= -99:
            mixer.pre_init(44100, -16, 1, 705)
            plus_ochki.play()
            Game.ochki += 1
            Game.AllWragi.remove(self)
        elif self.y > display_h:
            mixer.pre_init(44100, -16, 1, 705)
            plus_ochki.play()
            Game.ochki += 1
            Game.AllWragi.remove(self)
        else:
            display.blit(self.image, (self.x, self.y))


class Background:
    x = 0
    y = 0

    speed = 30
    height = 2352

    background1 = pygame.image.load('textures/background.png')
    background2 = pygame.image.load('textures/background.png')

    def draw(self, display):
        display.blit(self.background1, (self.x, self.y))
        display.blit(self.background2, (self.x, self.y - self.height))

        self.y += self.speed

        if self.y >= display_h:
            self.y = display_h - self.height


class Game:
    # здесь будут экземпляры класса, все элементы игры
    back = Background()
    PlayerCar = Car()
    AllWragi = []
    AllWragi2 = []
    MassWragCar = 0
    ochki = 0
    pause = False
    prochnost = 5
    green_car = []

    # if not pause:

    def check_collision(self):
        player_сar_rect = self.PlayerCar.image.get_rect().move(self.PlayerCar.x, self.PlayerCar.y)

        for wrag in self.AllWragi:
            wrag_rect = wrag.image.get_rect().move(wrag.x, wrag.y)
            if player_сar_rect.colliderect(wrag_rect):
                mixer.pre_init(44100, -16, 1, 705)
                auch.play()
                self.AllWragi.remove(wrag)
                self.prochnost -= 1
        # for wrag2 in self.AllWragi2:
        #     wrag2_rect = wrag2.image.get_rect().move(wrag2.x, wrag2.y)
        #     if wrag2_rect.colliderect(wrag_rect):
        #         self.AllWragi2.remove(wrag2)

    def draw(self, game_display):
        # на этом уровне должна происходить отрисовка
        # нарисовать фон
        Game.back.draw(game_display)
        # нарисовать машинку
        player_car = Game.PlayerCar.draw(game_display)
        self.green_car.append(player_car)
        for wragi in Game.AllWragi:
            wragi.draw(game_display)
        # полоса
        # pygame.draw.rect(game_display, (0, 0, 0), (0, display_h - 15, display_w, 10))
        # нарисуем счет
        # прочность
        game_display.blit(pygame.image.load('textures/car2.png'), (675, 200))
        # железо/очки
        game_display.blit(pygame.image.load('textures/iron.png'), (550, -40))
        ochki_text = shrift.render(str(self.ochki), True, (0, 0, 0))
        if self.prochnost <= 0:
            prochnost_text = shrift.render("0", True, (255, 0, 0))
            self.green_car.remove(player_car)
            ScreenSelector.screen = LoseEnd()

        elif self.prochnost == 1:
            prochnost_text = shrift.render(str(self.prochnost), True, (255, 36, 0))

        elif self.prochnost == 2:
            prochnost_text = shrift.render(str(self.prochnost), True, (255, 102, 18))

        elif self.prochnost == 3:
            prochnost_text = shrift.render(str(self.prochnost), True, (255, 162, 18))

        elif self.prochnost == 4:
            prochnost_text = shrift.render(str(self.prochnost), True, (255, 204, 0))

        elif self.prochnost == 5:
            prochnost_text = shrift.render(str(self.prochnost), True, (255, 255, 255))
        game_display.blit(prochnost_text, (719, 297))
        game_display.blit(ochki_text, (700, 22))

    def upravlenie_ochkami(self):
        # Game.ochki += 1
        # time.sleep(4)
        pass

    def tick(self):
        if self.ochki >= 50:
            ScreenSelector.screen = VictoryEnd()
        self.check_collision()
        if random.randint(0, 20) == 10:
            # if self.MassWragCar == 0:
            self.AllWragi.append(WragCar(random.randint(0, 10)))
            #     self.MassWragCar = 1
            # else:
            #     self.AllWragi2.append(WragCar(random.randint(0, 10)))
            #     self.MassWragCar = 0

    # клавиши/команды
    def process_keyboard(self, event):
        Game.PlayerCar.speed = 0
        if event.type == pygame.KEYDOWN:
            if event.key == 97 or event.key == pygame.K_LEFT:
                Game.PlayerCar.x = 335

            if event.key == 100 or event.key == pygame.K_RIGHT:
                Game.PlayerCar.x = 410

            if event.key == pygame.K_w or event.key == pygame.K_UP:
                Game.PlayerCar.speed = -4.2

            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                Game.PlayerCar.speed = 4.2

            if event.key == 27:
                Game.pause = not Game.pause

            if Game.PlayerCar.y >= display_h:
                Game.PlayerCar.y = -89
                Game.PlayerCar.speed = 4.2

            elif Game.PlayerCar.y <= -99:
                Game.PlayerCar.y = display_h
                Game.PlayerCar.speed = -4.2


# else:
#     pause_text = shrift.render("П А У З А", True, (255, 255, 255))
#     game_display.blit(pause_text, (display_w / 2 - 75, display_h / 2 - 20))


class Menu:
    ckursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    def tick(self):
        self.ckursor = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

    def draw(self, game_display):
        game_display.blit(pygame.image.load('textures/background.png'), (0, 0))
        game_display.blit(pygame.image.load('textures/car.png'), (410, display_h * 0.52))
        game_display.blit(pygame.image.load('textures/car_red2.png'), (335, display_h * 0.68))
        game_display.blit(pygame.image.load('textures/car_red2.png'), (335, display_h * 0.13))
        game_display.blit(pygame.image.load('textures/car_red1.png'), (410, display_h * 0.27))
        game_display.blit(pygame.image.load('textures/button_play.jpg'), (display_w / 2 - 205, display_h / 2 - 80))
        game_display.blit(pygame.image.load('textures/out_game.jpg'), (display_w / 2 - 125, display_h / 2 + 80))
        game_display.blit(pygame.image.load('textures/controls.jpg'), (display_w / 2 - 173, display_h / 2 - 3))

    def process_keyboard(self, event):
        if 195 < self.ckursor[0] < 606 and 370 < self.ckursor[1] < 410:
            game_display.blit(pygame.image.load('textures/button_play1.jpg'), (display_w / 2 - 205, display_h / 2 - 80))
            if self.click[0] == 1:
                ScreenSelector.screen = Game()

        if 275 < self.ckursor[0] < 525 and 530 < self.ckursor[1] < 581:
            game_display.blit(pygame.image.load('textures/out_game1.jpg'), (display_w / 2 - 125, display_h / 2 + 80))
            if self.click[0] == 1:
                quit()

        if 227 < self.ckursor[0] < 577 and 450 < self.ckursor[1] < 496:
            game_display.blit(pygame.image.load('textures/controls1.jpg'), (display_w / 2 - 173, display_h / 2 - 3))
            if self.click[0] == 1:
                ScreenSelector.screen = Controls()


class VictoryEnd:
    ckursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    moshno = 1

    def tick(self):
        self.ckursor = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

    def draw(self, game_display):
        end_text = shrift.render("V I S T O R Y !", True, (0, 255, 0))
        game_display.blit(end_text, (display_w / 2 - 119, display_h / 2 - 25))
        game_display.blit(pygame.image.load('textures/out_game.jpg'), (display_w / 2 - 125, display_h / 2 + 80))
        if self.moshno == 1:
            mixer.pre_init(44100, -16, 1, 705)
            victory_yes.play()
            mixer.pre_init(44100, -16, 2, 128)
            victory.play(-1)
            self.moshno = 2

    def process_keyboard(self, event):
        if 275 < self.ckursor[0] < 525 and 530 < self.ckursor[1] < 581:
            game_display.blit(pygame.image.load('textures/out_game1.jpg'), (display_w / 2 - 125, display_h / 2 + 80))
            if self.click[0] == 1:
                quit()


class LoseEnd:
    ckursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    moshno = 1

    def tick(self):
        self.ckursor = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

    def draw(self, game_display):
        end_text = shrift.render("G A M E  O V E R", True, (255, 0, 0))
        game_display.blit(end_text, (display_w / 2 - 140, display_h / 2 - 50))
        game_display.blit(pygame.image.load('textures/out_game.jpg'), (display_w / 2 - 125, display_h / 2 + 80))
        if self.moshno == 1:
            mixer.pre_init(44100, -16, 1, 705)
            lose_death.play()
            mixer.pre_init(44100, -16, 2, 192)
            lose.play(-1)
            self.moshno = 2

    def process_keyboard(self, event):
        if 275 < self.ckursor[0] < 525 and 530 < self.ckursor[1] < 581:
            game_display.blit(pygame.image.load('textures/out_game1.jpg'), (display_w / 2 - 125, display_h / 2 + 80))
            if self.click[0] == 1:
                quit()


class Controls:
    ckursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    def tick(self):
        self.ckursor = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

    def draw(self, game_display):
        game_display.blit(pygame.image.load('textures/background.png'), (0, 0))
        game_display.blit(pygame.image.load('textures/car.png'), (410, display_h * 0.52))
        game_display.blit(pygame.image.load('textures/car_red2.png'), (335, display_h * 0.68))
        game_display.blit(pygame.image.load('textures/car_red2.png'), (335, display_h * 0.13))
        game_display.blit(pygame.image.load('textures/car_red1.png'), (410, display_h * 0.27))
        game_display.blit(pygame.image.load('textures/car2.png'), (675, 200))
        game_display.blit(pygame.image.load('textures/iron.png'), (display_h * 0.45, 200))

        strelochki_text = shrift.render("УПРАВЛЕНИЕ СТРЕЛОЧКАМИ", True, (105, 225, 0))
        zaiezd_za_krai_text = shrift.render("ЕСЛИ ЗАЕДЕТ ЗА", True, (105, 225, 0))
        zaiezd_za_krai_text2 = shrift.render("КРАЙ ОДНОЙ СТОРОНЫ,", True, (105, 225, 0))
        zaiezd_za_krai_text3 = shrift.render("ТО ВЫЕДЕТ С", True, (105, 225, 0))
        zaiezd_za_krai_text4 = shrift.render("ДРУГОЙ СТОРОНЫ", True, (105, 225, 0))
        kasanie_red_car_text = shrift.render("ПРИ КАСАНИИ ОТНИМАЕТСЯ", True, (255, 0, 0))
        kasanie_red_car_text2 = shrift.render("1 ПРОЧНОСТЬ МАШИНЫ", True, (255, 0, 0))
        krai_red_car_text = shrift.render("ЕСЛИ ДОСТИГНЕТ КРАЯ", True, (255, 0, 0))
        krai_red_car_text2 = shrift.render("ПРИБАВИТЬСЯ 1 ЖЕЛЕЗО", True, (255, 0, 0))
        vistory_text = shrift.render("ЦЕЛЬ ИГРЫ - НАКОПИТЬ 50 ЖЕЛЕЗА", True, (0, 255, 0))
        lose_text = shrift.render("И НЕ СЛОМАТЬ МАШИНКУ (ПРОЧНОСТЬ НЕ ДОЛЖНА", True, (255, 0, 0))
        lose_text2 = shrift.render("ДОСТИГНУТЬ НУЛЯ)", True, (255, 0, 0))
        prochnost_text = shrift.render("ПРОЧНОСТЬ", True, (105, 225, 0))
        game_display.blit(prochnost_text, (display_h * 0.71, 380))
        iron_text = shrift.render("ЖЕЛЕЗО", True, (195, 195, 195))
        prochnost_text = shrift.render("5", True, (255, 255, 255))
        ochki_text = shrift.render("0", True, (0, 0, 0))

        game_display.blit(strelochki_text, (display_w * 0.009, display_h * 0.55))
        game_display.blit(zaiezd_za_krai_text, (display_w * 0.59, display_h * 0.51))
        game_display.blit(zaiezd_za_krai_text2, (display_w * 0.59, display_h * 0.54))
        game_display.blit(zaiezd_za_krai_text3, (display_w * 0.59, display_h * 0.57))
        game_display.blit(zaiezd_za_krai_text4, (display_w * 0.59, display_h * 0.6))
        game_display.blit(kasanie_red_car_text, (display_w * 0.006, display_h * 0.28))
        game_display.blit(kasanie_red_car_text2, (display_w * 0.05, display_h * 0.33))
        game_display.blit(krai_red_car_text, (display_w * 0.5, display_h * 0.68))
        game_display.blit(krai_red_car_text2, (display_w * 0.5, display_h * 0.73))
        game_display.blit(vistory_text, (20, display_h * 0.02))
        game_display.blit(lose_text, (20, display_h * 0.07))
        game_display.blit(lose_text2, (display_w * 0.64, display_h * 0.11))
        game_display.blit(iron_text, (display_h * 0.56, 370))
        game_display.blit(prochnost_text, (719, 297))

        game_display.blit(pygame.image.load('textures/done.jpg'), (display_w / 2 / 2 / 2 + 10, display_h / 2 + 310))
        game_display.blit(ochki_text, (555, 262))

    def process_keyboard(self, event):
        if 110 < self.ckursor[0] < 708 and 760 < self.ckursor[1] < 819:
            game_display.blit(pygame.image.load('textures/done1.jpg'),
                              (display_w / 2 / 2 / 2 + 10, display_h / 2 + 310))
            if self.click[0] == 1:
                ScreenSelector.screen = Menu()


class ScreenSelector:
    screen = Menu()

    @staticmethod
    def tick():
        ScreenSelector.screen.tick()

    @staticmethod
    def draw(game_display):
        ScreenSelector.screen.draw(game_display)

    @staticmethod
    def process_keyboard(event):
        ScreenSelector.screen.process_keyboard(event)


# game = Game()
# game.upravlenie_ochkami()
clock = pygame.time.Clock()
# здесь можно смело поменять название
pygame.display.set_caption('Тачки')


# самая важная функция в ней все и происходит
def game_loop(update_time):
    global game_exit

    while not game_exit:
        for event in pygame.event.get():
            # print('a', event, 'z')
            # game.process_keyboard(event)

            if event.type == pygame.QUIT:
                game_exit = True
                quit()
        # на этом уровне должна происходить отрисовка

        # нарисовать фон

        # нарисовать машинку

        # game.draw()
        ScreenSelector.tick()
        ScreenSelector.draw(game_display)
        ScreenSelector.process_keyboard(event)
        pygame.display.update()
        clock.tick(update_time)


game_loop(30)
pygame.quit()
quit()
