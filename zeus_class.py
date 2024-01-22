import pygame


class Zeus:
    def __init__(self, screen):
        self.screen = screen
        self.zeus_sprite = pygame.transform.scale_by(pygame.image.load("Resources/zeus/zeus.png").convert_alpha(), 0.35)
        self.cloud_sprite = pygame.transform.scale_by(pygame.image.load("Resources/zeus/cloud.png").convert_alpha(), 0.35)
        self.zeus_rect = self.zeus_sprite.get_rect()
        self.cloud_rect = self.cloud_sprite.get_rect()
        self.zeus_rect.center = ((self.screen.get_width() / 2) - 25, 100)
        self.cloud_rect.center = (465, 150)
        self.cloud_anim_side = 1
        self.counter = 0

    def draw(self):
        self.screen.blit(self.zeus_sprite, self.zeus_rect)
        if self.counter == 6:
            self.cloud_rect.centerx += self.cloud_anim_side
            self.screen.blit(self.cloud_sprite, self.cloud_rect)
            self.counter = 0
        else:
            self.screen.blit(self.cloud_sprite, self.cloud_rect)
        self.counter += 1

    def update(self):
        if self.cloud_rect.centerx == 470:
            self.cloud_anim_side = -1
        elif self.cloud_rect.centerx == 460:
            self.cloud_anim_side = 1
        self.draw()


