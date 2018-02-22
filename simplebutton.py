import pygame

class button:

    def __init__(self,display, x, y, w, h, text, fg, bg, f, f2):
        self.pos_x = x
        self.pos_y = y
        self.width = w
        self.height = h
        self.text = text
        self.fg_color = fg
        self.bg_color = bg
        self.target_display = display
        self.func = f(f2)

    def pressed(self, x, y):
        if self.pos_x < x < self.pos_x + self.width and self.pos_y < y < self.pos_y + self.height:
            print("clicked")
            self.func


    def draw(self, target):
        pygame.draw.rect(self.target_display, self.bg_color, (self.pos_x, self.pos_y, self.width, self.height))
        myfont = pygame.font.SysFont('Arial', 20)
        textsurface = myfont.render(self.text, False, self.fg_color)
        self.target_display.blit(textsurface, (self.pos_x + self.width/2 - textsurface.get_width()/2,\
                                               self.pos_y + self.height/2 - textsurface.get_height()/2))


