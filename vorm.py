#!python

import pygame
import sys
from options import Option
class Game:
    def __init__(self):
        self.gameState = 1
        self._exit = False
        self.gameDisplay = pygame.display.set_mode((1200, 859))
        self.menuFont = pygame.font.Font("assets/wayner.ttf", 40)
        self.options = [Option("PLAY", (540, 510), self.menuFont, self.gameDisplay),
                        Option("OPTIONS", (505, 575), self.menuFont, self.gameDisplay),
                        Option("EXIT", (548, 635), self.menuFont, self.gameDisplay)]

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
            optionMenu(self.options[0])
        if (pygame.mouse.get_pressed()[0] and options[2].rect.collidepoint(pygame.mouse.get_pos())):
            sys.exit(0)

    def gameHandler():
        print("Game\n")

    def optionHandler():
        exit = False
        clock = pygame.time.Clock()

        # while not exit:                                                     #
        #     for event in game.event.get():                                  #
        #         if event.type == game.QUIT:                                 #
        #             game.quit()                                             #
        #             quit()                                                  #
        #         if event.type == game.KEYDOWN:                              # boucle de detection des inputs
        #             if event.key == game.K_ESCAPE:                          #
        #                 exit = True                                         #
        #             if event.key == game.K_r:                               #
        #                 exit = True                                         #
        #                 restart = True                                      #

        #     game_interaction(map, player)
        #     if player.win(map):
        #         exit = True
        #         win = True
        #     place_map(game_display, map, images)
        #     place_sprite(game_display, player)
        #     game.display.update()
        #     clock.tick(10)
        # if win:
        #     win_loop(game_display, map, images, player)
        # if restart:
        #     return 1
        # return 0

def optionMenu(option):
    pass

def handlerEvent(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game.setExit(True)

def vormGame():
    pygame.init()
    game = Game()

    while not game.getExit():
        handlerEvent(game)
        game.handlerMenu()
        pygame.display.update()

    pygame.quit()
    quit()

vormGame()