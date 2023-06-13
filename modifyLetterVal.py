class letterVals:
    def __init__(self) -> None:
        self.map = {}

    def modify(self, letter, val):
        self.map[letter] = val

    def modifyLetterList(self, letters, vals):
        l = len(letters)
        for i in range(0, l):
            self.modify(letter=letters[i], val=vals[i])
    
    def getMap(self, letter):
        return self.map[letter]

letters = letterVals()