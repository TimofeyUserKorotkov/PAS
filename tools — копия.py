import pygame

def easy_crop(event, image, pr_width, pr_height, x=0, y=0):
    cpixel_color = image.get_at(((event.pos[0] - x) // (pr_width // image.get_width()), 
                                 (event.pos[1] - y) // (pr_height // image.get_height())))

    for i in range(image.get_height()):
        for j in range(image.get_width()):

            new_color = image.get_at((j, i))
            red_fault = cpixel_color[0] - new_color[0]
            green_fault = cpixel_color[1] - new_color[1]
            blue_fault = cpixel_color[2] - new_color[2]

            if (abs(red_fault - green_fault) < 7) and (abs(green_fault - blue_fault) < 7):
                image.set_at((j, i), (0, 0, 0, 0))

def crop_img(event, image, x=0, y=0):
    cpixel_color = image.get_at((event.pos[0] - x, event.pos[1] - y))
    crop_side_x = image.get_width()
    stepx = 1

    for xsides in range(2):
        for j in range(event.pos[0] - x, crop_side_x, stepx):
            new_color = image.get_at((j, event.pos[1] - y))
            red_fault = cpixel_color[0] - new_color[0]
            green_fault = cpixel_color[1] - new_color[1]
            blue_fault = cpixel_color[2] - new_color[2]

            if ((abs(red_fault - green_fault) >= 7) or (abs(green_fault - blue_fault) >= 7)) and new_color[3] != 0:
                break

            crop_side_y = image.get_height()
            stepy = 1

            for ysides in range(2):
                for i in range(event.pos[1] - y, crop_side_y, stepy):

                    new_color = image.get_at((j, i))
                    red_fault = cpixel_color[0] - new_color[0]
                    green_fault = cpixel_color[1] - new_color[1]
                    blue_fault = cpixel_color[2] - new_color[2]

                    if (abs(red_fault - green_fault) < 7) and (abs(green_fault - blue_fault) < 7):
                        image.set_at((j, i), (0, 0, 0, 0))
                    elif new_color[3] != 0:
                        break

                crop_side_y = -1
                stepy = -1
            crop_side_x = -1
            stepx = -1

def crop_bg(event, image, x=0, y=0):
    crop_side_x = image.get_width()
    stepx = 1

    for xsides in range(2):
        for j in range(event.pos[0] - x, crop_side_x, stepx):
            new_color = image.get_at((j, event.pos[1] - y))
            if new_color[2] == 0 and new_color[3] == 0:
                break
            crop_side_y = image.get_height()
            stepy = 1
            for ysides in range(2):
                for i in range(event.pos[1] - y, crop_side_y, stepy):
                    new_color = image.get_at((j, i))
                    if new_color[2] != 0 or new_color[3] != 0:
                        image.set_at((j, i), (0, 0, 255, 0))
                    else:
                        break

                crop_side_y = -1
                stepy = -1
            crop_side_x = -1
            stepx = -1

# def resolution(image, size, pixel_size, ratio, loc):
#     image = pygame.image.load(loc).convert_alpha()
#     if image.get_width() < image.get_height():
#                 image = pygame.transform.scale(image, (int(size * (image.get_width() / image.get_height())), size))
#     else:
#         image = pygame.transform.scale(image, (size, int(size * (image.get_height() / image.get_width()))))
#     return pygame.transform.scale(image, (image.get_width() * pixel_size * ratio, image.get_height() * pixel_size * ratio))

def resolution(image, size, pixel_size, loc):
    image = pygame.image.load(loc).convert_alpha()
    if image.get_width() < image.get_height():
                image = pygame.transform.scale(image, (int(size * (image.get_width() / image.get_height())), size))
    else:
        image = pygame.transform.scale(image, (size, int(size * (image.get_height() / image.get_width()))))
    return pygame.transform.scale(image, (image.get_width() * pixel_size, image.get_height() * pixel_size))

def create_palette(r, g, b, quantity, rich=0, step=1):
    palette = []
    cols, colors = [r, g, b], [r, g, b]
    cols.sort()
    part = 255 // cols[-1] // quantity if cols[-1] != 0 else 0
    bs = 255 // rich - cols[-1] * part * quantity if rich == 1 else 0
    bs = bs // cols[-1] if cols[-1] != 0 else 0
    for i in range(1, quantity + 1, step):
        palette.append([color * part * i + bs * color for color in colors])
    return palette

def create_from_img(image):
    palette = []
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            ccolor = image.get_at((x, y))
            color = [ccolor[0], ccolor[1], ccolor[2]]
            if color not in palette:
                palette.append(color)
    return palette

def filling(xm, ym, image, color):
    cpixel_color = image.get_at((xm, ym))
    for i in range(image.get_height()):
        for j in range(image.get_width()):
            new_color = image.get_at((j, i))
            if new_color == cpixel_color:
                image.set_at((j, i), color)

def filling_img(xm, ym, image, color):
    cpixel_color = image.get_at((xm, ym))
# def filling_img(event, image, color, x=0, y=0):
    # cpixel_color = image.get_at((event.pos[0] - x, event.pos[1] - y))
    img = pygame.Surface.copy(image)
    # img.append(image)
    crop_side_x = image.get_width()
    stepx = 1
    for xsides in range(2):
        for j in range(xm, crop_side_x, stepx):
            new_color = image.get_at((j, ym))
            if new_color != cpixel_color:
                break
            crop_side_y = image.get_height()
            stepy = 1
            for ysides in range(2):
                for i in range(ym, crop_side_y, stepy):
                    new_color = image.get_at((j, i))
                    if new_color == cpixel_color:
                        img.set_at((j, i), color)
                    else:
                        break
                crop_side_y = -1
                stepy = -1
            crop_side_x = -1
            stepx = -1

    # img.set_at((xm, ym), color)
    return img
    # return image