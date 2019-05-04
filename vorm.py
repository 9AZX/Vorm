#!python

import pygame
import sys

class Game:
    def __init__(self):
        self.gameState = 1
        self._exit = False
        self.gameDisplay = pygame.display.set_mode((1200, 859))
        self.menuFont = pygame.font.Font("assets/ka1.ttf", 40)
        self.options = [Option("PLAY", (520, 500), self.menuFont, self.gameDisplay),
                        Option("OPTIONS", (520, 555), self.menuFont, self.gameDisplay),
                        Option("EXIT", (520, 605), self.menuFont, self.gameDisplay)]

    def getExit(self):
        return self._exit

    def setExit(self, status):
        self._exit = status

    def setBackground(self, x, y):
        self.gameDisplay.blit(pygame.image.load("assets/images/background.jpg"), (x, y))

    def handlerMenu(self):
        self.setBackground(0, 0)
        pygame.event.pump()
        for option in self.options:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.is_hovered = True
            else:
                option.is_hovered = False
            option.draw(self.gameDisplay, self.menuFont)
        if (pygame.mouse.get_pressed()[0] and options[0].rect.collidepoint(pygame.mouse.get_pos())):
            game_ft()
        if (pygame.mouse.get_pressed()[0] and options[1].rect.collidepoint(pygame.mouse.get_pos())):
            options_ft()
        if (pygame.mouse.get_pressed()[0] and options[2].rect.collidepoint(pygame.mouse.get_pos())):
            sys.exit(0)

    def game_ft():
        print("Game\n")

    def options_ft():
        print("options")

class Option:
    is_hovered = False
    def __init__(self, text, pos, menuFont, gameDisplay):
        self.text = text
        self.pos = pos
        self.set_rect(menuFont)
        self.draw(gameDisplay, menuFont)

    def draw(self, gameDisplay, menuFont):
        self.set_rend(menuFont)
        gameDisplay.blit(self.rend, (self.pos))

    def set_rend(self, menuFont):
        self.rend = menuFont.render(self.text, True, self.get_color())

    def get_color(self):
        if self.is_hovered:
            return (100, 100, 100)
        else:
            return (0, 0, 0)

    def set_rect(self, menuFont):
        self.set_rend(menuFont)
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

def vormGame():
    pygame.init()
    game = Game()

    while not game.getExit():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.setExit(True)

        game.handlerMenu()
        pygame.display.update()

    pygame.quit()
    quit()

vormGame()