import pygame
import os
import random


class thunder:
    def __init__(self, screen, location):
        self.image_count = 0
        self.frame = 0
        self.screen = screen
        self.thunder_sprites = []
        self.location = location
        self.rec_counter = 0
        num = 1
        base = ".\\Resources\\bliksem\\lightning_line5b%d.png"
        while os.path.isfile(base % num):
            self.thunder_sprites.append(pygame.transform.scale_by(pygame.image.load(base % num).convert_alpha(), 2))
            num += 1

    def draw(self):
        for _ in self.location:
            self.screen.blit(self.thunder_sprites[self.image_count], self.thunder_sprites[self.image_count].get_rect(
                center=(self.location[self.rec_counter][0] + 55, self.location[self.rec_counter][1] - random.randint(90, 110))))
            self.rec_counter = (self.rec_counter + 1) % len(self.location)
        if self.frame == 15:
            self.image_count += 1
            self.frame = 0
        self.frame += 1


    def ended(self):
        if self.image_count >= len(self.thunder_sprites):
            self.image_count = 0
            return True
        else:
            return False

    def update(self):
        self.draw()
