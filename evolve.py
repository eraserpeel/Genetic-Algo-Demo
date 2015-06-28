
from creature import Creature

class Evolve:

    def __init__(self):
        self.generations = []
        self.generation_count = 0

    def next_generation(self, creatures, percentage_to_take):
        creatures.sort(key=lambda c: c.cycles)
        for i in creatures:
            print(i.cycles, i.metabolic_rate)
