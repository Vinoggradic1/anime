import pygame
import os
import sys

m = 0

pygame.init()

Size_window = 800, 600
Fps = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode(Size_window)

image_bear = []
path = 'textures'
for file_name in os.listdir(path):
    image = pygame.image.load(f'{path}/{file_name}')
    image_bear.append(image)


class Class(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = image_bear
        self.index = 0
        self.range = len(self.images)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x // 2, y // 2))

    def update(self):
        self.index += 0.1
        self.image = self.images[int(self.index % self.range)]
        self.rect.x += 0
        self.image.set_alpha(m)


bear = Class(*Size_window)
sprites = pygame.sprite.Group()
sprites.add(bear)


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                m += 10 if m < 255 else 5 if m < 255 else 0
            if e.key == pygame.K_DOWN:
                m -= 10 if m > 5 else 5 if m > 0 else 0
    screen.fill((0, 0, 0))
    sprites.update()
    sprites.draw(screen)
    pygame.display.update()
    clock.tick(Fps)
    # pyinstaller main.py --onefile --noconsole
