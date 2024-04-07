import pygame
import json
from bButtonV3 import *
from eSlider import *
from eField import *
from filters import *
from tools import *
from cursor import *
from eWindow import *

import tkinter
from tkinter.filedialog import askopenfile, asksaveasfile

root = tkinter.Tk()
root.withdraw()
root.iconbitmap("icons\\icon.ico")

def cover(screen):
    with open("data/theme3.json", "r") as file:
        data = json.load(file)
        colors = data["colors"]

    pygame.draw.rect(screen, colors["sidebar_left"], (0, 0, 100, screen.get_height()))
    pygame.draw.rect(screen, colors["stripes"], (94, 0, 2, screen.get_height()))
    pygame.draw.rect(screen, colors["contrast_stripes_left"], (96, 0, 2, screen.get_height()))
    pygame.draw.rect(screen, colors["stripes"], (98, 0, 2, screen.get_height()))
    pygame.draw.rect(screen, colors["sidebar_right"], (screen.get_width() - 100, 0, 100, screen.get_height()))
    pygame.draw.rect(screen, colors["stripes"], (screen.get_width() - 96, 0, 2, screen.get_height()))
    pygame.draw.rect(screen, colors["contrast_stripes_right"], (screen.get_width() - 98, 0, 2, screen.get_height()))
    pygame.draw.rect(screen, colors["stripes"], (screen.get_width() - 100, 0, 2, screen.get_height()))
    pygame.draw.rect(screen, colors["bottom_bar"], (0, screen.get_height() - 22, screen.get_width(), 22))
    pygame.draw.rect(screen, colors["stripes"], (0, screen.get_height() - 22, screen.get_width(), 2))


def main():
    screen = pygame.display.set_mode((1300, 670), pygame.RESIZABLE)
    pygame.display.set_caption('SAiP')
    icon = pygame.image.load("icons\\r16x16.png").convert_alpha()
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    screen.fill((50, 50, 54))
    cursor = pygame.cursors.compile(pixelCur3)
    pygame.mouse.set_cursor((24, 24), (0, 0), *cursor)
    pFont = pygame.font.Font('fonts\craft.ttf', 16)

    skin1, skin2 = pygame.image.load("icons\menu_skin22221.png").convert(), pygame.image.load("icons\menu_skin2222.png").convert()
    skin1, skin2 = pygame.transform.scale(skin1, (176, 16)), pygame.transform.scale(skin2, (176, 16))

    easy_cropBTN = Button(screen, 1240, 50, 34, 34, "icons\crop1.png", click_img="icons\crop22.png")
    crop_imgBTN = Button(screen, 1240, 82, 34, 34, "icons\srs1.png", click_img="icons\srs22.png")
    filterBWBTN = Button(screen, 1240, 114, 34, 34, "icons\\bw1.png", click_img="icons\\bw2.png")
    filterPABTN = Button(screen, 1240, 146, 34, 34, "icons\pas1.png", click_img="icons\pas2.png")
    pencilBTN = Button(screen, 1240, 178, 34, 34, "icons\pencil21.png", click_img="icons\pencil222.png")
    crop_bgBTN = Button(screen, 1240, 210, 34, 34, "icons\cropbg1.png", click_img="icons\cropbg2.png")
    eraserBTN = Button(screen, 1240, 242, 34, 34, "icons\eae1.png", click_img="icons\eae2.png")
    rlBTN = Button(screen, 1240, 274, 34, 34, "icons\\rl21.png", click_img="icons\\rl22.png")
    pipetBTN = Button(screen, 1240, 306, 34, 34, "icons\pipet1.png", click_img="icons\pipet2.png")
    open_windowBTN = Button(screen, 1240, 338, 34, 34, "icons\\str1.png", click_img="icons\\str2.png")
    fillingBTN = Button(screen, 1240, 370, 34, 34, "icons\\drop1.png", click_img="icons\\drop2.png")
    bbbbbbBTN = Button(screen, 1240, 600, 20, 20, "o", font=pFont)
    rlW = Window(screen, "icons\pole221.png", "icons\pole222.png", 2, font=pFont, 
                    close_skin1="icons\close22222.png", close_skin2="icons\close11111.png")
    openW = Window(screen, "icons\pole221.png", "icons\pole222.png", 1, font=pFont, 
                    close_skin1="icons\close22222.png", close_skin2="icons\close11111.png")
    listOfBTNS = [easy_cropBTN, crop_imgBTN, filterBWBTN, filterPABTN, crop_bgBTN, eraserBTN, 
                  rlBTN, pipetBTN, pencilBTN, open_windowBTN, bbbbbbBTN, fillingBTN]
    sliderA = Slider(screen, 1216, 10, 8, 8, 19, 70, 4)
    slider_red = Slider(screen, 24, 446, 12, 6, 255, 50, 2)
    slider_green = Slider(screen, 24, 460, 12, 6, 255, 50, 2)
    slider_blue = Slider(screen, 24, 476, 12, 6, 255, 50, 2)
    menuA = Menu(screen, ["helpy", "---------"],
                 pFont, (189, 198, 255), skin=skin1, skin_click=skin2)

    run = True
    size = 100
    pixel_size = 2
    img = "BG"
    image = pygame.image.load("imgs\\" + img + ".png").convert_alpha()
    image = resolution(image, size, pixel_size)
    
    red, green, blue = 0, 0, 0
    colors = 4
    add = None
    toolID = 0
    activeID = None
    prID = 0
    

    cn = 20
    new_palette = create_palette(1, 1, 1, cn, 0, step=1)
    new_palette.extend([[250, 110, 110], [10, 186, 181], [122, 255, 224]])
    print(new_palette)
    cn = len(new_palette)
    size_pcs = int(255/cn**(1/2)/2)
    cs_n = int(cn**(1/2)) + 1 if cn**(1/2) % 1 != 0 else int(cn**(1/2))
    spacing = 2
    cs_n = 4
    size_p = 20
    palette = []
    for i in range(len(new_palette)):
        palette.append(Button(screen, 0, 50, size_pcs, size_pcs, color=new_palette[i], color_click=new_palette[i]))
    
    x_p = xfp = sxfp = 4
    y_p = yfp = syfp = 100
    y_p = 230
    yfp = 34
    syfp = 120
    x_img, y_img = 650 - image.get_width() // 2, 335 - image.get_height() // 2
    width_palette = size_p * (cn // cs_n) + spacing * (cn // cs_n + 1)
    width_apr = size_p * (cn % cs_n) + spacing * (cn % cs_n + 1)
    aprect = pygame.Rect(xfp, yfp + width_palette, width_apr, size_p + spacing)
    print("poxy34232454356456")
    info_y = screen.get_height() - 18
    colorofcpr = [10, 186, 181]
    collideRect = pygame.Rect(sxfp - 2, syfp - 2, size_p + spacing * 4, size_p + spacing * 4)
    
    newpixel_sizes = []
    newsizes = []
    newcanvs = []
    x_newimgs = []
    y_newimgs = []
    fxnewimgs = 0
    fynewimgs = 0
    curcanv = None
    newimgs_rects = []
    
    isdragMain = False
    
    dragNewimgsID = None
    selectedH = []

    while run:
        clock.tick(500)
        for event in pygame.event.get():

            curcanv = None
            for i in range(len(newcanvs)):
                try:
                    if newimgs_rects[i].collidepoint(event.pos):
                        curcanv = i
                except: pass

            if pencilBTN.click_Button(event): toolID = 0
            elif eraserBTN.click_Button(event): toolID = 1
            elif pipetBTN.click_Button(event):
                if toolID < 7: prID = toolID
                toolID = 11
            elif crop_imgBTN.click_Button(event): toolID = 3
            elif crop_bgBTN.click_Button(event): toolID = 4
            elif easy_cropBTN.click_Button(event): toolID = 5
            elif fillingBTN.click_Button(event): toolID = 6
            elif filterBWBTN.click_Button(event): filterBW(image)
            elif open_windowBTN.click_Button(event):
                if toolID < 7: prID = toolID
                toolID = 9
            elif rlBTN.click_Button(event):
                if toolID < 7: prID = toolID
                toolID = 10
            elif bbbbbbBTN.click_Button(event):
                #* new_palette = create_from_img(image)
                #* cn = len(new_palette)
                #* sxfp, syfp = xfp, yfp
                pr_canv = pygame.Surface.copy(newcanvs[0])
                pr_canv = pygame.transform.scale(pr_canv, (newsizes[0], newsizes[0]))
                newcanvs[0] = pygame.Surface((10, 10)).convert_alpha()
                newcanvs[0].fill(pygame.Color(0, 0, 0, 0))
                newcanvs[0].blit(pr_canv, (0, 0))
                newsizes[0] = 10
                newimgs_rects[0] = pygame.Rect(x_newimgs[0], y_newimgs[0], 10 * newpixel_sizes[0], 10 * newpixel_sizes[0])
                newcanvs[0].blit(pr_canv, (0, 0))
            elif filterPABTN.click_Button(event):
                if image.get_width() < image.get_height():
                    image = pygame.transform.scale(image, (int(size * (image.get_width() / image.get_height())), size))
                else:
                    image = pygame.transform.scale(image, (size, int(size * (image.get_height() / image.get_width()))))
                colors = filterPAS(image, par)
                image = pygame.transform.scale(image, (image.get_width() * pixel_size, image.get_height() * pixel_size))


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if aprect.collidepoint(event.pos) or palette_rect.collidepoint(event.pos):
                        cpccolor = list(screen.get_at(event.pos))
                        if cpccolor[:-1] in new_palette:
                            sxfp = ((event.pos[0] - xfp) // (size_p + spacing)) * (size_p + spacing) + xfp
                            syfp = ((event.pos[1] - yfp) // (size_p + spacing)) * (size_p + spacing) + yfp
                            slider_red.set_Slider(cpccolor[0])
                            slider_green.set_Slider(cpccolor[1])
                            slider_blue.set_Slider(cpccolor[2])
                            colorofcpr = [122, 255, 224]
                    if collideRect.collidepoint(event.pos): colorofcpr = [122, 255, 224]
                    if toolID == 11: toolID = prID
                    if imRect.collidepoint(event.pos):
                        if toolID == 0: activeID = 0
                        elif toolID == 1: activeID = 1
                        elif toolID == 7:
                            faultsDrag = [event.pos[0] - imRect[0], event.pos[1] - imRect[1]]
                            activeID = 2
                            isdragMain = True
                        else:
                            if image.get_width() < image.get_height():
                                image = pygame.transform.scale(image, (int(size * (image.get_width() / image.get_height())), size))
                            else:
                                image = pygame.transform.scale(image, (size, int(size * (image.get_height() / image.get_width()))))
                            xm = int((event.pos[0] - x_img) / pixel_size)
                            ym = int((event.pos[1] - y_img) / pixel_size)
                            if toolID == 3: crop_img(xm, ym, image)
                            elif toolID == 4: crop_bg(xm, ym, image)  
                            elif toolID == 5: easy_crop(xm, ym, image)
                            elif toolID == 6: image = filling_img(xm, ym, image, (cr, cg, cb))
                            image = pygame.transform.scale(image, (image.get_width() * pixel_size, image.get_height() * pixel_size))
                    else:
                        try:
                            if newimgs_rects[curcanv].collidepoint(event.pos):
                                if toolID == 8:
                                    selectedH[curcanv] = not selectedH[curcanv]
                                elif toolID == 0: activeID = 0
                                elif toolID == 1: activeID = 1
                                elif toolID == 7:
                                    faultsDrag = [event.pos[0] - newimgs_rects[curcanv][0], event.pos[1] - newimgs_rects[curcanv][1]]
                                    activeID = 2
                                    dragNewimgsID = curcanv
                        except: pass
                elif event.button == 4: add = 1
                elif event.button == 5: add = -1
                if add != None:
                    if (imRect.collidepoint(event.pos) and size * (pixel_size + add) < 3000 and pixel_size + add > 0):
                        pixel_size += add
                        image = resolution(image, size, pixel_size)
                    else:
                        try:
                            if (newimgs_rects[curcanv].collidepoint(event.pos) and newsizes[curcanv] * 
                                (newpixel_sizes[curcanv] + add) < 1500 and newpixel_sizes[curcanv] + add > 0):
                                newpixel_sizes[curcanv] += add
                                newcanvs[curcanv] = pygame.transform.scale(newcanvs[curcanv], (newsizes[curcanv] * newpixel_sizes[curcanv],
                                                                     newsizes[curcanv] * newpixel_sizes[curcanv]))
                                newimgs_rects[curcanv][2] = newsizes[curcanv] * newpixel_sizes[curcanv]
                                newimgs_rects[curcanv][3] = newsizes[curcanv] * newpixel_sizes[curcanv]
                        except: pass
                    add = None
            elif event.type == pygame.MOUSEBUTTONUP:
                colorofcpr = [10, 186, 181]
                activeID = None
                isdragMain = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    if toolID < 7: prID = toolID
                    toolID = 7
                    cursor = pygame.cursors.compile(pixelHand)
                    pygame.mouse.set_cursor((24, 24), (0, 0), *cursor)
                elif event.key == 13:
                    try:
                        image = pygame.image.load(path.name).convert_alpha()
                        image = resolution(image, size, pixel_size)
                    except: pass
                elif event.key == pygame.K_LALT:
                    if toolID < 7: prID = toolID
                    toolID = 8
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LCTRL:
                    cursor = pygame.cursors.compile(pixelCur3)
                    pygame.mouse.set_cursor((24, 24), (0, 0), *cursor)
                    toolID = prID
                elif event.key == pygame.K_LALT: toolID = prID
            elif event.type == pygame.VIDEORESIZE:
                for btn in listOfBTNS:
                    btn.x_pos_button = screen.get_width() - 60
                sliderA.x_bar, sliderA.x_pos = screen.get_width() - 84, screen.get_width() - 84 - sliderA.slider_width // 2
                info_y = screen.get_height() - 18

            if event.type == pygame.QUIT:
                image = pygame.transform.scale(image, (image.get_width() // (pixel_size), image.get_height() // (pixel_size)))
                canv = pygame.Surface((image.get_width(), image.get_height()))
                screen.blit(canv, (x_img, y_img))
                canv.blit(image, (x_img, y_img))
                # save_path = asksaveasfilename(title="My title")
                # # pygame.image.save(canv, "res\img.png")
                # pygame.image.save(image, save_path.name + "A.png")
                # save_file(image)
                # # pygame.image.save(canv, "res\img.png")
                pygame.image.save(image, "res\A.png")
                run = False


            if activeID == 2:
                if isdragMain:
                    x_img = event.pos[0] - faultsDrag[0]
                    y_img = event.pos[1] - faultsDrag[1]
                else:
                    try:
                        if dragNewimgsID != None and isdragMain == False:
                            newimgs_rects[dragNewimgsID][0] = event.pos[0] - faultsDrag[0]
                            newimgs_rects[dragNewimgsID][1] = event.pos[1] - faultsDrag[1]
                            x_newimgs[dragNewimgsID] = event.pos[0] - faultsDrag[0]
                            y_newimgs[dragNewimgsID] = event.pos[1] - faultsDrag[1]
                    except: pass
            if activeID == 0 and imRect.collidepoint(event.pos):
                try:
                    fw, fh = image.get_width(), image.get_height()
                    mouse_pos = pygame.mouse.get_pos()
                    image = pygame.transform.scale(image, (fw // pixel_size, fh // pixel_size))
                    pygame.draw.line(image, (cr, cg, cb), [(pr_mouse_pos[0] - x_img) // pixel_size, (pr_mouse_pos[1] - y_img) // pixel_size], 
                                     [(mouse_pos[0] - x_img) // pixel_size, (mouse_pos[1] - y_img) // pixel_size], 1)
                    image = pygame.transform.scale(image, (fw, fh))
                except: pass
            try:
                if activeID == 0 and newimgs_rects[curcanv].collidepoint(event.pos):
                        mouse_pos = pygame.mouse.get_pos()
                        newcanvs[curcanv] = pygame.transform.scale(newcanvs[curcanv], 
                                                                   (newcanvs[curcanv].get_width() // newpixel_sizes[curcanv], 
                                                                    newcanvs[curcanv].get_height() // newpixel_sizes[curcanv]))
                        pygame.draw.line(newcanvs[curcanv], (cr, cg, cb), 
                                        [(pr_mouse_pos[0] - x_newimgs[curcanv]) // newpixel_sizes[curcanv], 
                                         (pr_mouse_pos[1] - y_newimgs[curcanv]) // newpixel_sizes[curcanv]], 
                                        [(mouse_pos[0] - x_newimgs[curcanv]) // newpixel_sizes[curcanv], 
                                         (mouse_pos[1] - y_newimgs[curcanv]) // newpixel_sizes[curcanv]], 1)
                        newcanvs[curcanv] = pygame.transform.scale(newcanvs[curcanv], 
                                                               (newsizes[curcanv] * newpixel_sizes[curcanv], 
                                                                newsizes[curcanv] * newpixel_sizes[curcanv]))
            except: pass
            if activeID == 1 and imRect.collidepoint(event.pos):
                try:
                    fw, fh = image.get_width(), image.get_height()
                    mouse_pos = pygame.mouse.get_pos()
                    image = pygame.transform.scale(image, (fw // pixel_size, fh // pixel_size))
                    pygame.draw.line(image, (0, 0, 0, 0), [(pr_mouse_pos[0] - x_img) // pixel_size, (pr_mouse_pos[1] - y_img) // pixel_size], 
                                     [(mouse_pos[0] - x_img) // pixel_size, (mouse_pos[1] - y_img) // pixel_size], 10)
                    image = pygame.transform.scale(image, (fw, fh))
                except: pass

            screen.fill((50, 50, 54))
            screen.blit(image, (x_img, y_img))
            pygame.draw.rect(screen, (5, 5, 5), (x_img - 2, y_img - 2, 
                                      image.get_width() + 4, image.get_height() + 4), 2)
            for i in range(len(newcanvs)):
                newcanvs[i] = pygame.transform.scale(newcanvs[i], (newsizes[i] * newpixel_sizes[i],
                                                                   newsizes[i] * newpixel_sizes[i]))
                screen.blit(newcanvs[i], (x_newimgs[i], y_newimgs[i]))
                if selectedH[i]:
                    pygame.draw.rect(screen, (10, 186, 181), 
                                     (x_newimgs[i] - 4, y_newimgs[i] - 4, 
                                      newcanvs[i].get_width() + 8, newcanvs[i].get_height() + 8), 2)
                    pygame.draw.rect(screen, (5, 5, 5), 
                                     (x_newimgs[i] - 2, y_newimgs[i] - 2, 
                                      newcanvs[i].get_width() + 4, newcanvs[i].get_height() + 4), 2)
                else:
                    pygame.draw.rect(screen, (5, 5, 5), 
                                     (x_newimgs[i] - 2, y_newimgs[i] - 2, 
                                      newcanvs[i].get_width() + 4, newcanvs[i].get_height() + 4), 2)
            cover(screen)
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #* width_palette = size_p * (cn // cs_n + 1) + spacing * (cn // cs_n + 2)
            width_palette = size_p * (cn // cs_n) + spacing * (cn // cs_n + 1)

            if cn % cs_n != 0:
                width_apr = size_p * (cn % cs_n) + spacing * (cn % cs_n + 1)
                aprect = pygame.Rect(xfp, yfp + width_palette, width_apr, size_p + spacing)
                pygame.draw.rect(screen, (25, 25, 25), aprect)

            palette_rect = pygame.Rect(xfp, yfp, size_p * cs_n + spacing * (cs_n + 1), width_palette)
            pygame.draw.rect(screen, (25, 25, 25), palette_rect)
            for i in range(len(new_palette)):
                x_p = xfp + i * (size_p + spacing) - (size_p + spacing) * cs_n * (i // cs_n) + 2
                y_p = yfp + (size_p + spacing) * (i // cs_n) + 2
                pygame.draw.rect(screen, new_palette[i], pygame.Rect(x_p, y_p, size_p, size_p))
            collideRect = pygame.Rect(sxfp - 2, syfp - 2, size_p + spacing * 4, size_p + spacing * 4)
            pygame.draw.rect(screen, (40, 40, 40), pygame.Rect(sxfp, syfp, size_p + spacing * 2, size_p + spacing * 2), 2)
            pygame.draw.rect(screen, (40, 40, 40), pygame.Rect(sxfp - 4, syfp - 4, size_p + spacing * 6, size_p + spacing * 6), 2)
            pygame.draw.rect(screen, colorofcpr, collideRect, 2)

            for btn in listOfBTNS:
                btn.draw_Button(event)
            imRect = image.get_rect()
            imRect[0], imRect[1] = x_img, y_img

            if toolID == 11:
                mouse_pos = pygame.mouse.get_pos()
                color_pick = screen.get_at((mouse_pos[0], mouse_pos[1]))
                red, green, blue = color_pick[0], color_pick[1], color_pick[2]
                slider_red.set_Slider(red)
                slider_green.set_Slider(green)
                slider_blue.set_Slider(blue)
            par = sliderA.render(event) + 1
            cr, cg, cb = slider_red.render(event), slider_green.render(event), slider_blue.render(event)
            pygame.draw.rect(screen, (cr, cg, cb), (8, 444, 4, 36))
            screen.blit(pFont.render(str(par), False, (250, 130, 130)), (sliderA.x_bar + 38, 15))
            screen.blit(pFont.render("cn=" + str(colors), False, (210, 210, 210)), (48, info_y))
            screen.blit(pFont.render(str(int(clock.get_fps())), False, (250, 250, 100)), (2, info_y))

            try:
                if toolID == 9:
                    path = askopenfile(title="My title", filetypes=[("PNG", ".png"), ("JPG", ".jpg")])
                    try:
                        image = pygame.image.load(path.name).convert_alpha()
                        image = resolution(image, size, pixel_size)
                    except: pass
                    toolID = prID
                if toolID == 10:
                    res = rlW.render(event)
                    if res == 0: toolID = prID
                    elif res != None:
                        toolID == prID
                        w, h = res
                        if h == "":
                            try:
                                pixel_size, size = 1000 // int(w), 1000 // (1000 // int(w))
                            except: pass
                        else:
                            try:
                                pixel_size = 1
                                image = pygame.transform.scale(image, (int(w), int(h)))
                                image = pygame.transform.scale(image, (int(w) * pixel_size, int(h) * pixel_size))
                                size = image.get_width() // pixel_size if image.get_width() > image.get_height() else image.get_height()
                            except: pass
            except: pass

            point = menuA.draw_Menu(event)
            if point == 1 and len(newcanvs) < 16:
                newimgs_rects.append(pygame.Rect(fxnewimgs, fynewimgs, 32 * 8, 32 * 8))
                x_newimgs.append(fxnewimgs)
                y_newimgs.append(fynewimgs)
                newpixel_sizes.append(8)
                ccanv = pygame.Surface((32, 32)).convert_alpha()
                ccanv.fill(pygame.Color(0, 0, 0, 0))
                newsizes.append(32)
                newcanvs.append(ccanv)
                selectedH.append(False)
            
            #*think
            pr_mouse_pos = pygame.mouse.get_pos()
            pr_mouse_pos = [pr_mouse_pos[0], pr_mouse_pos[1]]
        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()