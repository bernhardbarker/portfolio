import unittest
import tabletennis

class TestRandomGen(unittest.TestCase):
    def test_50_p_to_21(self):
        self.assertAlmostEqual(tabletennis.win_probability(0.5, 21),
                               0.5,
                               places=8)

    def test_100_p_to_21(self):
        self.assertEqual(tabletennis.win_probability(1, 21),
                         1)

    def test_0_p_to_21(self):
        self.assertEqual(tabletennis.win_probability(0, 21),
                         0)

    def test_60_p_to_21(self):
        self.assertAlmostEqual(tabletennis.win_probability(0.6, 21),
                               0.909,
                               places=3)

    def test_40_p_to_21(self):
        self.assertAlmostEqual(tabletennis.win_probability(0.4, 21),
                               0.091,
                               places=3)

    def test_51_p_to_4(self):
        self.assertAlmostEqual(tabletennis.win_probability(0.51, 4),
                               0.52498501,
                               places=8)

    def test_90_p_to_4(self):
        self.assertAlmostEqual(tabletennis.win_probability(0.9, 4),
                               0.99855220,
                               places=8)

if __name__ == '__main__':
    unittest.main()

