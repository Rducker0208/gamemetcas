import pygame

import druif_class
from zeus_class import Zeus
from player_class import Player
from druif_class import Druif
from hearts_class import hearts

MAX_FRAMERATE = 60
SCREEN_SIZE = (1000, 600)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Ricky & Caas Productions")

# kleuren
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# fonts
# // coole font website: https://textcraft.net/
font = pygame.font.Font('.\\Resources\\fonts\\Pixeltype.ttf', 75)

# Zeus
zeus = Zeus(screen)

# Player
player = Player(screen)

# hearts
heart_bar = hearts(screen)

# bg
bg_intro = pygame.transform.scale_by(pygame.image.load("Resources/background/temple_bg.png").convert(), 1.1)
bg_intro_rect = bg_intro.get_rect(center=(500, 300))
bg_surface = pygame.image.load("Resources/background/Naamloos.png").convert()
bg_rect = bg_surface.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))

# score
score_druif_image = pygame.transform.scale_by(pygame.image.load("Resources/grape.png"), 0.60)
score_druif_rect = score_druif_image.get_rect()
score_druif_rect.center = (screen.get_width() - 40, 30)


def start_screen():
    player.health = 5
    ricasius_text = pygame.transform.scale_by(pygame.image.load("Resources/text/Ricasius.png"), 1.25)
    ricasius_rect = ricasius_text.get_rect()
    ricasius_rect.center = (500, 100)

    battle_text = pygame.transform.scale_by(pygame.image.load("Resources/text/battle-with-zeus.png"), 1)
    battle_rect = battle_text.get_rect()
    battle_rect.center = (500, 185)

    press_space_text = pygame.transform.scale_by(pygame.image.load("Resources/text/press-space-to-start.png"), 0.75)
    press_space_rect = press_space_text.get_rect()
    press_space_rect.center = (500, 550)

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


def update_score(score):
    screen.blit(score_druif_image, score_druif_rect)
    if score < 10:
        screen.blit(font.render(str(score), True, (0, 0, 0)), (screen.get_width() - 100, 20))
    elif score < 100:
        screen.blit(font.render(str(score), True, (0, 0, 0)), (screen.get_width() - 120, 20))
    elif score < 1000:
        screen.blit(font.render(str(score), True, (0, 0, 0)), (screen.get_width() - 140, 20))
    else:
        screen.blit(font.render(str(score), True, (0, 0, 0)), (screen.get_width() - 160, 20))



def main():
    counter = 0
    score = 0
    ticks = 0
    druifDict = {}
    while True:
        ticks += 1

        # // test die elke 5 sec triggered
        # if ticks % 300 == 0:
        #     player.health -= 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.blit(bg_surface, bg_rect)
        update_score(score)
        player.update()
        zeus.update()
        heart_bar.update_hearts(player.health)

        while counter < 3:
            druifDict[counter] = Druif(counter, screen, player)
            counter += 1

        for druif_id, druif in druifDict.items():
            druif.update()
            if druif.collision():
                druifDict[druif_id] = Druif(druif_id, screen, player)
                score += 1

        if player.health <= 0:
            return start_screen()
        pygame.display.update()
        clock.tick(MAX_FRAMERATE)


if __name__ == "__main__":
    start_screen()

# yo
