#!/usr/bin/env python3

import pygame
import sys
import random
from options import Option

HEAT_BAR_IMAGE = pygame.Surface((1000, 10))
SCORE = 0

class Game:
    def __init__(self):
        self.gameState = 1
        self.keys = [0,0,0,0,0]
        self._exit = False
        self.gameDisplay = pygame.display.set_mode((1200, 859))
        self.menuFont = pygame.font.Font("assets/wayner.ttf", 40)
        self.options = [Option("PLAY", (540, 510), self.menuFont, self.gameDisplay),
                        Option("OPTIONS", (505, 575), self.menuFont, self.gameDisplay),
                        Option("EXIT", (548, 635), self.menuFont, self.gameDisplay)]
        self.volume = 100
        pygame.mixer.music.load("assets/music/intro.ogg")
        pygame.mixer.music.play()

    def getExit(self):
        return self._exit

    def setExit(self, status):
        self._exit = status

    def setBackground(self, x, y):
        self.gameDisplay.blit(pygame.image.load("assets/images/background.jpg"), (x, y))

    def setGeometrics(self):
        geomtrics = [
            pygame.image.load("assets/images/cube.png"),
            pygame.image.load("assets/images/delta.png"),
            pygame.image.load("assets/images/losange.png"),
            pygame.image.load("assets/images/rond.png"),
            pygame.image.load("assets/images/star.png"),
            pygame.image.load("assets/images/background_game.jpg")
        ]
        return (geomtrics)

    def isHover(self, listOptions):
        for option in listOptions:
            option.is_hovered = True if option.rect.collidepoint(pygame.mouse.get_pos()) else False
            option.draw(self.gameDisplay, self.menuFont)

    def handlerMenu(self):
        self.setBackground(0, 0)
        pygame.event.pump()
        self.isHover(self.options)
        if (pygame.mouse.get_pressed()[0] and self.options[0].rect.collidepoint(pygame.mouse.get_pos())):
            pygame.mixer.music.load("assets/music/on-the-run.ogg")
            pygame.mixer.music.play()
            self.gameHandler()
            pygame.mixer.music.load("assets/music/intro.ogg")
            pygame.mixer.music.play()
        if (pygame.mouse.get_pressed()[0] and self.options[1].rect.collidepoint(pygame.mouse.get_pos())):
            self.gameDisplay.fill((0,0,0))
            self.optionHandler()
        if (pygame.mouse.get_pressed()[0] and self.options[2].rect.collidepoint(pygame.mouse.get_pos())):
            sys.exit(0)

    def optionHandler(self):
        self.menuFont = pygame.font.Font("assets/ka1.ttf", 40)
        optionMenuFont = pygame.font.init()
        option = Option("VOLUME : " + str(self.volume), (440, 525), self.menuFont, self.gameDisplay)
        while True:
            self.gameDisplay.fill((0,0,0))
            self.setBackground(0,0)
            if self.optionEventHandler() == 1:
                return 1
            pygame.event.pump()
            title_text = self.menuFont.render("VOLUME : " + str(self.volume), True, (0, 0, 0))
            self.gameDisplay.blit(title_text, (440, 525))
            pygame.display.update()

    def optionEventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 1
                if event.key == pygame.K_m and self.volume == 100:
                    self.volume = 0
                    pygame.mixer.music.set_volume(self.volume)
                else:
                    self.volume = 100
                    pygame.mixer.music.set_volume(self.volume)

    def getKeys(self):
        self.keys[0] = random.randint(0, 3)
        self.keys[1] = random.randint(0, 3)
        self.keys[2] = random.randint(0, 3)
        self.keys[3] = random.randint(0, 3)
        self.keys[4] = random.randint(0, 3)

    def bar(self):
        color = pygame.Color('#f22b2b')
        for x in range(HEAT_BAR_IMAGE.get_width()):
            for y in range(HEAT_BAR_IMAGE.get_height()):
                HEAT_BAR_IMAGE.set_at((x, y), color)
            if x > 200:
                color = pygame.Color('#f2b11a')
            if x > 400:
                color = pygame.Color('#e0e00f')
            if x > 600:
                color = pygame.Color('#2dc611')

    def gameHandler(self):
        ORANGE = 255, 100, 0
        GEO = self.setGeometrics()
        clock = pygame.time.Clock()
        heat_rect = HEAT_BAR_IMAGE.get_rect(topleft=(100, 450))
        heat = 100
        done = False

        self.getKeys()
        while not done:
            self.bar()
            heat -= 1 + 0
            heat = max(1, min(heat, 100))
            self.gameDisplay.blit(GEO[5], (0,0))
            bigText = pygame.font.Font("assets/ka1.ttf", 80)
            title_text = bigText.render("SCORE: " + str(SCORE), True, ORANGE)
            self.gameDisplay.blit(title_text, (380, 280))
            self.gameDisplay.blit(GEO[0], (20, 30))
            self.gameDisplay.blit(GEO[1], (260, 50))
            self.gameDisplay.blit(GEO[2], (510, 50))
            self.gameDisplay.blit(GEO[3], (760, 50))
            self.gameDisplay.blit(GEO[4], (1010, 50))
            self.gameDisplay.blit(HEAT_BAR_IMAGE, heat_rect, (0, 0, heat_rect.w/100*heat, heat_rect.h))
            if (heat_rect.w/100*heat) == 10:
                done = True
            pygame.display.flip()
            clock.tick(30)

def handlerEvent(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game.setExit(True)

def vormGame():
    pygame.init()
    pygame.display.set_caption('Vorm')
    pygame.display.set_icon(pygame.image.load('./assets/icon.png'))
    game = Game()
    while not game.getExit():
        handlerEvent(game)
        game.handlerMenu()
        pygame.display.update()
    pygame.quit()
    quit()

vormGame()