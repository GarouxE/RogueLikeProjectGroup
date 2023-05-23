from Element import Element
import theGame

class Creature(Element):
    """A creature that occupies the dungeon.
        Is an Element. Has hit points and strength."""

    def __init__(self, name, hp, abbrv="", strength=1, invisible = False, fast=False):
        Element.__init__(self, name, abbrv)
        self.hp = hp
        self.armure = 0
        self.max_hp = hp
        self.strength = strength
        self.xp = (self.strength*self.max_hp)//2
        self.is_invisble = invisible
        self.is_fast = fast
        if self.is_invisible:
            self.xp = int(self.xp*1.5)
        if self.is_fast:
            self.xp = self.xp*2

    def description(self):
        """Description of the creature"""
        return Element.description(self) + " (%s/%s) " % (self.hp, self.max_hp)

    def meet(self, other):
        """The creature is encountered by an other creature.
            The other one hits the creature. Return True if the creature is dead."""
        if other.is_invisble:
            other.abbrv = "I"
        if self.is_invisble:
            self.abbrv = "I"
        if self.armure >0:
            self.armure-= other.strength
            if self.armure<0:
                self.armure = 0
        else:
            self.hp -= other.strength


        theGame.theGame().addMessage("The " + other.name + " hits the " + self.description())
        if self.hp > 0:
            return False
        if isinstance(other, Hero):
            other.earn_xp(self.xp)
        return True


