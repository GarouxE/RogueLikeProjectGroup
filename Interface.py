import random,copy

import pygame as pg
import sys
import time

import theGame

Inventaire = {"♥":"Sprites/Health_potion.png",
              "!":"Sprites/Teleport_potion.png",
              "b":"Sprites/Bow.png",
              "w":"Sprites/Portal.png",
              "Sh":"Sprites/Shield.png",
              "*":"Sprites/Key.png",
}

def drawText(screen, text, x, y, w, h, size=14, color=(255, 0, 255), fontName="comicsansms"):
    """Ecrit un texte centre en w et h"""
    font = pg.font.SysFont(fontName, size)
    txt = font.render(text, True, color)
    screen.blit(txt, (x + (w - txt.get_width()) / 2, y + (h - txt.get_height()) / 2))

class Ecran(object):

    def __init__(self):
      """Ouvre une fenetre pygame et initialise les evenements de base"""
        self.n = 0
        self.game = theGame.theGame()
        self.game.buildFloor()
        self.hero = self.game._hero
        self.coord_hero = self.game._floor._rooms[0].center()
        print(self.game._floor)
        pg.init()

        self.shop_items =[None for i in range(4)]
        self.level = -1

        self.screen = pg.display.set_mode((1400, 700))
        self.global_event = pg.USEREVENT + 0
        self.clock = pg.time.Clock()

    def mettre_a_jour(self):
      """Remet a jour l'eacran"""
        pg.display.flip()
        self.clock.tick(10)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')

    def donne_carte(self):
      """Dessine la carte avec les monstres"""
        pg.draw.rect(self.screen, "grey", (200, 50, 600, 600), 0)
        t = {}
        for j in range(len(self.game._floor._mat)):
            for i in range(len(self.game._floor._mat[j])):
                if self.game._floor._mat[i][j] != self.game._floor.empty:
                    pg.draw.rect(self.screen, "green", (j * 30 + 200, i * 30 + 50, 30, 30), 1)

                    #self.screen.blit(
                        #pg.transform.scale(pg.image.load("Sprites/Tile2.jpg"), (30, 30)).convert_alpha(),
                        #(j * 30 + 200, i * 30 + 50))
                    if str(self.game._floor._mat[i][j]) == "W":
                        self.screen.blit(
                            pg.transform.scale(pg.image.load("Sprites/Bat.png"), (30, 30)).convert_alpha(),
                            (j * 30 + 200, i * 30 + 50))
                    if str(self.game._floor._mat[i][j]) == "I":
                        self.screen.blit(
                            pg.transform.scale(pg.image.load("Sprites/Invisible.png"), (30, 30)).convert_alpha(),
                            (j * 30 + 200, i * 30 + 50))
                    if str(self.game._floor._mat[i][j]) == "B":
                        self.screen.blit(
                            pg.transform.scale(pg.image.load("Sprites/Blob.png"), (30, 30)).convert_alpha(),
                            (j * 30 + 200, i * 30 + 50))
                    if str(self.game._floor._mat[i][j]) == "G":
                        self.screen.blit(
                            pg.transform.scale(pg.image.load("Sprites/Goblin.png"), (30, 30)).convert_alpha(),
                            (j * 30 + 200, i * 30 + 50))
                    if str(self.game._floor._mat[i][j]) == "R":
                        self.screen.blit(
                            pg.transform.scale(pg.image.load("Sprites/Reaper.png"), (30, 30)).convert_alpha(),
                            (j * 30 + 200, i * 30 + 50))
                    if str(self.game._floor._mat[i][j]) == "O":
                        self.screen.blit(
                            pg.transform.scale(pg.image.load("Sprites/Ork.png"), (30, 30)).convert_alpha(),
                            (j * 30 + 200, i * 30 + 50))
                    if str(self.game._floor._mat[i][j]) == "@":
                        self.screen.blit(
                            pg.transform.scale(pg.image.load("Sprites/Hero.png"), (30, 30)).convert_alpha(),
                            (j * 30 + 200, i * 30 + 50))
                    if str(self.game._floor._mat[i][j]) == "♥":
                        self.screen.blit(
                            pg.transform.scale(pg.image.load("Sprites/Health_potion.png"), (30, 30)).convert_alpha(),
                            (j * 30 + 200, i * 30 + 50))
                    if str(self.game._floor._mat[i][j]) == "o":
                        self.screen.blit(
                            pg.transform.scale(pg.image.load("Sprites/Gold.png"), (30, 30)).convert_alpha(),
                            (j * 30 + 200, i * 30 + 50))
                    if str(self.game._floor._mat[i][j]) == "!":
                        self.screen.blit(
                            pg.transform.scale(pg.image.load("Sprites/Teleport_potion.png"), (30, 30)).convert_alpha(),
                            (j * 30 + 200, i * 30 + 50))
                    if str(self.game._floor._mat[i][j]) == "b":
                        self.screen.blit(
                            pg.transform.scale(pg.image.load("Sprites/Bow.png"), (30, 30)).convert_alpha(),
                            (j * 30 + 200, i * 30 + 50))
                    if str(self.game._floor._mat[i][j]) == "w":
                        self.screen.blit(
                            pg.transform.scale(pg.image.load("Sprites/Portal.png"), (30, 30)).convert_alpha(),
                            (j * 30 + 200, i * 30 + 50))
                    if str(self.game._floor._mat[i][j]) == "Sh":
                        self.screen.blit(
                            pg.transform.scale(pg.image.load("Sprites/Shield.png"), (30, 30)).convert_alpha(),
                            (j * 30 + 200, i * 30 + 50))
                    if str(self.game._floor._mat[i][j]) == "D":
                        self.screen.blit(
                            pg.transform.scale(pg.image.load("Sprites/Dragon.png"), (30, 30)).convert_alpha(),
                            (j * 30 + 200, i * 30 + 50))
                    if str(self.game._floor._mat[i][j]) == "S":
                        self.screen.blit(
                            pg.transform.scale(pg.image.load("Sprites/Shop.png"), (30, 30)).convert_alpha(),
                            (j * 30 + 200, i * 30 + 50))
                    if str(self.game._floor._mat[i][j]) == "T":
                        self.screen.blit(
                            pg.transform.scale(pg.image.load("Sprites/chest.png"), (30, 30)).convert_alpha(),
                            (j * 30 + 200, i * 30 + 50))
                else:
                    pg.draw.rect(self.screen, "purple", (j * 30 + 200, i * 30 + 50, 30, 30), 0)

        pg.display.flip()
        self.n += 1


    def dessine_sante(self):
      """Dessine la vie l'armure le personnage et son xp"""
        pg.draw.rect(self.screen, "green", (1250, 90, 80,90), 0)
        self.screen.blit(
            pg.transform.scale(pg.image.load("Sprites/Hero.png"), (70, 70)).convert_alpha(),
            (1250, 100))
        sante, max_sante, x, y = self.hero.hp, self.hero.max_hp, 0, 0
        armure = self.hero.armure

        while max_sante > 0:
            if x % 10 == 0:
                x = 0
                y += 1
            if sante > 0:
                self.screen.blit(
                    pg.transform.scale(pg.image.load("Sprites/Heart.png"), (40, 40)).convert_alpha(),
                    (800 + x * 40, 100 + y * 40))
                sante -= 1
            else:
                self.screen.blit(
                    pg.transform.scale(pg.image.load("Sprites/Empty_Heart.png"), (40, 40)).convert_alpha(),
                    (800 + x * 40, 100 + y * 40))
            x += 1
            max_sante -= 1

        while armure > 0:
            self.screen.blit(
                pg.transform.scale(pg.image.load("Sprites/Shield.png"), (30, 30)).convert_alpha(),
                (800 + armure * 40, 300))
            armure -= 1
        pg.draw.circle(self.screen, 'green', (
            self.game._floor._rooms[-1].center().x * 30 + 215, self.game._floor._rooms[-1].center().y * 30 + 65), 10)

    def dessine_inventaire(self):
      """Dessine les lelements presents dans l'inventaire du hero """
        pg.draw.rect(self.screen, "green", (800, 590, 700, 90), 0)
        self.screen.blit(
            pg.transform.scale(pg.image.load("Sprites/Fleches.png"), (100, 70)).convert_alpha(),
            (800 , 600))
        self.screen.blit(
            pg.transform.scale(pg.image.load("Sprites/Touches.png"), (200, 200)).convert_alpha(),
            (950 , 560))
        for i in range(len(self.hero._inventory)):
            self.screen.blit(
                pg.transform.scale(pg.image.load(Inventaire[str(self.hero._inventory[i])]), (50, 50)).convert_alpha(),
                (800+50*i, 400))
            pg.draw.rect(self.screen, "white", (800+50*i, 400, 50, 50), 1)
        drawText(self.screen, str(self.hero.gold), 1250,200, 0, 0, size=24,color="yellow")
        self.screen.blit(
            pg.transform.scale(pg.image.load("Sprites/Gold.png"), (50, 50)).convert_alpha(),
            (1275,175))
        drawText(self.screen,"XP:"+ str(self.hero.xp)+"/"+str(self.hero.xp_cap), 1300, 75, 0, 0, size=24, color="green")

    def draw_shop_items(self):
      """Dessine les elements dans la boutique """
        if theGame.theGame()._level != self.level:
            self.level = theGame.theGame()._level
            for i in range(4):
                self.shop_items[i] = random.choice(copy.copy(theGame.theGame().shop_items))

    def selling_shop(self):
      """Dessine et interagi le magasin pour vendre les objets"""
        self.screen.fill("black")
        self.screen.blit(pg.transform.scale(pg.image.load("Sprites/Shop_interior.png"), (1500, 700)).convert_alpha(),
                         (0, 0))
        pg.draw.rect(self.screen, "black", (0, 0, 1500, 70), 0)

        drawText(self.screen, "Press E to exit the shop", 200, 20, 0, 0, size=24)
        drawText(self.screen, str(self.hero.gold), 1250, 30, 0, 0, size=24, color="yellow")
        self.screen.blit(
            pg.transform.scale(pg.image.load("Sprites/Gold.png"), (50, 50)).convert_alpha(),
            (1275, 20))
        for i in range(len(self.hero._inventory)):
            self.screen.blit(
                pg.transform.scale(pg.image.load(Inventaire[str(self.hero._inventory[i])]), (50, 50)).convert_alpha(),
                (425 + 50 * i, 400))
            drawText(self.screen, str(theGame.theGame().shop_prices[str(self.hero._inventory[i])]),
                     450 + 50 * i, 450, 0, 0, color="yellow", size=24)
            drawText(self.screen, str(i),
                     450 + 50 * i, 475, 0, 0, color="blue", size=25)

        pg.display.flip()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN   and event.key == pg.K_e:
                    return
                if 0 in range(len(self.hero._inventory)):
                    if event.type == pg.KEYDOWN and event.key == pg.K_0:
                        self.hero.gold += int(theGame.theGame().shop_prices[str(self.hero._inventory[0])])
                        self.hero._inventory.remove(self.hero._inventory[0])
                        return
                if 1 in range(len(self.hero._inventory)):
                    if event.type == pg.KEYDOWN and event.key == pg.K_1:
                        self.hero.gold += int(theGame.theGame().shop_prices[str(self.hero._inventory[1])])
                        self.hero._inventory.remove(self.hero._inventory[1])
                        return
                if 2 in range(len(self.hero._inventory)):
                    if event.type == pg.KEYDOWN and event.key == pg.K_2:
                        self.hero.gold += int(theGame.theGame().shop_prices[str(self.hero._inventory[2])])
                        self.hero._inventory.remove(self.hero._inventory[2])
                        return
                if 3 in range(len(self.hero._inventory)):
                    if event.type == pg.KEYDOWN and event.key == pg.K_3:
                        self.hero.gold += int(theGame.theGame().shop_prices[str(self.hero._inventory[3])])
                        self.hero._inventory.remove(self.hero._inventory[3])
                        return
                if 4 in range(len(self.hero._inventory)):
                    if event.type == pg.KEYDOWN and event.key == pg.K_4:
                        self.hero.gold += int(theGame.theGame().shop_prices[str(self.hero._inventory[4])])
                        self.hero._inventory.remove(self.hero._inventory[4])
                        return
                if 5 in range(len(self.hero._inventory)):
                    if event.type == pg.KEYDOWN and event.key == pg.K_5:
                        self.hero.gold += int(theGame.theGame().shop_prices[str(self.hero._inventory[5])])
                        self.hero._inventory.remove(self.hero._inventory[5])
                        return
                if 6 in range(len(self.hero._inventory)):
                    if event.type == pg.KEYDOWN and event.key == pg.K_6:
                        self.hero.gold += int(theGame.theGame().shop_prices[str(self.hero._inventory[6])])
                        self.hero._inventory.remove(self.hero._inventory[6])
                        return
                if 7 in range(len(self.hero._inventory)):
                    if event.type == pg.KEYDOWN and event.key == pg.K_7:
                        self.hero.gold += int(theGame.theGame().shop_prices[str(self.hero._inventory[7])])
                        self.hero._inventory.remove(self.hero._inventory[7])
                        return
                if 8 in range(len(self.hero._inventory)):
                    if event.type == pg.KEYDOWN and event.key == pg.K_8:
                        self.hero.gold += int(theGame.theGame().shop_prices[str(self.hero._inventory[8])])
                        self.hero._inventory.remove(self.hero._inventory[8])
                        return
                if 9 in range(len(self.hero._inventory)):
                    if event.type == pg.KEYDOWN and event.key == pg.K_9:
                        self.hero.gold += int(theGame.theGame().shop_prices[str(self.hero._inventory[9])])
                        self.hero._inventory.remove(self.hero._inventory[9])
                        return
    def shop(self):
      """dessine et interagi pour le magasin pour acheter des objets"""
        self.screen.fill("black")
        self.screen.blit(pg.transform.scale(pg.image.load("Sprites/Shop_interior.png"), (1500, 700)).convert_alpha(),
                         (0, 0))
        pg.draw.rect(self.screen, "black", (0,0, 1500, 70), 0)

        drawText(self.screen, "Press E to exit the shop and S to sell an object", 400, 20, 0, 0, size=24)
        drawText(self.screen, str(self.hero.gold), 1250, 30, 0, 0, size=24, color="yellow")
        self.screen.blit(
            pg.transform.scale(pg.image.load("Sprites/Gold.png"), (50, 50)).convert_alpha(),
            (1275, 20))
        for i in range(len(self.shop_items)):
            if self.shop_items[i]:
                self.screen.blit(
                    pg.transform.scale(pg.image.load(Inventaire[str(self.shop_items[i])]), (100, 100)).convert_alpha(),
                    (400 + 100 * i, 350))
                if int(theGame.theGame().shop_prices[str(self.shop_items[i])]) <= int(self.hero.gold):
                    drawText(self.screen, str(theGame.theGame().shop_prices[str(self.shop_items[i])]),
                             450+100*i, 450, 0, 0, color="green",size=24)
                else:
                    drawText(self.screen, str(theGame.theGame().shop_prices[str(self.shop_items[i])]), 450 + 100 * i,
                             450, 0, 0, color="red", size=24)
                drawText(self.screen, str(i),
                         450 + 100 * i, 475, 0, 0, color="blue", size=25)

        pg.display.flip()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN   and event.key == pg.K_e:
                    self.hero.shopping = False
                    return
                if event.type == pg.KEYDOWN   and event.key == pg.K_s:
                    self.selling_shop()
                    self.hero.shopping = False
                    return
                if event.type == pg.KEYDOWN   and event.key == pg.K_0:
                    if self.shop_items[0] and len(self.hero._inventory)<10:
                        if int(theGame.theGame().shop_prices[str(self.shop_items[0])]) <= int(self.hero.gold) :
                            self.hero.gold -= int(theGame.theGame().shop_prices[str(self.shop_items[0])])
                            self.hero._inventory.append(self.shop_items[0])
                            self.shop_items[0] = None
                    self.hero.shopping = False
                    return
                if event.type == pg.KEYDOWN   and event.key == pg.K_1:
                    if self.shop_items[1] and len(self.hero._inventory)<10:
                        if int(theGame.theGame().shop_prices[str(self.shop_items[1])]) <= int(self.hero.gold) :
                            self.hero.gold -= int(theGame.theGame().shop_prices[str(self.shop_items[1])])
                            self.hero._inventory.append(self.shop_items[1])
                            self.shop_items[1] = None
                    self.hero.shopping = False
                    return
                if event.type == pg.KEYDOWN   and event.key == pg.K_2:
                    if self.shop_items[2] and len(self.hero._inventory)<10:
                        if int(theGame.theGame().shop_prices[str(self.shop_items[2])]) <= int(self.hero.gold) :
                            self.hero.gold -= int(theGame.theGame().shop_prices[str(self.shop_items[2])])
                            self.hero._inventory.append(self.shop_items[2])
                            self.shop_items[2] = None
                    self.hero.shopping = False
                    return
                if event.type == pg.KEYDOWN   and event.key == pg.K_3:
                    if self.shop_items[3] and len(self.hero._inventory)<10:
                        if int(theGame.theGame().shop_prices[str(self.shop_items[3])]) <= int(self.hero.gold) :
                            self.hero.gold -= int(theGame.theGame().shop_prices[str(self.shop_items[3])])
                            self.hero._inventory.append(self.shop_items[3])
                            self.shop_items[3] = None
                    self.hero.shopping = False
                    return




    def dessine_carte(self):
      """ Lance les fonctions de dessin"""
        self.screen.fill("black")
        self.donne_carte()
        self.dessine_sante()
        self.dessine_inventaire()
        
    def select_slot(self):
      """permet de choisir des elements de l'intaire"""
        while True:
            drawText(self.screen, "Veuillez choisir item a utiliser ou appuyer sur TAB pour sortir", 1025, 370, 0, 0, size=14)
            drawText(self.screen,"A",825,470,0,0,size= 24)
            drawText(self.screen, "Z", 875, 470, 0, 0, size=24)
            drawText(self.screen, "E", 925, 470, 0, 0, size=24)
            drawText(self.screen, "R", 975, 470, 0, 0, size=24)
            drawText(self.screen, "T", 1025, 470, 0, 0, size=24)
            drawText(self.screen, "Y", 1075, 470, 0, 0, size=24)
            drawText(self.screen, "U", 1125, 470, 0, 0, size=24)
            drawText(self.screen, "I", 1175, 470, 0, 0, size=24)
            drawText(self.screen, "O", 1225, 470, 0, 0, size=24)
            drawText(self.screen, "P", 1275, 470, 0, 0, size=24)
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN  and event.key == pg.K_a:
                    if 0 < len(self.hero._inventory):
                        return "0"
                if event.type == pg.KEYDOWN   and event.key == pg.K_z:
                    if 1< len(self.hero._inventory):
                        return "1"
                if event.type == pg.KEYDOWN   and event.key == pg.K_e:
                    if 2 < len(self.hero._inventory):
                        return "2"
                if event.type == pg.KEYDOWN   and event.key == pg.K_r:
                    if 3 < len(self.hero._inventory):
                        return "3"
                if event.type == pg.KEYDOWN   and event.key == pg.K_t:
                    if 4 < len(self.hero._inventory):
                        return "4"
                if event.type == pg.KEYDOWN   and event.key == pg.K_y:
                    if 5 < len(self.hero._inventory):
                        return "5"
                if event.type == pg.KEYDOWN  and event.key == pg.K_u:
                    if 6 < len(self.hero._inventory):
                        return "6"
                if event.type == pg.KEYDOWN   and event.key == pg.K_i:
                    if 7 < len(self.hero._inventory):
                        return "7"
                if event.type == pg.KEYDOWN   and event.key == pg.K_o:
                    if 8 < len(self.hero._inventory):
                        return "8"
                if event.type == pg.KEYDOWN  and event.key == pg.K_p:
                    if 9 < len(self.hero._inventory):
                        return "9"
                if event.type == pg.KEYDOWN   and event.key == pg.K_TAB:
                    return None





    def verifier_evenements(self):
      """ Verifie le mouvement du joeuer"""


        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN and (event.key == pg.K_RIGHT or event.key == pg.K_d):
                    return 'd'
                if event.type == pg.KEYDOWN and (event.key == pg.K_LEFT or event.key == pg.K_q):
                    return 'q'
                if event.type == pg.KEYDOWN and (event.key == pg.K_UP or event.key == pg.K_z):
                    return 'z'
                if event.type == pg.KEYDOWN and (event.key == pg.K_DOWN or event.key == pg.K_s):
                    return 's'
                if event.type == pg.KEYDOWN and event.key == pg.K_a:
                    return 'a'
                if event.type == pg.KEYDOWN and event.key == pg.K_e:
                    return 'e'
                if event.type == pg.KEYDOWN and event.key == pg.K_w:
                    return 'w'
                if event.type == pg.KEYDOWN and event.key == pg.K_c:
                    return 'c'
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    return ' '
                if event.type == pg.KEYDOWN and event.key == pg.K_k:
                    return 'k'
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    return ' '
                if event.type == pg.KEYDOWN and event.key == pg.K_u:
                    a = self.select_slot()
                    return a

    def run(self):
      """Lance la boucle principale"""
        self.dessine_carte()
        while True:
            print(self.game._floor)
            self.mettre_a_jour()
            self.draw_shop_items()
            c = self.verifier_evenements()
            if c in self.game._actions:
                self.game._actions[c](self.game._hero)
            if self.hero.shopping:
                self.shop()
            self.game._floor.moveAllMonsters()
            self.dessine_carte()

            if self.hero.hp <= 0:
                self.screen.fill("black")
                self.screen.blit(pg.image.load("Sprites/gameOver.png"), (500, 200))
                pg.display.flip()
                time.sleep(2)
                pg.quit()
                sys.exit()

