#Test random word class
import unittest
from Model.randWord import RandWord

class TestRandWord(unittest.TestCase):
    def setUp(self):
        self.word = RandWord(5)

    def test_generate(self):
        # Test that the generated word is of the correct length
        self.assertEqual(len(self.word.generate()), 6)

        # Test that the generated word is in the filtered word list
        self.assertIn(self.word.generate(), self.word.filteredArray)

if __name__ == '__main__':
    unittest.main()
