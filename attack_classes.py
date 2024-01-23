import pygame


class Attacks:
    def __init__(self, screen, attack_id, player_rect):
        self.current_attack_area = []
        self.circles = []
        self.circle_locs = []
        self.screen = screen
        self.attack_id = attack_id
        self.player_rect = player_rect

    def drawGrid(self, attack_area):
        # de grid zelf
        blockSize = 50  # Set the size of the grid block
        for x in range(0, self.screen.get_width(), blockSize):
            for y in range(0, self.screen.get_height(), blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.screen, 'white', rect, 1)

        # de rode blokjes
        # attack_vakjes = [(5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (12, 5)]
        for x, y in self.current_attack_area:
            rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            pygame.draw.rect(self.screen, 'red', rect)

    # // aanval 1
    def attack_1(self):
        attack_vakjes_horizontal = [(x, y) for y in range(5, 7) for x in range(20)]
        self.current_attack_area = attack_vakjes_horizontal

    def attack_2(self):
        attack_vakjes = [(x, y) for y in range(12) for x in range(8, 11)]
        self.current_attack_area = attack_vakjes

    def attack_3(self):
        attack_vakjes = [(x, y) for y in range(5, 7) for x in range(0, 20)]
        for x in range(8, 11):
            for y in range(0, 12):
                attack_vakjes.append((x, y))
        self.current_attack_area = attack_vakjes

    def attack_4(self):
        attack_vakjes = [(x, y) for y in range(12) for x in range(10, 20)]
        self.current_attack_area = attack_vakjes

    def attack_5(self):
        attack_vakjes = [(x, y) for y in range(12) for x in range(9)]
        self.current_attack_area = attack_vakjes


    # // spawned de aanval en verzamelt locatie data
    def spawnattack(self):
        for location in self.current_attack_area:
            x_location = 50 + 50 * location[0]
            y_location = 50 + 50 * location[1]
            attack_circle = pygame.draw.circle(self.screen, 'red', (x_location - 25, y_location - 25), 25)
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
        print('check')
        if self.player_rect.collideobjects(self.circles):
            return 1
        else:
            return 0

    # // teken rode cirkels op het scherm
    def draw_attack(self):
        for loc in self.circle_locs:
            x_location, y_location = loc
            pygame.draw.circle(self.screen, 'red', (x_location - 25, y_location - 25), 25)

    def update(self):
        self.drawGrid(self.current_attack_area)
