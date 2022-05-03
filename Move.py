class Move:
    MOVES_DICTIONARY = {}
    def __init__(self, move):
        moveInfo = []
        if len(Move.MOVES_DICTIONARY) == 0:
            file = open('pokemon Moves.csv', 'r')
            for line in file:
                line = line.strip()
                moveList = line.split(",")
                Move.MOVES_DICTIONARY[moveList[1]] = moveList
                # Name of the move is a key, rest is the value

            file.close()
        
        for key in Move.MOVES_DICTIONARY:
            if key.lower() == move.lower():
                moveInfo = Move.MOVES_DICTIONARY[key]
        

        self.moveInfo = moveInfo
        self.id = moveInfo[0]
        self.name = moveInfo[1]

        self.description = moveInfo[2]
        self.type = moveInfo[3]
        self.kind = moveInfo[4]

        self.power = int(moveInfo[5])
        self.accuracy = moveInfo[6]
        self.pp = int(moveInfo[7])

        # Methods

        def __str__(self):
            msg = self.name + " " + str(self.power)
            return msg
        
        def getID(self):
            return self.id
        
        def getName(self):
            return self.name
        
        def getDescription(self):
            return self.description
        
        def getKind(self):
            return self.kind
        
        def getPower(self):
            return self.power
        
        def getAccuracy(self):
            return self.accuracy
        
        def getPP(self):
            return self.pp
        
        