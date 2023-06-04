from Creature import Creature
from Equipment import Equipment
from Gold import Gold
import theGame

class Hero(Creature):
    """The hero of the game.
        Is a creature. Has an inventory of elements. """

    def __init__(self, name="Hero", hp=10, abbrv="@", strength=2):
        Creature.__init__(self, name, hp, abbrv, strength)
        self._inventory = []
        self.level = 0
        self.xp_cap = 10
        self.xp = 0
        self.gold = 0
        self.poisonned = False
        self.goldInventory = {"gold" : self.gold}
        self.shopping = False
    
    def description(self):
        """Description of the hero"""
        return Creature.description(self) +"armure:"+ str(self.armure)+ " exp:%s/%s" % (self.xp, self.xp_cap)+ str(self._inventory) 

    def fullDescription(self):
        """Complete description of the hero"""
        res = ''
        for e in self.__dict__:
            if e[0] != '_':
                res += '> ' + e + ' : ' + str(self.__dict__[e]) + '\n'
        res += '> INVENTORY : ' + str([x.name for x in self._inventory])
        return res

    def checkEquipment(self, o):
        """Check if o is an Equipment."""
        if not isinstance(o, Equipment) and not isinstance(o, Gold):
            raise TypeError('Not a Equipment or Gold')
            
    def take(self, elem):
        """The hero takes adds the equipment to its inventory"""
        if len(self._inventory)<10:
            self.checkEquipment(elem)
            self._inventory.append(elem)
     
    def takeGold(self, elem):
        "the hero add gold to his inventory"
        self.checkEquipment(elem)
        self.gold += 1
        
    def incrementGold(self, increment):
        """increments the gold"""
        self.gold += increment
    
    def randTake(self):
        """the hero recieves a random equipment"""
        elem = theGame.theGame().randEquipment()
        if isinstance(elem, Equipment):
            self.take(elem)
            theGame.theGame().addMessage("The " + self.name + " recieved a " + elem.name)
        elif isinstance(elem, Gold):
            self.takeGold(elem)
            theGame.theGame().addMessage("The " + self.name + " recieved " + elem.name)
            
    def trade(self, value):
        """substract the value from the hero's amount of gold"""
        if self.gold >= value:
            self.gold -= value
            return True
        return False
    
    def remove(self, elem):
        """removes an element from the inventory"""
        self.checkEquipment(elem)
        self._inventory.remove(elem)
        
    def check_elem(self, item):
        """Verifies if the item is in the Hero inentory"""
        for elem in self._inventory:
            if elem.name == item:
                return elem
        return None
    
    def length_inventory(self):
        """returns the length of the inventory"""
        return len(self._inventory)
    
    def use(self, elem):
        """Use a piece of equipment"""
        if elem is None:
            return
        self.checkEquipment(elem)
        if elem not in self._inventory:
            raise ValueError('Equipment ' + elem.name + 'not in inventory')
        if elem.use(self):
            self._inventory.remove(elem)

    def earn_xp(self, xp_amount):
        self.xp += xp_amount
        while self.xp >= self.xp_cap:
            self.xp -= self.xp_cap
            self.level_up()
    
    def level_up(self):
        if self.level % 2 == 0:
            self.max_hp += 2
            self.strength += 1
        else:
            self.max_hp += 3
        self.level += 1
        self.hp = self.max_hp
        self.xp_cap += 10 + 5*self.level
