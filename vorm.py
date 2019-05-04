#!python

import pygame as game
import sys

# from sokoban_game import game_loop

class Option:
    is_hovered = False
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()

    def draw(self):
        self.set_rend()
        game_display.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())

    def get_color(self):
        if self.is_hovered:
            return (100, 100, 100)
        else:
            return (0, 0, 0)

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos


def background(x, y):
    game_display.blit(game.image.load("assets/images/background.jpg"), (x, y))

def logo(x, y):
    game_display.blit(game.image.load("assets/images/top_logo.png"), (x, y))

def game_ft():
    bool_game = 1
    while bool_game == 1:
        print("Game\n")
        # bool_game = game_loop(game_display)

def options_ft():
    print("options")

def menu_ft(exit):
    background(0, 0)
    logo(630, 60)
    game.event.pump()
    for option in options:
        if option.rect.collidepoint(game.mouse.get_pos()):
            option.is_hovered = True
        else:
            option.is_hovered = False
        option.draw()
    if (game.mouse.get_pressed()[0] and options[0].rect.collidepoint(
            game.mouse.get_pos())):
        game_ft()
    if (game.mouse.get_pressed()[0] and options[1].rect.collidepoint(
            game.mouse.get_pos())):
        options_ft()
    if (game.mouse.get_pressed()[0] and options[2].rect.collidepoint(
            game.mouse.get_pos())):
        sys.exit(0)

if __name__ == '__main__':

    exit = False
    game_state = 1

    game.init()
    game_display = game.display.set_mode((1920, 1080))
    menu_font = game.font.Font("assets/ka1.ttf", 40)
    options = [Option("PLAY", (950, 250 + 20)),
                Option("OPTIONS", (950, 295 + 20)),
                Option("EXIT", (950, 340 + 20))]

    while not exit:
        for event in game.event.get():
            if event.type == game.QUIT:
                exit = True
            if event.type == game.KEYDOWN:
                if event.key == game.K_ESCAPE:
                    exit = True
                if event.key == game.K_p:
                    game_ft()

        menu_ft(exit)
        game.display.update()

    game.quit()
    quit()