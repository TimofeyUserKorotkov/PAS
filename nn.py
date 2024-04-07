import pygame
import random
pygame.init()

e = 2.718281828459045
la = 0.1

deltas = list()
signs_maps = list()
signs_map = list()
new_weights = list()
pr = list()

back_list = list()

kernels_signs = []
weights = []
matrix = [[-1, -1], [0, -1], [1, -1], 
          [-1, 0], [0, 0], [1, 0], 
          [-1, 1], [0, 1], [1, 1]]

random.seed(1)
for i in range(5):
    # 196 65536
    weights.append([round(random.uniform(-1, 1), 4) for j in range(196)])
for i in range(5):
    kernels_signs.append([round(random.uniform(-1, 1), 4) for j in range(9)])

# kernels_signs.append([-1, 0, 1,
#                       -2, 0, 2,
#                       -1, 0, 1])

def sigmoid(x):
    return 1 / (1 + e**(-x))

def ReLU(x):
    return 0 if x < 0 else x
    
def maxPooling(convs):
    new_convs = []
    new_conv = []
    for i in range(len(convs)):
        cconv = convs[i]
        new_conv.clear()
        for j in range(0, len(cconv), 4):
            new_conv.append(max(cconv[j], cconv[j + 1], cconv[j + 2], cconv[j + 3]))
        new_convs.append(new_conv)
    return new_convs
    
def check_pixel(image, x, y):
    color = image.get_at((x, y))
    if color[3] != 0:
        return 1 - color[0] / 255
    else:
        return 0
    
def check_pixel2(image, x, y):
    color = image.get_at((x, y))
    # if color[3] != 0:
    #     return 1 - color[0] / 255
    # else:
    #     return 0
    return 255 - color[0]

def prediction(image):
    signs_maps.clear()
    summ = 0
    summa = 0
    for s in range(len(kernels_signs)):
        signs_map.clear()
        for i in range(image.get_width()):
            for j in range(image.get_height()):
                # 29 513
                if i > 0 and j > 0 and i < 29 and j < 29:
                    for k in range(9):
                        summ += kernels_signs[s][k] * check_pixel(image, i + matrix[k][0], j + matrix[k][1])
                    signs_map.append(ReLU(summ))
                    summ = 0
        signs_maps.append(signs_map)
        loc = maxPooling(signs_maps)
        signs_maps.clear()
        signs_maps.extend(loc)
    for i in range(len(signs_maps)):
        for j in range(len(signs_maps[0])):
            summa += signs_maps[i][j] * weights[i][j]
    return sigmoid(summa)

def train(image, correct):
    w = image.get_width()
    deltas.clear()
    for iteration in range(10):
        predict = prediction(image)
        error = predict - correct
        delta = error * predict * (1 - predict)
        for i in range(len(signs_maps)):
            for j in range(len(signs_maps[0])):
                weights[i][j] -= signs_maps[i][j] * delta * la
            new_weights.clear()
            pr.clear()
            for weis in range(len(weights)):
                new_weights.append([weights[weis][weig] for weig in range(len(weights[0])) for w in range(4)])
            for si in range(1, w + 1):
                for sj in range(1, image.get_height() + 1):
                    for k in range(9):
                        deriv = 0 if signs_maps[i][k] < 0 else 1
                        # deriv = signs_maps[i][k] * (1 - signs_maps[i][k])
                        # if (si - 1) * (sj - 1) not in pr:
                        if si > 1 and sj > 1 and si < 30 and sj < 30:
                            try:
                                kernels_signs[i][k] -= check_pixel(image, si - 1 + matrix[k][0], sj - 1 + matrix[k][1]) * delta * new_weights[i][((sj - 2) * (w - 2) + si - 1) - 1] * deriv * la
                            except:
                                print((sj - 2) * (w - 2) + si - 1, "===> l:", len(new_weights[i]), f"r{sj}x{si}")
                            # pr.append((si - 1) * (sj - 1))

def drawIm(image, correct):
    fimage = image
    summ = 0
    print(kernels_signs[4])
    for sign in range(len(signs_maps) - 4):
        for i in range(1, image.get_width() - 1):
            for j in range(1, image.get_height() - 1):
                for k in range(9):
                    summ += (kernels_signs[4][k]) * check_pixel2(image, i + matrix[k][0], j + matrix[k][1])
                    # print(check_pixel2(image, i + matrix[k][0], j + matrix[k][1]))
                # summ = sigmoid(summ)
                # print(summ)
                color = int(summ)
                try:
                    fimage.set_at((i, j), (color, color, color))
                except:
                    if color > 255:
                        fimage.set_at((i, j), (255, 255, 255))
                    else:
                        fimage.set_at((i, j), (0, 0, 0))
                    # print((color, color, color))
                    pass
                summ = 0

    return fimage

def showTest(image):
    w = image.get_width()
    h = image.get_height()
    for i in range(1, w + 1):
        for j in range(1, h + 1):
            if i > 1 and j > 1 and i < 5 and j < 5:
            # print(j * w + w - i, j, "x", i)
                print((j - 1) * w + i, j, "x", i)
            # print(i * h + h - j)
    print(kernels_signs)