import theGame

def heal(creature):
    """Heal the creature"""
    if creature.hp <=creature.max_hp - 3:
        creature.hp += 3
    else:
        creature.hp = creature.max_hp
    return True


def teleport(creature, unique):
    """Teleport the creature"""
    t = []
    for j in range(len(theGame.theGame()._floor)):
        for i in range(len(theGame.theGame()._floor)):
            if str(theGame.theGame()._floor._mat[i][j]) == ".":
                t.append(Coord.Coord(i,j))
    theGame.theGame()._floor.rm(theGame.theGame()._floor.pos(creature))
    theGame.theGame()._floor.put(random.choice(t), creature)
    return unique

def armure(hero):
    if hero.armure <= 7:
        hero.armure +=3
    else:
        hero.armure = 10
    return True

def throw(power, loss):
    """Throw an object"""
    pass
