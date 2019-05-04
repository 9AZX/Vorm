class Option:
    is_hovered = False
    def __init__(self, text, pos, menuFont, gameDisplay):
        self.text = text
        self.pos = pos
        self.set_rect(menuFont)
        self.draw(gameDisplay, menuFont)

    def setText(self, newText):
        self.text = newText

    def draw(self, gameDisplay, menuFont):
        self.rend = menuFont.render(self.text, True, self.get_color())
        gameDisplay.blit(self.rend, (self.pos))

    def get_color(self):
        if self.is_hovered:
            return (100, 100, 100)
        else:
            return (0, 0, 0)

    def set_rect(self, menuFont):
        self.rend = menuFont.render(self.text, True, self.get_color())
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos