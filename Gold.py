from Element import Element
import theGame

class Gold(Element):
    """Gold"""

    def __init__(self, name = "gold", abbrv = 'o'):
        Element.__init__(self, name, abbrv)

    def meet(self, hero):
        """Makes the hero meet the Gold. The hero takes the Gold."""
        hero.takeGold(self)
        theGame.theGame().addMessage("You picked up gold")
        return True
