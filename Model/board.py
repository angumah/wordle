from Model.randWord import RandWord

class Board:
    def __init__(self, size):
        '''
        Constructs board object
        Parameters:
            size - length of word
            grid - grid size x size+1
            word - randomly generated word of length size
        '''
        self.size = size
        self.grid = [[0] * (size+1)] * (size)
        self.word = RandWord(self.size).generate()
        self.guessAttempt = 0
        print(self.word)
        


    def getRow(self):
        '''
        returns # of rows in grid
        '''
        return len(self.grid[0])
    

    def getCol(self):
        '''
        returns # of columns in grid
        '''
        return len(self.grid)
    

    def getGuessAttempt(self):
        """
        returns the current guess attempt
        """
        return self.guessAttempt
    def compChar(self, char1, char2):
        '''
        compares two characters ans returns whether they are equal.
        '''
        return char1 == char2

    def checkGuess(self, guess):
        '''
        checks the accuracy of each character in guess.
        returns a list of score values.
        score is either 0 1 or 2
        0 - letter not in word.
        1 - letter is in word but in the incorrect position.
        2 - letter is in word and in the correct position
        '''
        scores = []
        word = self.word
        for i in range(len(self.word)-1):
            wordChar = word[i:i+1]
            guessChar = guess[i:i+1]
            print(i)
            score = 0
            if word.find(guessChar) != -1:
                score+=1
                if self.compChar(wordChar, guessChar):
                    score+=1
                    word = word[0:i] + word[i+1:]
            scores.append(score)
        return scores


    def takeAttempt(self):
        """Increments attempts by 1"""
        self.guessAttempt+=1

    def endGame(self, guess):
        """
        Returns true if game has ended
        """

        if self.guessAttempt >= self.getRow():
            return True
        elif sum(self.checkGuess(guess)) >= 2*self.size:
            return True
        else:
            return False
    

        