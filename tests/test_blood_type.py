import unittest

from blood_type import *

class TestBloodType(unittest.TestCase):

    def test_of(self):
        test_patterns = (
            (BloodTypeGene.A, BloodTypeGene.A, BloodType.A ),
            (BloodTypeGene.A, BloodTypeGene.B, BloodType.AB),
            (BloodTypeGene.A, BloodTypeGene.O, BloodType.A ),
            (BloodTypeGene.B, BloodTypeGene.A, BloodType.AB),
            (BloodTypeGene.B, BloodTypeGene.B, BloodType.B ),
            (BloodTypeGene.B, BloodTypeGene.O, BloodType.B ),
            (BloodTypeGene.O, BloodTypeGene.A, BloodType.A ),
            (BloodTypeGene.O, BloodTypeGene.B, BloodType.B ),
            (BloodTypeGene.O, BloodTypeGene.O, BloodType.O ),
        )

        for gene1, gene2, expected in test_patterns:
            with self.subTest(gene1=gene1, gene2=gene2):
                gene_pair = BloodTypeGenePair(gene1, gene2)
                actual = BloodType.of(gene_pair)
                self.assertEqual(actual, expected)
