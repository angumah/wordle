import unittest

# Wordle tester class

# Test Board class
import unittest
from Model.randWord import RandWord
from Model.board import Board

class BoardTests(unittest.TestCase):
    def setUp(self):
        self.size = 5
        self.board = Board(self.size)

    def test_board_properties(self):
        self.assertEqual(self.board.size, self.size)
        self.assertEqual(len(self.board.grid), self.size)
        self.assertEqual(len(self.board.grid[0]), self.size+1)

    def test_guess_attempt(self):
        self.assertEqual(self.board.getGuessAttempt(), 0)
        self.board.takeAttempt()
        self.assertEqual(self.board.getGuessAttempt(), 1)

    def test_compChar(self):
        self.assertTrue(self.board.compChar('a', 'a'))
        self.assertFalse(self.board.compChar('a', 'b'))

    def test_checkGuess(self):
        scores = self.board.checkGuess('hello')
        self.assertEqual(len(scores), self.size)
        self.assertTrue(all(s in [0, 1, 2] for s in scores))

    def test_endGame(self):
        self.assertFalse(self.board.endGame('hello'))
        for i in range(self.board.getRow()):
            self.board.takeAttempt()
        self.assertTrue(self.board.endGame('hello'))
        self.assertTrue(self.board.endGame('helle'))

if __name__ == '__main__':
    unittest.main()
