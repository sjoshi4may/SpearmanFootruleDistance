import unittest
from sumSpearmanDistances import sumSpearmanDistances

class TestSumSpearmanDistances(unittest.TestCase):

    def test_case1(self):
        scores = {'A' : (100,0.1),'B' : (90,0.3),'C' : (20, 0.2)}
        proposedRank = ['A', 'B', 'C']
        self.assertEqual(sumSpearmanDistances(scores,proposedRank), 4)

    def test_case2(self):
        scores = {'A' : (100,0.1),'B' : (90,0.3),'C' : (20, 0.2)}
        proposedRank = ['C', 'A', 'B']
        self.assertEqual(sumSpearmanDistances(scores,proposedRank), 8)

    def test_case3(self):
        scores = {'A' : (100,0.1),'B' : (90,0.3),'C' : (20, 0.2)}
        proposedRank = ['C', 'B', 'A']
        self.assertEqual(sumSpearmanDistances(scores,proposedRank), 6)

    def test_rank_collisions(self):
        scores = {'A' : (100,0.1), 'B' : (90,0.3), 'C' : (20, 0.2),
                 'D' : (100,0.1), 'E' : (90,0.3)}
        proposedRank = ['A','B','C','D','E']
        self.assertEqual(sumSpearmanDistances(scores,proposedRank), 16)


    def test_raise_proposed_rank(self):
        scores = {'A' : (100,0.1),'B' : (90,0.3),'C' : (20, 0.2)}
        proposedRank = []
        with self.assertRaises(Exception) as err:
            sumSpearmanDistances(scores,proposedRank)
        self.assertEqual(str(err.exception), "Sorry, proposed rank is not provided.")

    def test_raise_scores(self):
        scores = {}
        proposedRank = ['A','B','C']
        with self.assertRaises(Exception) as err:
            sumSpearmanDistances(scores,proposedRank)
        self.assertEqual(str(err.exception), "Sorry, no scores are provided.")


    def test_partial_ranking1(self):
        scores = {'A' : (100,0.1),'B' : (90,0.3)}
        proposedRank = ['A','B','C']
        with self.assertRaises(Exception) as err:
            sumSpearmanDistances(scores,proposedRank)
        self.assertEqual(str(err.exception),"Items in scores and proposed rank are different")

    def test_partial_ranking2(self):
        scores = {'A' : (100,0.1),'B' : (90,0.3), 'B' : (90,0.3)}
        proposedRank = ['A','B','C']
        with self.assertRaises(Exception) as err:
            sumSpearmanDistances(scores,proposedRank)
        self.assertEqual(str(err.exception),"Items in scores and proposed rank are different")

if __name__=='__main__':
    unittest.main(verbosity=2)
