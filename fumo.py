import time
import pygame

pygame.init()
class Fumo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/FumoReimu.png')
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))


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

previous_time = time.time()
times_clicked = 0
mouse_down = False
while running:
    if not running:
        pygame.quit()
        break

    delta_Time = time.time() - previous_time
    previous_time = time.time()

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    mouse = pygame.mouse.get_pressed()
    if mouse[0] and not mouse_down:
        mouse_pos = pygame.mouse.get_pos()
        mouse_down = True
        if 346 <= mouse_pos[0] <= 454 and 136 <= mouse_pos[1] <= 264:
            has_clicked_fumo = True
            times_clicked += 1
            sound.play()

    if not mouse[0] and mouse_down:
        mouse_down = False
    screen.blit(bg_surface, (0, 0))
    if has_clicked_fumo:
        yay_surface = pixel_font.render(f"You have clicked the fumo {times_clicked} {'times' if times_clicked > 1 else 'time' } :)", False, (64, 64, 64))
        yay_rectangle = yay_surface.get_rect(center=(SCREEN_WIDTH / 2, 50))
        screen.blit(yay_surface, yay_rectangle)

    fumo_group.draw(screen)
    pygame.display.update()
