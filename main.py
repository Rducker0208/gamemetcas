import random
import pygame

MAX_FRAMERATE = 60
SCREEN_SIZE = (1000, 600)


# player
class Player:
    def __init__(self):
        self.imagesR = [".\\Resources\\player\\playerWalk1.png",
                        ".\\Resources\\player\\playerWalk2.png",
                        ".\\Resources\\player\\playerWalk3.png",
                        ".\\Resources\\player\\playerWalk4.png",
                        ".\\Resources\\player\\playerWalk5.png",
                        ".\\Resources\\player\\playerWalk6.png",
                        ".\\Resources\\player\\playerWalk7.png",
                        ".\\Resources\\player\\playerWalk8.png", ]
        self.imagesL = [".\\Resources\\player\\playerWalkL1.png",
                        ".\\Resources\\player\\playerWalkL2.png",
                        ".\\Resources\\player\\playerWalkL3.png",
                        ".\\Resources\\player\\playerWalkL4.png",
                        ".\\Resources\\player\\playerWalkL5.png",
                        ".\\Resources\\player\\playerWalkL6.png",
                        ".\\Resources\\player\\playerWalkL7.png",
                        ".\\Resources\\player\\playerWalkL8.png", ]
        self.surface = pygame.transform.scale_by(pygame.image.load(".\\Resources\\player\\playerWalk1.png"), 1.5)
        self.rect = self.surface.get_rect()
        self.counter = 0
        self.facing_direction = "right"
        self.health = 100

    def playerInput(self):
        keys_pressed = pygame.key.get_pressed()
        if not self.rect.x < 0 or not self.rect.x > 1000:  # Player Input
            if keys_pressed[pygame.K_d]:
                if self.rect.right < screen.get_width() - 10:
                    self.surface = pygame.transform.scale_by(pygame.image.load(self.imagesL[self.counter]).convert_alpha(), 2.5)
                    self.counter = (self.counter + 1) % len(self.imagesL)
                    self.facing_direction = "right"
                    self.rect.x += 5
            if keys_pressed[pygame.K_a]:
                if self.rect.left > 10:
                    self.surface = pygame.transform.scale_by(pygame.image.load(self.imagesR[self.counter]).convert_alpha(), 2.5)
                    self.counter = (self.counter + 1) % len(self.imagesR)
                    self.facing_direction = "left"
                    self.rect.x += -5
            if keys_pressed[pygame.K_w]:
                if self.rect.top > 10:
                    if self.facing_direction == "left" and not keys_pressed[pygame.K_a] and not keys_pressed[pygame.K_d]:
                        self.surface = pygame.transform.scale_by(
                            pygame.image.load(self.imagesR[self.counter]).convert_alpha(), 2.5)
                        self.counter = (self.counter + 1) % len(self.imagesR)
                    elif not keys_pressed[pygame.K_a] and not keys_pressed[pygame.K_d]:
                        self.surface = pygame.transform.scale_by(
                            pygame.image.load(self.imagesL[self.counter]).convert_alpha(), 2.5)
                        self.counter = (self.counter + 1) % len(self.imagesL)
                    self.rect.y += -5
            if keys_pressed[pygame.K_s]:
                if self.rect.bottom < screen.get_height() - 10:
                    if self.facing_direction == "left" and not keys_pressed[pygame.K_a] and not keys_pressed[pygame.K_d]:
                        self.surface = pygame.transform.scale_by(
                            pygame.image.load(self.imagesR[self.counter]).convert_alpha(), 2.5)
                        self.counter = (self.counter + 1) % len(self.imagesR)
                    elif not keys_pressed[pygame.K_a] and not keys_pressed[pygame.K_d]:
                        self.surface = pygame.transform.scale_by(
                            pygame.image.load(self.imagesL[self.counter]).convert_alpha(), 2.5)
                        self.counter = (self.counter + 1) % len(self.imagesR)
                    self.rect.y += 5

    def draw(self):
        screen.blit(self.surface, self.rect)

    def update(self):
        self.playerInput()
        self.draw()
        if self.health == 0:
            quit()


# Fruitje
class Druif:
    def __init__(self, druif_id):
        self.id = druif_id
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
        screen.blit(rotated_image, self.rect)

    def collision(self):
        # if abs(player.rect.centerx - self.x) < 50 and abs(player.rect.centery - self.y) < 75:
        #     return True
        # else:
        #     return False
        if self.rect.colliderect(player.rect):
            return True
        else:
            return False

    def update(self):
        self.drawDruif()


class Attack_1:
    pass


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Ricky & Caas Productions")

# kleuren
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Zeus
zeus_sprite = pygame.transform.scale_by(pygame.image.load(".\\Resources\\zeus.png"), 0.35)
zeus_cloud_sprite = pygame.transform.scale_by(pygame.image.load("Resources/cloud.png"), 0.35)
zeus = zeus_sprite.get_rect()
zeus_cloud = zeus_cloud_sprite.get_rect()
zeus.center = ((screen.get_width() / 2) - 25, 100)
zeus_cloud.center = (465, 150)

# Player
player = Player()

# bg
bg_intro = pygame.transform.scale_by(pygame.image.load(".\\Resources\\temple_bg.png").convert(), 1.1)
bg_intro_rect = bg_intro.get_rect(center=(500, 300))
bg_surface = pygame.image.load("Resources\\Naamloos.png").convert()
bg_rect = bg_surface.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))

# text
# // coole font website: https://textcraft.net/
font = pygame.font.Font('.\\Resources\\fonts\\Pixeltype.ttf', 75)


def start_screen():
    ricasius_text = pygame.transform.scale_by(pygame.image.load("Resources/ricasius_text.png"), 1.25)
    ricasius_rect = ricasius_text.get_rect()
    ricasius_rect.center = (500, 100)

    battle_text = pygame.transform.scale_by(pygame.image.load("Resources/battle_text.png"), 0.5)
    battle_rect = battle_text.get_rect()
    battle_rect.center = (490, 175)

    press_space_text = pygame.transform.scale_by(pygame.image.load("Resources/press_space.png"), 0.75)
    press_space_rect = press_space_text.get_rect()
    press_space_rect.center = (500, 500)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
        screen.blit(bg_intro, bg_intro_rect)
        screen.blit(ricasius_text, ricasius_rect)
        screen.blit(battle_text, battle_rect)
        screen.blit(press_space_text, press_space_rect)
        pygame.display.update()
        clock.tick(MAX_FRAMERATE)

def draw_hp(hearts_left):
    if hearts_left >= 1:
        pass



def main():
    hp = 5
    counter = 0
    score = 0
    druifDict = {}
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        while counter < 3:
            druifDict[counter] = Druif(counter)
            counter += 1
        screen.blit(bg_surface, bg_rect)
        for i, druif in druifDict.items():
            druif.update()
            if druif.collision():
                druifDict[i] = Druif(i)
                score += 1
        player.update()
        screen.blit(zeus_sprite, zeus)
        screen.blit(zeus_cloud_sprite, zeus_cloud)
        screen.blit(font.render(f'Score: {score}', True, (0, 0, 0)), (25, screen.get_height() - 50))
        pygame.display.update()
        clock.tick(MAX_FRAMERATE)


if __name__ == "__main__":
    start_screen()
