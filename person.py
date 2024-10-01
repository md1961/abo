from blood_type import *

class Person:
    def __init__(self, blood_type_gene_pair):
        self.gene_pair = blood_type_gene_pair

    @property
    def blood_type(self):
        return self.gene_pair.blood_type
