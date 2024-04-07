import pygame
pygame.init()

class Slider:
    def __init__(self, screen, x, y, width, height,  par, bar_width=None, bar_height=None, 
                 color=(240, 240, 240), color_click=(210, 210, 210), bar_color=(120, 120, 120)):
        self.screen = screen
        self.x_bar = x
        self.y_pos = y
        self.slider_width = width
        self.slider_height = height
        self.slider_color = color
        self.slider_color_on_click = color_click
        self.bar_color = bar_color
        self.par = par

        self.x_pos = x - self.slider_width // 2
        self.color = self.slider_color
        self.click = 0

        if bar_width == None:
            self.bar_width = self.slider_width * 18
        else:
            self.bar_width = bar_width

        if bar_height == None:
            self.bar_height = self.slider_width // 3
        else:
            self.bar_height = bar_height

        self.bar_rect = pygame.Rect(self.x_bar, self.y_pos, self.bar_width, self.bar_height)
        self.slider_rect = pygame.Rect(self.x_pos, self.y_pos - self.slider_height / 2 + self.bar_height // 2, self.slider_width, self.slider_height)

    def render(self, event):
        self.bar_rect = pygame.Rect(self.x_bar, self.y_pos, self.bar_width, self.bar_height)
        self.slider_rect = pygame.Rect(self.x_pos, self.y_pos - self.slider_height / 2 + self.bar_height // 2, self.slider_width, self.slider_height)
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and (self.slider_rect.collidepoint(mouse_pos) or self.bar_rect.collidepoint(mouse_pos)):
            self.click = 1
        if event.type == pygame.MOUSEBUTTONUP:
            self.click = 0
        
        if self.click == 1:
            self.x_pos = mouse_pos[0] - self.slider_width // 2
            self.color = self.slider_color_on_click
        else:
            self.color = self.slider_color
        
        if self.x_pos < self.x_bar - self.slider_width / 2:
            self.x_pos = self.x_bar - self.slider_width / 2
        elif self.x_pos > self.x_bar + self.bar_width - self.slider_width / 2:
            self.x_pos = self.x_bar + self.bar_width - self.slider_width / 2

        self.slider_rect = pygame.Rect(self.x_pos, self.y_pos - self.slider_height / 2 + self.bar_height / 2, self.slider_width, self.slider_height)
        pygame.draw.rect(self.screen, self.bar_color, self.bar_rect, 0)
        pygame.draw.rect(self.screen, self.color, self.slider_rect, 0)

        float_val = (self.x_pos + self.slider_width / 2 - self.x_bar) / (self.bar_width / self.par)
        cvalue = int((self.x_pos + self.slider_width / 2 - self.x_bar) / (self.bar_width / self.par))
        if cvalue < float_val - 0.5:
            cvalue += 1

        return cvalue
    
    def set_Slider(self, value):
        self.x_pos = (self.bar_width / self.par) * value + self.x_bar - self.slider_width / 2
        self.slider_rect = pygame.Rect(self.x_pos, self.y_pos - self.slider_height / 2 + self.bar_height / 2, self.slider_width, self.slider_height)
        pygame.draw.rect(self.screen, self.bar_color, self.bar_rect, 0)
        pygame.draw.rect(self.screen, self.color, self.slider_rect, 0)

