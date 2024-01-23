import pygame


class hearts:
    def __init__(self, screen):
        self.screen = screen
        self.empty_heart = pygame.transform.scale_by(pygame.image.load("Resources/hearts/background.png"), 3)
        self.heart_border = pygame.transform.scale_by(pygame.image.load("Resources/hearts/border.png"), 3)
        self.heart = pygame.transform.scale_by(pygame.image.load("Resources/hearts/heart.png"), 3)

        self.empty_heart_rect_1 = self.empty_heart.get_rect()
        self.empty_heart_rect_2 = self.empty_heart.get_rect()
        self.empty_heart_rect_3 = self.empty_heart.get_rect()
        self.empty_heart_rect_4 = self.empty_heart.get_rect()
        self.empty_heart_rect_5 = self.empty_heart.get_rect()

        self.heart_border_1 = self.heart_border.get_rect()
        self.heart_border_2 = self.heart_border.get_rect()
        self.heart_border_3 = self.heart_border.get_rect()
        self.heart_border_4 = self.heart_border.get_rect()
        self.heart_border_5 = self.heart_border.get_rect()

        self.heart_1 = self.heart.get_rect()
        self.heart_2 = self.heart.get_rect()
        self.heart_3 = self.heart.get_rect()
        self.heart_4 = self.heart.get_rect()
        self.heart_5 = self.heart.get_rect()

        self.heart_border_1.center = (30, 40)

        self.heart_border_2.center = (80, 40)

        self.heart_border_3.center = (130, 40)

        self.heart_border_4.center = (180, 40)

        self.heart_border_5.center = (230, 40)

    def update_hearts(self, hearts_left):

        self.screen.blit(self.heart_border, self.heart_border_1)
        self.screen.blit(self.heart_border, self.heart_border_2)
        self.screen.blit(self.heart_border, self.heart_border_3)
        self.screen.blit(self.heart_border, self.heart_border_4)
        self.screen.blit(self.heart_border, self.heart_border_5)

        if hearts_left >= 1:
            self.heart_1.center = (30, 40)
            self.screen.blit(self.heart, self.heart_1)
        else:
            self.empty_heart_rect_1.center = (30, 40)
            self.screen.blit(self.empty_heart, self.empty_heart_rect_1)

        if hearts_left >= 2:
            self.heart_2.center = (80, 40)
            self.screen.blit(self.heart, self.heart_2)
        else:
            self.empty_heart_rect_2.center = (80, 40)
            self.screen.blit(self.empty_heart, self.empty_heart_rect_2)

        if hearts_left >= 3:
            self.heart_3.center = (130, 40)
            self.screen.blit(self.heart, self.heart_3)
        else:
            self.empty_heart_rect_3.center = (130, 40)
            self.screen.blit(self.empty_heart, self.empty_heart_rect_3)

        if hearts_left >= 4:
            self.heart_4.center = (180, 40)
            self.screen.blit(self.heart, self.heart_4)
        else:
            self.empty_heart_rect_4.center = (180, 40)
            self.screen.blit(self.empty_heart, self.empty_heart_rect_4)

        if hearts_left >= 5:
            self.heart_5.center = (230, 40)
            self.screen.blit(self.heart, self.heart_5)
        else:
            self.empty_heart_rect_5.center = (230, 40)
            self.screen.blit(self.empty_heart, self.empty_heart_rect_5)
