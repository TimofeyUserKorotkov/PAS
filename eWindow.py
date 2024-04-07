import pygame
import bButtonV3, eField
from bButtonV3 import *
pygame.init()

class Window:
    def __init__(self, screen, skin1, skin2, content=2, color_top=(76, 76, 76),
                 font=None, close_skin1="", close_skin2=None):
        self.screen = screen
        self.content = None
        self.color_top = color_top
        self.font = font

        self.x = 100
        self.y = 100
        self.width = 128
        
        self.clicked = False
        self.content = list()

        for i in range(content): 
            self.content.append(eField.Field(screen, self.x, self.y + 22 * i + 22, color=(50, 50, 50), 
                                             color_click=(190, 190, 190), font=font, skin1=skin1, skin2=skin2))
            print(content)
        self.closeBtn = bButtonV3.Button(screen, self.x + self.width - 22, self.y, 22, 22, image=close_skin1, click_img=close_skin2, font=font)
        self.main_rect = pygame.Rect(self.x, self.y, self.width - 22, 22)
        # self.arect = pygame.Rect(self.x, self.y, self.width, len(self.content) * 24 + 14)
        # self.brect = pygame.Rect(self.x, self.y + len(self.content) * 24 + 14, self.width, 22)

        self.fault = None

    def render(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                res = list()
                for i in range(len(self.content)): res.append(self.content[i].render(event))
                return res
        elif self.closeBtn.click_Button(event): return 0
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.main_rect.collidepoint(event.pos): 
            self.fault = [event.pos[0] - self.x, event.pos[1] - self.y]
            self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.clicked = False
        if self.clicked:
            self.x, self.y = event.pos[0] - self.fault[0], event.pos[1] - self.fault[1]
            for i in range(len(self.content)): self.content[i].x, self.content[i].y = self.x, self.y + 22 * i + 22

            self.closeBtn.x_pos_button, self.closeBtn.y_pos_button = self.x + self.width - 22, self.y

            self.main_rect.x, self.main_rect.y = self.x, self.y

        pygame.draw.rect(self.screen, self.color_top, self.main_rect)
        self.closeBtn.draw_Button(event)
        for i in self.content: i.render(event)

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RETURN:
        #         res = list()
        #         for i in range(len(self.content)): res.append(i.render(event))
        #         return res