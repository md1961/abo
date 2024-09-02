from blood_type import *

class Person:
    def __init__(self, blood_type_gene_pair):
        self.gene_pair = blood_type_gene_pair

    @classmethod
    def create_from_gene_str(cls, gene_str):
        blood_type_gene_pair = BloodTypeGenePair.create_from_gene_str(gene_str)
        return cls(blood_type_gene_pair)

    @property
    def blood_type(self):
        return self.gene_pair.blood_type


if __name__ == '__main__':
    str_genes = list('ABO')
    for g1 in str_genes:
        for g2 in str_genes:
            person = Person.create_from_gene_str(g1 + g2)
            print(f'{g1} & {g2}  =>  {person.blood_type}')
