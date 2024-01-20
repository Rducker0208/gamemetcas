import pygame
from sys import exit
MAX_FRAMERATE = 60
SCREEN_SIZE = (1000, 600)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill((255, 255, 255))
pygame.display.set_caption("Ricky & Caas Productions")

# kleuren
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#player
player = pygame.Rect(500, 300, 50, 100)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_d]:
            player.x += 5
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, player)
        pygame.display.update()
        clock.tick(MAX_FRAMERATE)

main()