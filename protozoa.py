
import pyglet
from random import random
from math import atan2

class Protozoa:

    def __init__(self, x, y, img, batch):
        self.x_delta = 0.5 - random() 
        self.y_delta = 0.5 - random()
        self.sprite = pyglet.sprite.Sprite(img, x, y, batch=batch)
        self.sprite.image.anchor_x = self.sprite.width / 2
        self.sprite.image.anchor_y = self.sprite.height / 2
        self.sprite.rotation = -(atan2(self.y_delta, self.x_delta) / (2 * 3.1459)) * 360 
        print(self.sprite.rotation)
        self.food_collected = 0
        self.genes = []
        self.initialize()

    def initialize(self):
        for i in range(0, 24):
            self.genes.append(int(random() * 2))
       

    def get_image(self):
        pass

    def update(self):
        #self.sprite.rotation = self.sprite.rotation + 1
        self.sprite.x = self.sprite.x + self.x_delta
        self.sprite.y = self.sprite.y + self.y_delta