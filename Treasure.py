from Element import Element
import theGame


class Treasure(Element):
    """ Treasure chest containing an equipment of a higher level than the map """

    def __init__(self):
        super().__init__("Treasure", 'T')

    def meet(self, hero):
        """opens chest if a key is in the Hero's inventory"""
        if hero.check_elem("key"):
            theGame.theGame().addMessage("The " + hero.name + " opened the treasure chest")
            hero.randTake()#need to be an equiment level higher than the game (game level * 2)
            hero.remove(hero.check_elem("key"))
            return True
        else : 
            theGame.theGame().addMessage("A key is required")
            return False
