import pygame as pg
import sys

import theGame

Inventaire = {"♥":"Sprites/Health_potion.png",
              "!":"Sprites/Teleport_potion.png",
              "b":"Sprites/Bow.png",
              "w":"Sprites/Portal.png",
              "S":"Sprites/Shield.png",
              "*":"Sprites/Key.png",
}


def drawText(screen, text, x, y, w, h, size=14, color=(255, 0, 255), fontName="comicsansms"):
    """Draws a text centered inside the w and h"""
    font = pg.font.SysFont(fontName, size)
    txt = font.render(text, True, color)
    screen.blit(txt, (x + (w - txt.get_width()) / 2, y + (h - txt.get_height()) / 2))

class Ecran(object):

    def __init__(self):
        self.n = 0
        self.game = theGame.theGame()
        self.game.buildFloor()
        self.hero = self.game._hero
        self.coord_hero = self.game._floor._rooms[0].center()
        print(self.game._floor)
        pg.init()

        self.screen = pg.display.set_mode((1400, 700))
        self.global_event = pg.USEREVENT + 0
        self.clock = pg.time.Clock()

    def mettre_a_jour(self):
        pg.display.flip()
        self.clock.tick(10)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')

    def donne_carte(self):
        pg.draw.rect(self.screen, "grey", (200, 50, 600, 600), 0)
        t = {}
        for j in range(len(self.game._floor._mat)):
            for i in range(len(self.game._floor._mat[j])):
                if self.game._floor._mat[i][j] != self.game._floor.empty:
                    pg.draw.rect(self.screen, "green", (j * 30 + 200, i * 30 + 50, 30, 30), 1)
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
        print(self.hero.hp)

    def dessine_sante(self):
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
        for i in range(len(self.hero._inventory)):
            self.screen.blit(
                pg.transform.scale(pg.image.load(Inventaire[str(self.hero._inventory[i])]), (50, 50)).convert_alpha(),
                (800+50*i, 400))
            pg.draw.rect(self.screen, "white", (800+50*i, 400, 50, 50), 1)



    def dessine_carte(self):
        self.screen.fill("black")
        self.donne_carte()
        self.dessine_sante()
        self.dessine_inventaire()
    def select_slot(self):
        while True:
            drawText(self.screen, "Veuillez choisir item a utiliser ou appuyer sur U pour sortir", 1025, 370, 0, 0, size=14)
            drawText(self.screen,"A    Z    E    R    T    Y    U    I    O    P",1025,470,0,0,size= 24)
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
                        return "4"
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
                if event.type == pg.KEYDOWN   and event.key == pg.K_u:
                    return None

    def verifier_evenements(self):


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
        self.dessine_carte()
        while True:
            self.mettre_a_jour()
            c = self.verifier_evenements()
            if c in self.game._actions:
                self.game._actions[c](self.game._hero)

            self.game._floor.moveAllMonsters()
            print(self.game._floor)
            self.dessine_carte()
            if self.hero.hp <= 0:
                pg.quit()
                sys.exit()


jeu = Ecran()
jeu.run()
