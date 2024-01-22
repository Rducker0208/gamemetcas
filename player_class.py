import pygame
import os


# player
class Player:
    def __init__(self, screen):
        self.screen = screen
        self.walkL = []
        self.walkR = []
        self.idleL = []
        self.idleR = []
        self.directory = ".\\Resources\\player"
        for file in os.listdir(self.directory):
            filename = os.fsdecode(file)
            if filename.startswith("playerWalk"):
                self.walkL.append(pygame.transform.scale_by(pygame.image.load
                                                            (f".\\Resources\\player\\{file}").convert_alpha(), 2.5))
                self.walkR.append(pygame.transform.scale_by(pygame.transform.flip(pygame.image.load
                                                                                  (f".\\Resources\\player\\{file}").convert_alpha(),
                                                                                  True, False), 2.5))
            elif filename.startswith("playerIdle"):
                self.idleR.append(pygame.transform.scale_by(pygame.image.load
                                                            (f'.\\Resources\\player\\{file}').convert_alpha(), 2.5))
                self.idleL.append(pygame.transform.scale_by(pygame.transform.flip(pygame.image.load
                                                                                  (f".\\Resources\\player\\{file}").convert_alpha(),
                                                                                  True, False), 2.5))
        self.surface = pygame.transform.scale_by(pygame.image.load(".\\Resources\\player\\playerWalk1.png"), 2.5)
        self.rect = self.surface.get_rect(midbottom=(500, 300))
        self.counter = 0
        self.frame_counter = 0
        self.facing_direction = "right"
        self.health = 5
        self.movement_speed = 4

    def playerInput(self):
        keys_pressed = pygame.key.get_pressed()
        if not self.rect.x < 0 or not self.rect.x > 1000:  # Player Input
            if keys_pressed[pygame.K_d]:
                if self.rect.right < self.screen.get_width() - 10:
                    self.facing_direction = "right"
                    self.animate('right')
                    self.rect.x += self.movement_speed
            if keys_pressed[pygame.K_a]:
                if self.rect.left > 10:
                    self.facing_direction = "left"
                    self.animate('left')
                    self.rect.x += -self.movement_speed
            if keys_pressed[pygame.K_w]:
                if self.rect.top > 10:
                    self.animate('up')
                    self.rect.y += -self.movement_speed
            if keys_pressed[pygame.K_s]:
                if self.rect.bottom < self.screen.get_height() - 10:
                    self.animate('down')
                    self.rect.y += self.movement_speed
            if not keys_pressed[pygame.K_s] and not keys_pressed[pygame.K_w] and not keys_pressed[pygame.K_a] and not \
            keys_pressed[pygame.K_d]:
                self.animate(None)

    def animate(self, direction):
        keys_pressed = pygame.key.get_pressed()
        if self.frame_counter == 5:
            if direction == 'right':
                self.surface = self.walkL[self.counter]
                self.counter = (self.counter + 1) % len(self.walkL)
            elif direction == 'left':
                self.surface = self.walkR[self.counter]
                self.counter = (self.counter + 1) % len(self.walkR)
            elif direction == 'up' or direction == 'down':
                if self.facing_direction == "left" and not keys_pressed[pygame.K_a] and not keys_pressed[pygame.K_d]:
                    self.surface = self.walkR[self.counter]
                    self.counter = (self.counter + 1) % len(self.walkR)
                elif not keys_pressed[pygame.K_a] and not keys_pressed[pygame.K_d]:
                    self.surface = self.walkL[self.counter]
                    self.counter = (self.counter + 1) % len(self.walkL)
            else:
                if self.facing_direction == "left" and not keys_pressed[pygame.K_a] and not keys_pressed[pygame.K_d]:
                    self.surface = self.idleL[self.counter]
                    self.counter = (self.counter + 1) % len(self.idleL)
                elif not keys_pressed[pygame.K_a] and not keys_pressed[pygame.K_d]:
                    self.surface = self.idleR[self.counter]
                    self.counter = (self.counter + 1) % len(self.idleR)

            self.frame_counter = 0
        self.frame_counter += 1

    def draw(self):
        self.screen.blit(self.surface, self.rect)

    def update(self):
        if self.counter > len(self.walkR): self.counter = 0
        self.playerInput()
        self.draw()
