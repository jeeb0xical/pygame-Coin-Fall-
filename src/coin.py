################
# Coin class
################
import random

class Coin():
    def __init__(self, res, size):
        self.image = res.coin_img
        self.x = random.randint(0, size[0] - 55)
        self.y = -15

    def fall(self):
        self.y += 7  # Change the value if necessary

    def draw(self, surface):
        try:
            surface.blit(self.image, (self.x, self.y))
        except AttributeError:
            pass