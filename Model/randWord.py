
import random
class RandWord:
    '''
    constructs RandWord object, takes in integer for word size
    '''
    def __init__(self, size):
        self.size = int(size)
        f = open("/Users/tngumah/Desktop/computing_fundamentals/Project/wordList.txt")
        wordArray = f.readlines()
        f.close()    

        self.filteredArray = [word for word in wordArray if len(word) == self.size+1]
    def generate(self):
        '''
        Filters wordList.txt by size variable to select a random word of x length.
        '''
        for word in self.filteredArray:
            print(word)
        return self.filteredArray[random.randint(0, len(self.filteredArray))]
    



        
    
    