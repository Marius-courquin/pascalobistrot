import unittest
from pascalobistrot.main import donne_a_boire


class MyTestCase(unittest.TestCase):
    def test_something(self):
        coup_a_boire = donne_a_boire(8, 10)
        self.assertEqual(coup_a_boire, 18)

    def test_something2(self):
        coup_a_boire = donne_a_boire(12, 10)
        self.assertEqual(24, coup_a_boire)  # add assertion here


if __name__ == '__main__':
    unittest.main()
