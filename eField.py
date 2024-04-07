import pygame
pygame.init()

class Field:
    def __init__(self, screen, x, y, width=120, color=(50, 50, 50), 
                 color_click=(210, 210, 210), font_size=16, font=None, skin1=None, skin2=None):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.first_width = width
        # self.height = height
        self.color = color
        self.color_on_click = color_click
        self.field_color = color
        self.font_size = font_size

        # self.field = pygame.Rect(x, y, width, height)
        self.active = False
        self.text = ""

        self.font = font

        if skin1 != None:
            self.skin1 = pygame.image.load(skin1).convert_alpha()
            self.skin2 = pygame.image.load(skin2).convert_alpha()

            self.skin1 = pygame.transform.scale(self.skin1, (128, 24))
            self.skin2 = pygame.transform.scale(self.skin2, (128, 24))
        else: self.skin1 = None
        self.skin = self.skin1

    def render(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: return self.text
        if self.font == None:
            txt_surface = pygame.font.Font(None, self.font_size).render(self.text, True, (240, 240, 240))
        else:
            txt_surface = self.font.render(self.text, True, (240, 240, 240))
        if self.skin1 == None: self.field = pygame.Rect(self.x, self.y, self.width, txt_surface.get_height())
        else: self.field = pygame.Rect(self.x, self.y, self.skin.get_width(), self.skin.get_height())
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = True if self.field.collidepoint(event.pos) else False
            if self.skin1 == None: self.field_color = self.color_on_click if self.active else self.color
            else: self.skin = self.skin2 if self.active else self.skin1

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE: self.text = self.text[:-1]
                elif txt_surface.get_width() + 8 < self.width: self.text += event.unicode

        if self.font == None:
            txt_surface = pygame.font.Font(None, self.font_size).render(self.text, True, (240, 240, 240))
        else:
            txt_surface = self.font.render(self.text, True, (240, 240, 240))

        self.width = max(self.width, txt_surface.get_width())
        self.field.w = self.width

        if self.skin == None:
            pygame.draw.rect(self.screen, self.field_color, self.field, 2)
            self.screen.blit(txt_surface, (self.field.x + 2, self.field.y + self.field.h - txt_surface.get_height() + 2))
        else:
            self.screen.blit(self.skin, (self.x, self.y))
            self.screen.blit(txt_surface, (self.x + 6, self.y + self.skin.get_height() - txt_surface.get_height() - 2))

        return self.text
