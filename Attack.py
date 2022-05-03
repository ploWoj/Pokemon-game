from random import random
from Move import Move
from Pokemon import Pokemon
import random

def statmod(statStage):
    if statStage == 1:
        multiplie = 1.5
    elif statStage == -1:
        multiplie = 2/3
    elif statStage == 2:
        multiplie = 2
    elif statStage == -2:
        multiplie = 1/2
    elif statStage == 3:
        multiplie = 2.5
    elif statStage == -3:
        multiplier = 0.4
    elif statStage == 4:
        multiplier = 3
    elif statStage == -4:
        multiplier = 1/3
    elif statStage == 5:
        multiplier = 3.5
    elif statStage == -5:
        multiplier = 2/7
    elif statStage == 6:
        multiplier = 4
    elif statStage == -6:
        multiplier = 1/4

    return multiplier


def attack(move, pokemon1, pokemon2):
    tempMsg = ""

    file = open("advantages.csv", 'r')
    typeDic = {}
    for line in file:
        line = line.strip()
        typeList = line.split(",")
        typeDic[typeList[0]] = typeList
    file.close()

    move = Move(move)

    modifier = 1

    for key in typeDic:
        if typeDic[key][1] == move.type and typeDic[key][2] == pokemon1.type1:
            modifier *= float(typeDic[key][3])

        if typeDic[key][1] == move.type and typeDic[key][2] == pokemon2.type2:
            modifier *= float(typeDic[key][3]) 
    
    # Calculating STAB (Same-type Attack Bonus)
    if move.type == pokemon1.type1:
        modifier *= Pokemon.STAB

    elif move.type == pokemon1.type2:
        modifier *= Pokemon.STAB

    modifier *= random.uniform(0.85, 1.0)

    print()

    tempMsg += random.useMove(move)

    # ATK/DEF or SpATK/SpDEF or Status? Using the Pokemon damage formula
    # If the move is "Physical", the damage formula will take into account attack and defense
    if move.kind == "Physical":
        damage = int((((2*pokemon1.getLevel()) + 10)/250 * (pokemon1.battleATK/pokemon2.battleDEF) * move.getPower() + 2) * modifier)
        tempMsg += "\n" + pokemon2.loseHP(damage)
    # If the move is "Special", the damage formula will take into account special attack and special defense
    elif move.kind == "Special":
        damage = int((((2*pokemon1.getLevel()) + 10)/250 * (pokemon1.battleSpATK/pokemon2.battleSpDEF) * move.getPower() + 2) * modifier)
        tempMsg += "\n" + pokemon2.loseHP(damage)

    # Stat Changing moves
    else:
        # If the move is stat-changing, it does 0 damage and the modifier is set to 1 (so it doesn't return super effective or not very effective)
        damage = 0
        modifier = 1

        # Going through each kind of different stat change based on the move type
        if move.kind == "a-":
            pokemon2.atkStage -= 1
            pokemon2.battleATK = pokemon2.originalATK * statMod(pokemon2.atkStage)
            tempMsg += "\n" + pokemon2.name + "'s attack fell! "

        elif move.kind == "a+":
            pokemon1.atkStage +=1
            pokemon1.battleATK = pokemon1.originalATK * statMod(pokemon1.atkStage)
            tempMsg += "\n" + pokemon1.name + "'s attack rose! "

        elif move.kind == "d+":
            pokemon1.defStage +=1
            pokemon1.battleDEF = pokemon1.originalDEF * statMod(pokemon1.defStage)
            print(pokemon1.name + "'s defense rose! ")
            tempMsg += "\n" + pokemon1.name + "'s defense rose! "

        elif move.kind == "sa+":
            pokemon1.spAtkStage +=1
            pokemon1.battleSpATK = pokemon1.originalSpATK * statMod(pokemon1.spAtkStage)
            print(pokemon1.name + "'s special attack rose! ")
            tempMsg += "\n" + pokemon1.name + "'s special attack rose! "

        elif move.kind == "sd+":
            pokemon1.spDefStage +=1
            pokemon1.battleSpDef = pokemon1.originalSpDEF * statMod(pokemon1.spDefStage)
            tempMsg += "\n" + pokemon1.name + "'s special defense rose! "

        elif move.kind == "s+":
            pokemon1.speedStage +=1
            pokemon1.battleSpeed = pokemon1.originalSpeed * statMod(pokemon1.speedStage)
            tempMsg += "\n" + pokemon1.name + "'s speed fell! "

        elif move.kind == "d-":
            pokemon2.defStage -=1
            pokemon2.battleDEF = pokemon2.originalDEF * statMod(pokemon2.defStage)
            tempMsg += "\n" + pokemon2.name + "'s defense fell! "

        elif move.kind == "sa-":
            pokemon2.spAtkStage -=1
            pokemon2.battleSpATK = pokemon2.originalSpATK * statMod(pokemon2.spAtkStage)
            tempMsg += "\n" + pokemon2.name + "'s special attack fell! "

        elif move.kind == "sd-":
            pokemon2.spDefStage -=1
            pokemon2.battleSpDEF = pokemon2.originalSpDEF * statMod(pokemon2.spDefStage)
            tempMsg += "\n" + pokemon2.name + "'s special defense fell! "

        elif move.kind == "s-":
            pokemon2.speedStage -=1
            pokemon2.battleSpeed = pokemon2.originalSpeed * statMod(pokemon2.speedStage)
            tempMsg += "\n" + pokemon2.name + "'s speed fell! "

    # Super effective, not very effective, or no effect?
    # Appending the result to tempMsg
    if modifier < 0.85 and modifier > 0:
        tempMsg += "\nIt's not very effective..."

    elif modifier > 1.5:
        tempMsg += "\nIt's super effective!"

    elif modifier == 0.0:
        tempMsg += "\nIt doesn't affect " + pokemon2.name + "..."

    # String containing useMove(), damage, and type effectiveness
    return tempMsg
