from Element import Element
import theGame
from utils import getch
from Equipment import Equipment

from handler import heal, teleport, armure


class Shop(Element):
    """ Shop exchanging gold for equipments """

    items = {Equipment("healing potion", "♥", usage=lambda self, hero: heal(hero)): 2,
             Equipment("teleport potion", "!", usage=lambda self, hero: teleport(hero, True)): 1,
             Equipment("armure", "Sh", usage=lambda self, hero: armure(hero)): 2,
             Equipment("portoloin", "w", usage=lambda self, hero: teleport(hero, False)): 3
             }

    def __init__(self):
        super().__init__("Shop", 'S')

    def value(self, item):
        """returns the value of an equipment"""
        for key in Shop.items:
            if key.name == item.name:
                return Shop.items[key]
        return 0

    def verification(self, item):
        """verifies if the item is sellable"""
        for key in Shop.items:
            if key.name == item.name:
                return True
        return False

    def meet(self, hero):
        hero.shopping = True
'''
    def meet(self, hero):
        """option to buy or sell items"""
        theGame.theGame().addMessage("You have " + str(hero.gold) + " gold")
        theGame.theGame().addMessage("Would you like to buy or sell ? [b, s]")
        print(theGame.theGame().readMessages())
        c = getch()
        if c == 'b' and hero.gold > 0:
            theGame.theGame().addMessage(
                "Items> ['0: healing potion (2)', '1: teleport potion (1)', '2: bow (2)' , '3: portoloin (3)']")
            print(theGame.theGame().readMessages())
            d = getch()
            while d != '0' and d != '1' and d != '2' and d != '3':
                print(theGame.theGame().readMessages())
                d = getch()
            if d == '0' and hero.trade(list(Shop.items.values())[0]):
                hero.take(list(Shop.items.keys())[0])
                theGame.theGame().addMessage("You bought a " + list(Shop.items.keys())[0].name)
            elif d == '1' and hero.trade(list(Shop.items.values())[1]):
                hero.take(list(Shop.items.keys())[1])
                theGame.theGame().addMessage("You bought a " + list(Shop.items.keys())[1].name)
            elif d == '2' and hero.trade(list(Shop.items.values())[2]):
                hero.take(list(Shop.items.keys())[2])
                theGame.theGame().addMessage("You bought a " + list(Shop.items.keys())[2].name)
            elif d == '3' and hero.trade(list(Shop.items.values())[3]):
                hero.take(list(Shop.items.keys())[3])
                theGame.theGame().addMessage("You bought a " + list(Shop.items.keys())[3].name)
            else:
                theGame.theGame().addMessage("You don't have enough gold")
        elif c == 's' and hero.length_inventory() > 0:
            sold = theGame.theGame().select(hero._inventory)
            if self.verification(sold):
                hero.incrementGold(self.value(sold))
                theGame.theGame().addMessage("You sold a " + sold.name)
                hero.remove(sold)
            else:
                theGame.theGame().addMessage("You cannot sell this item")
        elif hero.gold <= 0:
            theGame.theGame().addMessage("You don't have enough gold")
        elif hero.length_inventory() <= 0:
            theGame.theGame().addMessage("You don't have any items in your inventory")
        theGame.theGame().addMessage("You now have " + str(hero.gold) + " gold")
        return False
'''

