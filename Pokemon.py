from Move import Move

class Pokemon:
    POKEMON_DICTIONARY = {}
    # BASE POKEMON STATS
    IV = 30
    EV = 85
    STAB = 1.5
    LEVEL = 50
    def __init__(self, pokemon):
        pokemonInfo = []
        if len(Pokemon.POKEMON_DICTIONARY) == 0:
            file = open("Pokemons.csv", 'r')
            for line in file:
                line = line.strip()
                pokeList = line.split(',')
                Pokemon.POKEMON_DICTIONARY[pokeList[1]] = pokeList
            file.close()

        for key in Pokemon.POKEMON_DICTIONARY:
            if key.lower() == pokemon.lowet():
                pokemonInfo = Pokemon.POKEMON_DICTIONARY[key]

            # attributes

            self.__id = pokemonInfo[0]
            self.name = pokemonInfo[1]
            self.level = Pokemon.LEVEL

            # Type
            self.type1 = pokemonInfo[2]
            self.type2 = pokemonInfo[3]

            # Base stats

            self.__hp = int(pokemonInfo[4])
            self.__att = int(pokemonInfo[5])
            self.__def = int(pokemonInfo[6])
            self.__spAtk = int(pokemonInfo[7])
            self.__spDef = int(pokemonInfo[8])
            self.__speed = int(pokemonInfo[9])

            #  Values stats in battle. Theye are diffrent than basic stats
            self.battleHP = int(self.__hp + (0.5*Pokemon.IV) + (0.125 * Pokemon.EV) + 60)
            self.battleATT = int(self.__att + (0.5*Pokemon.IV) + (0.125 * Pokemon.EV) + 5)
            self.battleDEF = int(self.__def + (0.5*Pokemon.IV) + (0.125 * Pokemon.EV) + 5)
            self.battleSpATT = int(self.__spAtk + (0.5*Pokemon.IV) + (0.125 * Pokemon.EV) + 5)
            self.battleSpDef = int(self.__spDef + (0.5*Pokemon.IV) + (0.125 * Pokemon.EV) + 5)
            self.battleSpeed = int(self.__speed + (0.5*Pokemon.IV) + (0.125 * Pokemon.EV) + 5)


             # These variables are used to just hold the values of the original stat for stat modification purposes
            self.originalATK = self.__atk + (0.5*Pokemon.IV) + (0.125*Pokemon.EV) + 5
            self.originalDEF = self.__defense + (0.5*Pokemon.IV) + (0.125*Pokemon.EV) + 5
            self.originalSpATK = self.__spAtk + (0.5*Pokemon.IV) + (0.125*Pokemon.EV) + 5
            self.originalSpDEF = self.__spDef + (0.5*Pokemon.IV) + (0.125*Pokemon.EV) + 5
            self.originalSpeed = self.__speed + (0.5*Pokemon.IV) + (0.125*Pokemon.EV) + 5
            # Moves
            # Polemos.csv has pre-dtermined movesets

            self.move1 = Move(pokemonInfo[10])
            self.move2 = Move(pokemonInfo[11])
            self.move3 = Move(pokemonInfo[12])
            self.move4 = Move(pokemonInfo[13])

            # A list containing alle the moves:
            self.moveList = [self.move1.name.lower(), self.move2.name.lower(), self.move3.name.lower(), self.move4.name.lower()]

            # InBattle
            # Raised or lowered based on different moves used in battle.
            self.atkStage = 0
            self.defStage = 0
            self.spAtkStage = 0
            self.spDefStage = 0
            self.speedStage = 0

        # Methods
        # Printing all the Pokemon info the str method
        def __str__(self):
            msg = "Name: " + str(self.__name) + "\nID: " + str(self.__id) + "\nType1: " + str(self.__type1) + \
                "\nType2: " + str(self.__type2) + "\nBase HP: " + str(self.__hp) + "\nBase ATK: " + str(self.__atk) + "\nBase DEF: " + \
                str(self.__defense) + "\nBase Sp. ATK: " + str(self.__spAtk) + "\nBase Sp. DEF: " + str(self.__spDef) + "\nBase Speed: " + str(self.__speed)
            return msg
        
        # getters
        def getName(self):
            return self.name
        
        def getLevel(self):
            return self.level

        def getHP(self):
            return self.__hp
        
        def getATK(self):
            return self.__atk

        def getDEF(self):
            return self.__def

        def getSpATK(self):
            return self.__spATK
        
        def getSpDEF(self):
            return self.__spDef

        def getSpeed(self):
            return self.__speed
        
    #  setters
    def setAtkStage(self, atkStage):
        self.atkStage = atkStage
    
    def setDefStage(self, defStage):
        self.defStage = defStage

    def setSpAtkStage(self, spAtkStage):
        self.spAtkStage = spAtkStage
    
    def setSpDefStage(self, spDefStage):
        self.spDefStage = spDefStage

    def setSpeedStage(self, speedStage):
        self.speedStage = speedStage
    
    # MOVE METHODS
    # getters
    def getMove(self):
        return self.move1
    
    def getMove2(self):
        return self.move2
    
    def getMove3(self):
        return self.move3
    
    def getMove4(self):
        return self.move4
    # setters

    def setMove1(self, move1):
        self.mov1 = move1

    def setMove2(self, move2):
        self.move2 = move2

    def setMove3(self, move3):
        self.move3 = move3

    def setMove4(self, move4):
        self.move4 = move4

    # Printing methods

    def loseHP(self, lostHP):
        self.battleHP -= lostHP
        if self.battleHP < 0:
            self.battleHP = 0
        msg = self.name + " lost "  + str(lostHP) + 'HP!'
        return msg

    def gainHP(self, gainedHP):
        self.__hp = gainedHP

    def isAlive(self):
        if self.battleHP > 0:
            return True
        else:
            return False

    def faint(self):
        if self.battleHP <= 0:
            msg = self.name + "fainted"
            return msg
