import pygame
pygame.init()

class Button:
    def __init__(self, screen, x, y, width, hight, image="", color=(240, 240, 240), 
                 color_click=(210, 210, 210), font_size=18, edge_width=0, font="consolas", click_img=None):
        self.screen = screen
        self.x_pos_button = x
        self.y_pos_button = y
        self.width_button = width
        self.hight_button = hight
        self.color_button = color
        self.color_on_click_button = color_click

        # self.image_button = pygame.image.load(image_button)
        self.image_button = image
        
        self.default_img = image

        self.edge_width = edge_width
        self.color = self.color_button
        self.click = 0
        self.if_click = 0
        self.button_rect = pygame.Rect(self.x_pos_button, self.y_pos_button, self.width_button, self.hight_button)
        # self.img_size = self.image_button.convert().get_rect().size

        self.font_size = font_size
        self.font = font

        self.img = 0
        for i in self.image_button:
            if i == ".":
                self.img = 1

        if self.img == 1:
            self.img_size = pygame.image.load(self.image_button).convert().get_rect().size

        self.click_img = click_img

    def draw_Button(self, event):
        self.button_rect = pygame.Rect(self.x_pos_button, self.y_pos_button, self.width_button, self.hight_button)
        if self.button_rect.collidepoint(pygame.mouse.get_pos()) == False:
            if self.click_img == None:
                    self.color = self.color_button
            else:
                self.image_button = self.default_img
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button_rect.collidepoint(event.pos):
                if self.click_img == None:
                    self.color = self.color_on_click_button
                self.click = 1
        if self.click == 1 and self.button_rect.collidepoint(pygame.mouse.get_pos()):
            if self.click_img == None:
                self.color = self.color_on_click_button
            else:
                self.image_button = self.click_img
        if event.type == pygame.MOUSEBUTTONUP and self.click == 1 and event.button == 1:
            self.click = 0
            if self.button_rect.collidepoint(event.pos):
                if self.click_img == None:
                    self.color = self.color_button
                else:
                    self.image_button = self.default_img

        if self.click_img == None:
            pygame.draw.rect(self.screen, self.color, self.button_rect, 0)
            pygame.draw.rect(self.screen, self.color, self.button_rect, self.edge_width)
        # self.screen.blit(self.image_button, (self.width_button/2 - self.img_size[0]/2 + self.x_pos_button, self.hight_button/2 - self.img_size[1]/2 + self.y_pos_button))

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        if self.img == 1:
            img = pygame.image.load(self.image_button).convert_alpha()
            if self.click_img == None:
                img = pygame.transform.scale(img, (self.width_button - img.get_width() // 4, self.hight_button - img.get_height() // 4))
                self.screen.blit(img, (self.x_pos_button - img.get_width() // 2 + self.width_button // 2, 
                                   self.y_pos_button - img.get_height() // 2 + self.hight_button // 2))
            else:
                img = pygame.transform.scale(img, (self.width_button, self.hight_button))
                self.screen.blit(img, (self.x_pos_button, self.y_pos_button))
        else:
            self.screen.blit(pygame.font.SysFont(self.font, self.font_size).render(str(self.image_button), False, (33, 33, 33)), 
                             (self.x_pos_button + self.width_button // 2 - 5 * len(self.image_button), 
                              self.y_pos_button + self.hight_button // 2 - 11))
            # self.screen.blit(pygame.font.SysFont("consolas", 18).render(str(self.image_button), False, (33, 33, 33)), 
            #                  (self.x_pos_button + self.width_button // 2 - 18 // 2 * len(self.image_button), (self.y_pos_button + self.hight_button // 2) - 18))

    def click_Button(self, event):
        # if self.button_rect.collidepoint(pygame.mouse.get_pos()):
        #     return 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button_rect.collidepoint(event.pos):
                self.if_click = 1
        if event.type == pygame.MOUSEBUTTONUP and self.if_click == 1 and event.button == 1:
            self.if_click = 0
            if self.button_rect.collidepoint(event.pos):
                return True


class Menu:
    def __init__(self, screen, points, font=None, font_color=(0, 0, 250), skin=None, skin_click=None):
        self.screen = screen
        self.points = points
        self.click = 3
        self.click_on = 0
        self.if_click = 0
        self.f = 0
        self.x = 0
        self.y = 0
        self.y_stat = 0

        self.per = 0

        self.font = font
        self.font_color = font_color

        self.skin = skin
        self.skin_click = skin_click

        self.askin = skin

    def draw_Menu(self, event):
        point = None
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                self.click = 1
                self.x, self.y = pygame.mouse.get_pos()
                self.y_stat = self.y

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                self.click = 0
        
        button_rect = pygame.Rect(self.x, self.y, 180, 18 * len(self.points) + 2)
        for i in range(len(self.points)):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button_rect.collidepoint(pygame.mouse.get_pos()) == False:
                self.click = 1

        if self.click == 0:
            if self.skin != None:
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.x, self.y, 180, 18 * len(self.points) + 2), 0)
            for i in range(len(self.points)):
                if self.skin == None:
                    color = (255, 255, 255)
                else:
                    self.askin = self.skin
                button_rect = pygame.Rect(self.x, self.y, 180, 18)
                if button_rect.collidepoint(pygame.mouse.get_pos()) == False:
                    if self.skin == None:
                        color = (255, 255, 255)
                    else:
                        self.askin = self.skin
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if button_rect.collidepoint(event.pos):
                        if self.skin == None:
                            color = (200, 200, 200)
                        else:
                            self.askin = self.skin_click
                        self.click_on = 1
                        # *****
                        # print(i + 1)
                        # *****
                        self.click = 1
                        # *****
                        point = i + 1
                        # *****
                if button_rect.collidepoint(pygame.mouse.get_pos()):
                    if self.skin == None:
                        color = (200, 200, 200)
                    else:
                        self.askin = self.skin_click
                if event.type == pygame.MOUSEBUTTONUP and self.click_on == 1 and event.button == 1:
                    self.click_on = 0
                    if button_rect.collidepoint(event.pos):
                        if self.skin == None:
                            color = (255, 255, 255)
                        else:
                            self.askin = self.skin
                if self.skin == None:
                    pygame.draw.rect(self.screen, color, button_rect, 0)
                else:
                    self.screen.blit(self.askin, (self.x + 2, self.y + 2))
                if self.font == None:
                    self.screen.blit(pygame.font.SysFont("comfortaa", 21).render(str(self.points[i]), False, (0, 0, 250)), 
                                    (self.x + 4, self.y + 2))
                else:
                    self.screen.blit(self.font.render(str(self.points[i]), False, self.font_color), 
                                    (self.x + 4, self.y + 2))
                self.y += 18
            self.y = self.y_stat
            return point