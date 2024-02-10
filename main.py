import random
import time

import pygame

from zeus_class import Zeus
from player_class import Player
from druif_class import Druif
from hearts_class import hearts
from attack_classes import Attacks
from loot_vaas_class import Vaas
from thunder_class import thunder

MAX_FRAMERATE = 60
SCREEN_SIZE = (1000, 600)

pygame.init()
pygame.mixer.init()
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
alpha_surface = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA)
# Player
player = Player(screen)

# Zeus
zeus = Zeus(screen)
attacks = Attacks(screen, alpha_surface, 1, player.rect)

# hearts
heart_bar = hearts(screen)

# vaas
vaas = Vaas(screen)
vaas_sprite = pygame.transform.scale_by(pygame.image.load("Resources/vaas.png"), 0.2)
vaas_rect = vaas_sprite.get_rect()

# voet
voet_sprite = pygame.transform.scale_by(pygame.image.load("Resources/schoen_met_vleugels.png"), 0.15)
voet_rect = voet_sprite.get_rect()
voet_rect.center = (30, 100)

# bg
bg_intro = pygame.transform.scale_by(pygame.image.load("Resources/background/temple_bg.png").convert(), 1.1)
bg_intro_rect = bg_intro.get_rect(center=(500, 300))

bg_surface = pygame.image.load("Resources/background/Naamloos.png").convert_alpha()
bg_rect = bg_surface.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))

# score
score_druif_image = pygame.transform.scale_by(pygame.image.load("Resources/grape.png"), 0.60)
score_druif_rect = score_druif_image.get_rect()
score_druif_rect.center = (screen.get_width() - 40, 30)

# thunder
pygame.mixer.music.load('Resources/soundeffects/thunder_sfx.mp3')
pygame.mixer.music.set_volume(.5)


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


def game_over_screen():
    pass


def update_effect(ticks_since_start):
    time_left = 600 - ticks_since_start
    time_left /= 60
    time_left = round(time_left)
    screen.blit(voet_sprite, voet_rect)
    screen.blit(font.render(str(time_left), True, (0, 0, 0)), (60, 85))


def main():
    score = 0
    ticks = 0
    wait = 0
    effect_ticks = 0
    druifDict = {}
    grid_toggled = False
    attack_on_field = False
    effect = False
    thunder_sprite = None

    for i in range(3):
        druifDict[i] = Druif(i, screen, player)

    while True:
        ticks += 1
        effect_ticks += 1
        if player.health <= 0:
            return start_screen()

        screen.blit(bg_surface, bg_rect)
        screen.blit(alpha_surface, (0, 0))
        # // elke 5 seconden wordt er een aanval gestart of gestopt
        if ticks % 300 == 0:
            if attack_on_field is False:
                attacks.spawnattack()
                attack_on_field = True

        if effect_ticks % 600 == 0:
            player.movement_speed = 4
            effect = False

        if effect is True:
            update_effect(effect_ticks)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    if grid_toggled:
                        grid_toggled = False
                    else:
                        grid_toggled = True

        for druif_id, druif in druifDict.items():
            druif.update()
            if druif.collision():
                chance = random.randint(1, 20)
                if chance == 1:
                    vaas.spawn_vaas()
                druifDict[druif_id] = Druif(druif_id, screen, player)
                score += 1

        for vaas_loc in vaas.vaas_list:
            vaas_rect.center = (vaas_loc[0], vaas_loc[1])
            if abs(player.rect.center[0] - vaas_rect.center[0]) < 25 and abs(
                    player.rect.center[1] - vaas_rect.center[1]) < 50:  # noqa
                vaas.vaas_list.remove(vaas_loc)
                if player.health < 5:
                    if random.randint(1, 2) == 1:
                        player.health += 1
                    else:
                        effect = True
                        player.movement_speed = 6
                        effect_ticks = 0
                else:
                    effect = True
                    player.movement_speed = 6
                    effect_ticks = 0
            screen.blit(vaas_sprite, vaas_rect)

        if grid_toggled:
            attacks.drawGrid()

        if attack_on_field is True:
            attacks.draw_attack()
            if wait >= 120:
                player.health -= attacks.check_damage()
                attack_on_field = False
                pygame.mixer.music.play()
                thunder_sprite = thunder(screen, attacks.circle_locs)
                wait = 0
            else:
                wait += 1
        if thunder_sprite:
            if not thunder_sprite.ended():
                thunder_sprite.update()
                attacks.draw_attack()
            else:
                thunder_sprite = None
                attacks.remove_attack()
                alpha_surface.fill(pygame.Color(0, 0, 0, 0))
        player.update()
        update_score(score)
        zeus.update()
        heart_bar.update_hearts(player.health)
        pygame.display.update()
        clock.tick(MAX_FRAMERATE)


if __name__ == "__main__":
    start_screen()
