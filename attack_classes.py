import pygame


class Attack_1:
    def __init__(self, screen, id):
        self.screen = screen
        self.id = id

    def drawGrid(self):
        # de grid zelf
        blockSize = 50  # Set the size of the grid block
        for x in range(0, self.screen.get_width(), blockSize):
            for y in range(0, self.screen.get_height(), blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.screen, 'white', rect, 1)
        # de rode blokjes
        attack_vakjes = [(5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (12, 5)]
        for x, y in attack_vakjes[0:]:
            rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            pygame.draw.rect(self.screen, 'red', rect)

    def update(self):
        self.drawGrid()
