
import pyglet
from random import random
from math import sqrt

class Food:

    def __init__(self, dimensions, food_image, batch):
        self.sprite = pyglet.sprite.Sprite(food_image, batch=batch)
        self.sprite.x = random() * dimensions[0]
        self.sprite.y = random() * dimensions[1]

    def is_eaten(self, location):
        if sqrt(((location[0] - self.sprite.x) * (location[0] - self.sprite.x)) +
                ((location[1] - self.sprite.y) * (location[1] - self.sprite.y))) < 7:
            self.sprite.batch = None
            return True
        return False






