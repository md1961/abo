from enum import Enum, auto

class BloodType(Enum):
    A  = auto()
    B  = auto()
    O  = auto()
    AB = auto()

    @classmethod
    def of(cls, gene_pair):
        genes = sorted(list(set(gene_pair.genes)))
        if len(genes) == 2 and genes[-1] == BloodTypeGene.O:
            genes.pop() 
        type_name = ''.join(map(lambda gene: gene.name, genes))
        return cls[type_name]

class BloodTypeGene(Enum):
    A = auto()
    B = auto()
    O = auto()

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return self.name

class BloodTypeGenePair:
    def __init__(self, gene0, gene1):
        self.genes = tuple(sorted([gene0, gene1]))
        self.blood_type = BloodType.of(self)

    def __str__(self):
        return ''.join(map(str, self.genes))
