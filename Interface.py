import pygame as pg
import sys
import Sprites


import Element
import theGame
import Creature


class Ecran(object):

    def __init__(self):
        self.game = theGame.theGame()
        self.game.buildFloor()
        self.hero = self.game._hero
        self.coord_hero = self.game._floor._rooms[0].center()
        print(self.game._floor)
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode((1500, 800))
        self.global_event = pg.USEREVENT + 0
        self.clock = pg.time.Clock()

    def mettre_a_jour(self):
        pg.display.flip()
        self.clock.tick(60)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')

    def donne_carte(self):
        t = {}
        print(self.game._floor._mat)
        for j in range(len(self.game._floor._mat)):
            for i in range(len(self.game._floor._mat[j])):
                if self.game._floor._mat[i][j] != self.game._floor.empty:
                    t[(j,i)] = "green"

                    if str(self.game._floor._mat[i][j]) == "W" :
                        self.screen.blit( pg.transform.scale(pg.image.load("Sprites/Bat.png"),(30,30)).convert_alpha(), (j * 30 + 300, i * 30 + 100))
                    if str(self.game._floor._mat[i][j]) == "B" :
                        self.screen.blit( pg.transform.scale(pg.image.load("Sprites/Blob.png"),(30,30)).convert_alpha(), (j * 30 + 300, i * 30 + 100))
                    if str(self.game._floor._mat[i][j]) == "G" :
                        self.screen.blit( pg.transform.scale(pg.image.load("Sprites/Goblin.png"),(30,30)).convert_alpha(), (j * 30 + 300, i * 30 + 100))
                    if str(self.game._floor._mat[i][j]) == "O" :
                        self.screen.blit( pg.transform.scale(pg.image.load("Sprites/Ork.png"),(30,30)).convert_alpha(), (j * 30 + 300, i * 30 + 100))
                    if str(self.game._floor._mat[i][j]) == "@" :
                        self.screen.blit( pg.transform.scale(pg.image.load("Sprites/Dragon.png"),(30,30)).convert_alpha(), (j * 30 + 300, i * 30 + 100))




                    #if isinstance(self.game._floor._mat[i][j], Element.Element):
                        #pg.draw.circle(self.screen, 'blue',(j * 30 + 315, i * 30 + 115), 10)
        pg.display.flip()
        return t



    def dessine_carte(self):
        self.screen.fill("black")
        t = self.donne_carte()
        [pg.draw.rect(self.screen, t[pos], (pos[0] * 30+300, pos[1] * 30+100, 30, 30), 2)
         for pos in t]
        self.hero = pg.draw.circle(self.screen, 'grey', (self.coord_hero.x * 30 +315, self.coord_hero.y * 30 +115), 10)
        pg.draw.circle(self.screen, 'green', (self.game._floor._rooms[-1].center().x * 30 + 315, self.game._floor._rooms[-1].center().y  * 30 + 115), 10)

    def verifier_sortie(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        self.dessine_carte()
        while True:
            self.mettre_a_jour()
            self.verifier_sortie()


jeu = Ecran()
jeu.run()
