from Element import Element
import theGame


class Trap(Element):
    """A Trap that occupies the dungeon.
        Is an Element. Just does damage."""

    def __init__(self, name = "trap", abbrv = ".", strength=1):
        Element.__init__(self, name, abbrv)
        self.strength = strength

    def meet(self, other):
        """The creature is encountered by a Trap.
            can effect the hero as well as monsters."""
        other.hp -= self.strength
        theGame.theGame().addMessage("The " + other.name + " hits a " + self.name)
        return True
