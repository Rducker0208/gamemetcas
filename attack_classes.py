import pygame
import random


class Attacks:
    def __init__(self, screen, attack_id, player_rect):
        self.current_attack_area = []
        self.circles = []
        self.circle_locs = []
        self.screen = screen
        self.attack_id = attack_id
        self.player_rect = player_rect
        self.current_attack = None
        self.color = 'green'

    def drawGrid(self):
        # de grid zelf
        blockSize = 50  # Set the size of the grid block
        for x in range(0, self.screen.get_width(), blockSize):
            for y in range(0, self.screen.get_height(), blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.screen, 'white', rect, 1)

        for x, y in self.current_attack_area:
            rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            pygame.draw.rect(self.screen, 'red', rect)

    # // aanval 1
    def attack_1(self):
        attack_vakjes_horizontal = [(x, y) for y in range(5, 7) for x in range(20)]
        self.current_attack_area = attack_vakjes_horizontal

    def attack_2(self):
        attack_vakjes = [(x, y) for y in range(4, 12) for x in range(8, 12)]
        attack_vakjes.extend([(0, 11), (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5), (7, 4)])
        attack_vakjes.extend([(12, 4), (13, 5), (14, 6), (15, 7), (16, 8), (17, 9), (18, 10), (19, 11)])
        attack_vakjes.extend([(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4)])
        attack_vakjes.extend([(13, 4), (14, 4), (15, 4), (16, 4), (17, 4), (18, 4), (19, 4)])
        attack_vakjes.extend([(7, 5), (12, 5)])
        self.current_attack_area = attack_vakjes

    def attack_3(self):
        attack_vakjes = [(x, y) for y in range(5, 7) for x in range(0, 20)]
        attack_vakjes.extend([(x, y) for x in range(8, 12) for y in range(4, 12)])
        self.current_attack_area = attack_vakjes

    def attack_4(self):
        attack_vakjes = [(x, y) for y in range(12) for x in range(11, 20)]
        self.current_attack_area = attack_vakjes

    def attack_5(self):
        attack_vakjes = [(x, y) for y in range(12) for x in range(9)]
        self.current_attack_area = attack_vakjes

    # // spawned de aanval en verzamelt locatie data
    def spawnattack(self):
        location = random.randint(1, 60)
        self.color = 'green'
        if 15 >= location >= 1:
            self.current_attack = 1
            self.attack_1()
        if 30 >= location >= 16:
            self.current_attack = 2
            self.attack_2()
        if 40 >= location >= 31:
            self.current_attack = 3
            self.attack_3()
        if 50 >= location >= 41:
            self.current_attack = 4
            self.attack_4()
        if 60 >= location >= 51:
            self.current_attack = 5
            self.attack_5()

        for location in self.current_attack_area:
            x_location = 50 + 50 * location[0]
            y_location = 50 + 50 * location[1]
            attack_circle = pygame.draw.circle(self.screen, self.color, (x_location - 25, y_location - 25), 25)
            self.circles.append(attack_circle)
            self.circle_locs.append((x_location, y_location))

        pygame.display.update()

    # // despawned aanval
    def remove_attack(self):
        self.circles = []
        self.current_attack_area = []
        self.circle_locs = []

    # // check for collision
    def check_damage(self):
        self.color = 'red'
        if self.player_rect.collideobjectsall(self.circles):
            return 1
        else:
            return 0
        # return len(self.player_rect.collideobjectsall(self.circles))

    # // teken rode cirkels op het scherm
    def draw_attack(self):
        for loc in self.circle_locs:
            x_location, y_location = loc
            pygame.draw.circle(self.screen, self.color, (x_location - 25, y_location - 25), 25)
