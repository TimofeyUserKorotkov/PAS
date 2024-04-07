import pygame

def filterBW(image):
    for i in range(image.get_width()):
        for j in range(image.get_height()):
            ccolor = image.get_at((i, j))
            if ccolor[3] != 0:
                cmid = (ccolor[0] + ccolor[1] + ccolor[2]) // 3
                image.set_at((i, j), (cmid, cmid, cmid, 255))

def filterPA(image):
    colors = []
    tones = []
    for i in range(image.get_width()):
        for j in range(image.get_height()):
            ctone = [0, 0, 0]
            ccolor = list(image.get_at((i, j)))
            sort_colors = sorted(ccolor[:-1])
            ctone[0] = sort_colors.index(ccolor[0])
            ctone[1] = sort_colors.index(ccolor[1])
            ctone[2] = sort_colors.index(ccolor[2])
            if ctone not in tones and ccolor[3] != 0:
                tones.append(ctone)
                colors.append(ccolor)

    for i in range(image.get_width()):
        for j in range(image.get_height()):
            ccolor = list(image.get_at((i, j)))
            if ccolor[3] != 0:
                ctone = [0, 0, 0]
                sort_colors = sorted(ccolor[:-1])
                ctone[0] = sort_colors.index(ccolor[0])
                ctone[1] = sort_colors.index(ccolor[1])
                ctone[2] = sort_colors.index(ccolor[2])
                image.set_at((i, j), colors[tones.index(ctone)])

def filterPAL(image):
    colors = []
    tones = []
    levels = 10
    for i in range(image.get_width()):
        for j in range(image.get_height()):
            ctone = [0, 0, 0, 0]
            ccolor = list(image.get_at((i, j)))
            sort_colors = sorted(ccolor[:-1])
            ctone[0] = sort_colors.index(ccolor[0])
            ctone[1] = sort_colors.index(ccolor[1])
            ctone[2] = sort_colors.index(ccolor[2])
            ctone[3] = int(((ccolor[0] + ccolor[1] + ccolor[2]) / 3) // (255 / levels))
            if ctone not in tones and ccolor[3] != 0:
                tones.append(ctone)
                colors.append(ccolor)
    print(tones)
    print(colors)

    for i in range(image.get_width()):
        for j in range(image.get_height()):
            ccolor = list(image.get_at((i, j)))
            if ccolor[3] != 0:
                ctone = [0, 0, 0, 0]
                sort_colors = sorted(ccolor[:-1])
                ctone[0] = sort_colors.index(ccolor[0])
                ctone[1] = sort_colors.index(ccolor[1])
                ctone[2] = sort_colors.index(ccolor[2])
                ctone[3] = ((ccolor[0] + ccolor[1] + ccolor[2]) / 3) // (255 / levels)
                image.set_at((i, j), colors[tones.index(ctone)])

def filterPALS(image, levels):
    colors = []
    tones = []
    # levels = 10
    for i in range(image.get_width()):
        for j in range(image.get_height()):
            ctone = [0, 0, 0, 0, 0, 0]
            ccolor = list(image.get_at((i, j)))
            sort_colors = sorted(ccolor[:-1])
            ctone[0] = sort_colors.index(ccolor[0])
            ctone[1] = sort_colors.index(ccolor[1])
            ctone[2] = sort_colors.index(ccolor[2])
            ctone[3] = int(ccolor[0] // (255 / levels))
            ctone[4] = int(ccolor[1] // (255 / levels))
            ctone[5] = int(ccolor[2] // (255 / levels))
            if ctone not in tones and ccolor[3] != 0:
                tones.append(ctone)
                colors.append(ccolor)
    print(tones)
    print(colors)

    for i in range(image.get_width()):
        for j in range(image.get_height()):
            ccolor = list(image.get_at((i, j)))
            if ccolor[3] != 0:
                ctone = [0, 0, 0, 0, 0, 0]
                sort_colors = sorted(ccolor[:-1])
                ctone[0] = sort_colors.index(ccolor[0])
                ctone[1] = sort_colors.index(ccolor[1])
                ctone[2] = sort_colors.index(ccolor[2])
                ctone[3] = int(ccolor[0] // (255 / levels))
                ctone[4] = int(ccolor[1] // (255 / levels))
                ctone[5] = int(ccolor[2] // (255 / levels))
                image.set_at((i, j), colors[tones.index(ctone)])

def filterPAS(image, levels):
    colors = []
    tones = []
    # levels = 5
    for i in range(image.get_width()):
        for j in range(image.get_height()):
            ctone = [0, 0, 0]
            ccolor = list(image.get_at((i, j)))
            ctone[0] = int(ccolor[0] // (255 / levels))
            ctone[1] = int(ccolor[1] // (255 / levels))
            ctone[2] = int(ccolor[2] // (255 / levels))
            if ctone not in tones and ccolor[3] != 0:
                tones.append(ctone)
                colors.append(ccolor)
    # print(tones)
    # print(colors)

    for i in range(image.get_width()):
        for j in range(image.get_height()):
            ccolor = list(image.get_at((i, j)))
            if ccolor[3] != 0:
                ctone = [0, 0, 0]
                ctone[0] = int(ccolor[0] // (255 / levels))
                ctone[1] = int(ccolor[1] // (255 / levels))
                ctone[2] = int(ccolor[2] // (255 / levels))
                image.set_at((i, j), colors[tones.index(ctone)])

    return len(colors)


def filterColors(image, canvas, r, g, b, a):
    rect = pygame.Surface((image.get_width(), image.get_height()))
    rect.set_alpha(a)
    rect.fill((r, g, b))
    canvas.blit(rect, (0, 0))