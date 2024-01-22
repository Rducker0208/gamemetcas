import pygame
import random


class Druif:
    def __init__(self, druif_id, screen, player):
        self.id = druif_id
        self.screen = screen
        self.player = player
        self.angle = 0
        self.rot = random.choice((-2, 2))
        self.image = pygame.transform.rotozoom(pygame.image.load(".\\Resources\\grape.png").convert_alpha(), 0, .5)
        self.rect = self.image.get_rect()
        spawn_zone = None
        spawn_location = random.randint(1, 20)

        # // onder zeus
        if 15 > spawn_location > 5:
            self.x = random.randint(25, screen.get_width() - 25)
            self.y = random.randint(100, screen.get_height() - 25)
            spawn_zone = 1

        # // links van zeus
        elif spawn_location <= 5:
            self.x = random.randint(25, 200)
            self.y = random.randint(25, 100)
            spawn_zone = 2

        # // rechts van zeus
        elif spawn_location >= 15:
            self.x = random.randint(screen.get_width() - 200, screen.get_width() - 25)
            self.y = random.randint(25, 100)
            spawn_zone = 3

        print(f"Druif {self.id}, coörds: {(self.x, self.y)}, spawn zone: {spawn_zone}")

    def drawDruif(self):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.rect = rotated_image.get_rect(center=self.image.get_rect(center=(self.x, self.y)).center)
        if self.angle == 24:
            self.rot = -2
        elif self.angle == -24:
            self.rot = 2
        self.angle += self.rot
        self.screen.blit(rotated_image, self.rect)

    def collision(self):
        if self.rect.colliderect(self.player.rect):
            return True
        else:
            return False

    def update(self):
        self.drawDruif()
