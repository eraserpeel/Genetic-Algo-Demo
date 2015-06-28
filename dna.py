
from random import random

class DNA:

    def __init__(self, num_genes):
        self.genes = []
        self.num_of_genes = 4
        for i in range(0, 8 * self.num_of_genes):
            self.genes.append(str(int(random() * 2)))

    def get_gene(self, gene_index):
        return int(''.join(self.genes[gene_index * 8:gene_index * 8 + 8]), 2)

