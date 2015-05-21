
import pyglet
from random import random
from protozoa import Protozoa

class GAWindow(pyglet.window.Window):

    def __init__(self):
        super().__init__(600, 600)
        pyglet.clock.schedule_interval(self.update, 1.0/60.0)
        self.window_width, self.window_height = self.get_size()

        self.protozoa = []
        self.batch = pyglet.graphics.Batch()
        self.initialize() 
        
    def initialize(self):
        img = pyglet.resource.image("imgs/protozoa-green.png")

        for i in range(0, 10):
            x = random() * (self.window_width - 100) + 50
            y = random() * (self.window_height - 100) + 50
            self.protozoa.append(Protozoa((x, y), self.get_size(), img, self.batch))


    def on_draw(self):
        self.clear()
        self.batch.draw()

    def update(self, dt):
        for i in range(0, 10):
            self.protozoa[i].update()
        

   

def main():
    ga = GAWindow()
    pyglet.app.run()

if __name__ == '__main__':
    print(int('11111111', 2))
    main()
    