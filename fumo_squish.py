import time
import pygame

pygame.init()
class Fumo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.not_squished = pygame.image.load('assets/FumoReimu.png')
        self.squished = pygame.image.load('assets/FumoReimu.png')
        self.squished = pygame.transform.scale(self.squished, (128, 64))
        self.fumo = [self.not_squished, self.squished]
        self.squish_index = 0

        self.image = self.fumo[self.squish_index]
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.rotate = 90
        self.scale = 2
        self.bounds = [346, 454, 136, 264]
        self.squished = False

    def do_click(self):
        global mouse_down
        global times_clicked
        global has_clicked_fumo

        mouse = pygame.mouse.get_pressed()
        if mouse[0] and not mouse_down:
            mouse_pos = pygame.mouse.get_pos()
            mouse_down = True

            if self.bounds[0] <= mouse_pos[0] <= self.bounds[1] and self.bounds[2] <= mouse_pos[1] <= self.bounds[3]:
                has_clicked_fumo = True
                times_clicked += 1
                if self.squish_index == 0:
                    self.squish_index = 1
                    self.image = self.fumo[self.squish_index]
                    self.rect = self.image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 32))
                else:
                    self.squish_index = 0
                    self.image = self.fumo[self.squish_index]
                    self.rect = self.image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
                sound.play()

        if not mouse[0] and mouse_down:
            mouse_down = False

    def update(self,):
        self.do_click()


sound = pygame.mixer.Sound('assets/sounds/bloop.ogg')
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Fumo Click')
pygame.display.set_icon(pygame.image.load('assets/FumoReimu.png'))
bg_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
bg_surface.fill((255, 171, 248))
pixel_font = pygame.font.Font('assets/Pixeltype.ttf', 50)
running = True
has_clicked_fumo = False

fumo_group = pygame.sprite.GroupSingle()
fumo_group.add(Fumo())

times_clicked = 0
mouse_down = False
while running:
    if not running:
        pygame.quit()
        break
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_surface, (0, 0))
    if has_clicked_fumo:
        yay_surface = pixel_font.render(f"You have clicked the fumo {times_clicked} {'times' if times_clicked > 1 else 'time' } :)", False, (64, 64, 64))
        yay_rectangle = yay_surface.get_rect(center=(SCREEN_WIDTH / 2, 50))
        screen.blit(yay_surface, yay_rectangle)

    fumo_group.draw(screen)
    fumo_group.update()
    pygame.display.update()
