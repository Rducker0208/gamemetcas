import pygame

from zeus_class import Zeus
from player_class import Player
from druif_class import Druif

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

# Zeus
zeus = Zeus(screen)

# Player
player = Player(screen)

# bg
bg_intro = pygame.transform.scale_by(pygame.image.load("Resources/background/temple_bg.png").convert(), 1.1)
bg_intro_rect = bg_intro.get_rect(center=(500, 300))
bg_surface = pygame.image.load("Resources/background/Naamloos.png").convert()
bg_rect = bg_surface.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))

# text
# // coole font website: https://textcraft.net/
font = pygame.font.Font('.\\Resources\\fonts\\Pixeltype.ttf', 75)


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


def draw_hp(hearts_left):
    empty_heart = pygame.transform.scale_by(pygame.image.load("Resources\\hearts\\background.png"), 3)
    heart_border = pygame.transform.scale_by(pygame.image.load("Resources\\hearts\\border.png"), 3)
    heart = pygame.transform.scale_by(pygame.image.load("Resources\\hearts\\heart.png"), 3)

    empty_heart_rect_1 = empty_heart.get_rect()
    empty_heart_rect_2 = empty_heart.get_rect()
    empty_heart_rect_3 = empty_heart.get_rect()
    empty_heart_rect_4 = empty_heart.get_rect()
    empty_heart_rect_5 = empty_heart.get_rect()

    heart_border_1 = heart_border.get_rect()
    heart_border_2 = heart_border.get_rect()
    heart_border_3 = heart_border.get_rect()
    heart_border_4 = heart_border.get_rect()
    heart_border_5 = heart_border.get_rect()

    heart_1 = heart.get_rect()
    heart_2 = heart.get_rect()
    heart_3 = heart.get_rect()
    heart_4 = heart.get_rect()
    heart_5 = heart.get_rect()

    heart_border_1.center = (30, 40)
    screen.blit(heart_border, heart_border_1)

    heart_border_2.center = (80, 40)
    screen.blit(heart_border, heart_border_2)

    heart_border_3.center = (130, 40)
    screen.blit(heart_border, heart_border_3)

    heart_border_4.center = (180, 40)
    screen.blit(heart_border, heart_border_4)

    heart_border_5.center = (230, 40)
    screen.blit(heart_border, heart_border_5)

    if hearts_left >= 1:
        heart_1.center = (30, 40)
        screen.blit(heart, heart_1)
    else:
        empty_heart_rect_1.center = (30, 40)
        screen.blit(empty_heart, empty_heart_rect_1)

    if hearts_left >= 2:
        heart_2.center = (80, 40)
        screen.blit(heart, heart_2)
    else:
        empty_heart_rect_2.center = (80, 40)
        screen.blit(empty_heart, empty_heart_rect_2)

    if hearts_left >= 3:
        heart_3.center = (130, 40)
        screen.blit(heart, heart_3)
    else:
        empty_heart_rect_3.center = (130, 40)
        screen.blit(empty_heart, empty_heart_rect_3)

    if hearts_left >= 4:
        heart_4.center = (180, 40)
        screen.blit(heart, heart_4)
    else:
        empty_heart_rect_4.center = (180, 40)
        screen.blit(empty_heart, empty_heart_rect_4)

    if hearts_left >= 5:
        heart_5.center = (230, 40)
        screen.blit(heart, heart_5)
    else:
        empty_heart_rect_5.center = (230, 40)
        screen.blit(empty_heart, empty_heart_rect_5)


def main():
    counter = 0
    score = 0
    ticks = 0
    druifDict = {}
    while True:
        ticks += 1
        if ticks % 300 == 0:
            player.health -= 1
            print('min health')
            print(player.health)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        while counter < 3:
            druifDict[counter] = Druif(counter, screen, player)
            counter += 1
        screen.blit(bg_surface, bg_rect)
        for druif_id, druif in druifDict.items():
            druif.update()
            if druif.collision():
                druifDict[druif_id] = Druif(druif_id, screen, player)
                if player.health < 5:
                    player.health += 1
                score += 1
        if player.health <= 0:
            start_screen()
            break
        player.update()
        zeus.update()
        draw_hp(player.health)
        screen.blit(font.render(f'Score: {score}', True, (0, 0, 0)), (25, screen.get_height() - 50))
        pygame.display.update()
        clock.tick(MAX_FRAMERATE)


if __name__ == "__main__":
    start_screen()

# yo