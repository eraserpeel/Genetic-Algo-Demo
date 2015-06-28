
import pyglet
from random import random
from math import atan2, sin, cos
from dna import DNA

class Creature:
    TWO_PI = 6.283185

    #location (x, y) and window_size (width, height)
    def __init__(self, location, window_size, image, batch, dna = None):
        self.window_width, self.window_height = window_size
        self.initialize_image(image, batch)
        self.initialize_genes(dna)
        self.initialize_attributes(location)

    def initialize_image(self, image, batch):
        self.sprite = pyglet.sprite.Sprite(image, batch=batch)
        self.sprite.image.anchor_x = self.sprite.width / 2
        self.sprite.image.anchor_y = self.sprite.height / 2
        self.sprite_boundary_width = self.sprite.width / 2
        self.sprite_boundary_height = self.sprite.height / 2

    def initialize_genes(self, dna):
        if dna is not None:
            self.dna = dna
        else:
            self.dna = DNA(4)

        self.probability_of_turn = self.dna.get_gene(0) * 0.1 / 100
        self.angle_of_rotation = self.dna.get_gene(1) / 255 * self.TWO_PI
        self.speed = self.dna.get_gene(2) / 255.0 * 10
        self.probability_turn_direction = self.dna.get_gene(3) / 255.0 * 10

    def initialize_attributes(self, location):
        self.sprite.x, self.sprite.y = location
        self.x_delta = (random() - 0.5) * self.speed
        self.y_delta = (random() - 0.5) * self.speed
        self.metabolic_rate = self.speed
        self.rotation = self.angle_of_rotation
        self.life = 200
        self.cycles = 0
        self.sprite.rotation = -(atan2(self.y_delta, self.x_delta) / self.TWO_PI) * 360

    def update(self):
        if not self.is_alive():
            self.remove_sprite()
            return

        if self.is_turning():
            dir_r = 1
            if random() < 0.5:
                dir_r = -1
            self.rotation = (self.rotation + dir_r * self.angle_of_rotation) % self.TWO_PI
            self.x_delta = -sin(self.rotation)
            self.y_delta = cos(self.rotation)
            self.sprite.rotation = -(atan2(self.y_delta, self.x_delta) / self.TWO_PI) * 360

        self.sprite.x = self.sprite.x + self.x_delta
        self.sprite.y = self.sprite.y + self.y_delta

        if self.is_x_off_map(): 
            self.sprite.x = self.sprite.x - self.x_delta

        if self.is_y_off_map():
            self.sprite.y = self.sprite.y - self.y_delta

        self.life -= self.metabolic_rate
        self.cycles += 1

    def is_turning(self):
        if random() < self.probability_of_turn:
            return True
        return False

    def is_y_off_map(self):
        if self.sprite.y < self.sprite_boundary_height or \
           self.sprite.y > self.window_height - self.sprite_boundary_height:
            return True
        return False

    def is_x_off_map(self):
        if self.sprite.x < self.sprite_boundary_width or \
           self.sprite.x > self.window_height - self.sprite_boundary_width:
            return True
        return False

    def get_location(self):
        return (self.sprite.x, self.sprite.y)

    def add_life(self):
        self.life += 100

    def is_alive(self):
        if self.life <= 0:
            return False
        return True

    def remove_sprite(self):
        self.sprite.batch = None