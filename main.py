
import pyglet
from random import random
from creature import Creature
from food import Food
from evolve import Evolve

class GAWindow(pyglet.window.Window):

    def __init__(self):
        super().__init__(600, 600)
        pyglet.clock.schedule_interval(self.update, 1.0/60.0)
        self.flag = False
        self.cycles = 0
        self.window_width, self.window_height = self.get_size()
        self.creatures = []
        self.food = []
        self.num_of_creatures = 100
        self.num_of_food = 10
        self.environment = None
        self.batch = pyglet.graphics.Batch()
        self.initialize()

    def initialize(self):
        creature_img = pyglet.resource.image("imgs/protozoa-green-small.png")
        for i in range(0, self.num_of_creatures):
            x = random() * (self.window_width - 100) + 50
            y = random() * (self.window_height - 100) + 50
            self.creatures.append(Creature((x, y), self.get_size(), creature_img, self.batch))

        food_img = pyglet.resource.image("imgs/food.png")
        for i in range(0, self.num_of_food):
            self.food.append(Food(self.get_size(), food_img, self.batch))

    def on_draw(self):
        self.clear()
        self.batch.draw()

    def update(self, dt):
        if self.cycles == 200:
            e = Evolve()
            e.next_generation(self.creatures, 0.0)
        self.cycles += 1
        for i in range(0, len(self.creatures)):
            self.creatures[i].update()
            for j in range(0, self.num_of_food):
                if self.food[j].is_eaten(self.creatures[i].get_location()):
                    self.creatures[i].add_life()

        self.creatures = [creature for creature in self.creatures if creature.is_alive()]
        print(len(self.creatures))


def main():
    ga = GAWindow()
    pyglet.app.run()

if __name__ == '__main__':
    main()
