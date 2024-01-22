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
    ricasius_text = pygame.transform.scale_by(pygame.image.load("Resources/text/ricasius_text.png"), 1.25)
    ricasius_rect = ricasius_text.get_rect()
    ricasius_rect.center = (500, 100)

    battle_text = pygame.transform.scale_by(pygame.image.load("Resources/text/battle_text.png"), 0.5)
    battle_rect = battle_text.get_rect()
    battle_rect.center = (490, 175)

    press_space_text = pygame.transform.scale_by(pygame.image.load("Resources/text/press_space.png"), 0.75)
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
    if hearts_left >= 2:
        pass
    if hearts_left >= 3:
        pass
    if hearts_left >= 4:
        pass
    if hearts_left >= 5:
        pass


def main():
    counter = 0
    score = 0
    druifDict = {}
    while True:
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
                score += 1
        player.update()
        zeus.update()
        screen.blit(font.render(f'Score: {score}', True, (0, 0, 0)), (25, screen.get_height() - 50))
        pygame.display.update()
        clock.tick(MAX_FRAMERATE)


if __name__ == "__main__":
    start_screen()
