
import pyglet
from random import random
from math import atan2, sin, cos

class Protozoa:

    #location (x, y) and window_size (width, height)
    def __init__(self, location, window_size, image, batch):
        self.window_width, self. window_height = window_size
        self.initialize_image(image, batch)
        self.initialize_genes()
        self.initialize_attributes(location)
    
    def initialize_image(self, image, batch):
        self.sprite = pyglet.sprite.Sprite(image, batch=batch)
        self.sprite.image.anchor_x = self.sprite.width / 2
        self.sprite.image.anchor_y = self.sprite.height / 2
    
    def initialize_genes(self):
        self.genes = []
        self.num_of_genes = 4
        for i in range(0, 8 * self.num_of_genes):
            self.genes.append(str(int(random() * 2)))
        self.probability_of_turn = int(''.join(self.genes[0:8]), 2) / 2550.0
        self.angle_of_rotation = int(''.join(self.genes[0:8]), 2) / 255.0 * 360 - 180
        self.speed = int(''.join(self.genes[0:8]), 2) / 255.0 * 10

    def initialize_attributes(self, location):
        self.sprite.x, self.sprite.y = location
        self.x_delta = (random() - 0.5) * self.speed
        self.y_delta = (random() - 0.5) * self.speed
        self.sprite.rotation = -(atan2(self.y_delta, self.x_delta) / (2 * 3.1459)) * 360 
        self.rotation = random() * 360
        self.metabolic_rate = self.speed
        self.life = 1000
    
    def update(self):
        if self.is_turning():
            self.sprite.rotation += self.angle_of_rotation + (random()
            self.x_delta = -sin(self.sprite.rotation/360.0 * 2 * 3.1459)
            self.y_delta = cos(self.sprite.rotation/360.0 * 2 * 3.1459)
            self.sprite.rotation = -(atan2(self.y_delta, self.x_delta) / (2 * 3.1459)) * 360 

        self.sprite.x = self.sprite.x + self.x_delta
        self.sprite.y = self.sprite.y + self.y_delta

        if self.is_x_off_map(): 
            self.sprite.x = self.sprite.x - self.x_delta

        if self.is_y_off_map():
            self.sprite.y = self.sprite.y - self.y_delta            


    def is_turning(self):
        if random() < self.probability_of_turn:
            return True
        return False

    def is_y_off_map(self):
        if self.sprite.y < 20 or self.sprite.y > self.window_height - 20:
            return True
        return False

    def is_x_off_map(self):
        if self.sprite.x < 20 or self.sprite.x > self.window_height - 20:
            return True
        return False