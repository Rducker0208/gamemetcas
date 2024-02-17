import random

class Vaas:
    def __init__(self, screen):
        self.vaas_list = []
        self.screen = screen

    def spawn_vaas(self):
        spawn_location = random.randint(1, 20)
        if 15 > spawn_location > 3:
            x = random.randint(25, self.screen.get_width() - 25)
            y = random.randint(288, self.screen.get_height() - 25)

        # // links van zeus
        elif spawn_location <= 3:
            x = random.randint(25, 338)
            y = random.randint(85, 100)

        # // rechts van zeus
        else:
            x = random.randint(612, self.screen.get_width() - 25)
            y = random.randint(50, 100)

        self.vaas_list.append((x, y))