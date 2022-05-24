import pygame
import math


def check_hover_X(w, m, h, lh, s, b, bg, tlX, tmX, trX, l, mlX, cX, mrX, brX, bmX, blX, pt, tlY, tmY, trY, mlY, cY
                  , mrY, blY, bmY, brY):
    r = math.floor(w / 6)
    if 0 + math.floor(w * 1 / 3) > m[0] > 0 and math.floor(h * 1 / 3) > m[1] > 0:  # top left
        pygame.draw.rect(s, b, (0, 0, math.floor(1 / 3 * w), math.floor(1 / 3 * h)))
        if tlY is False and pt == 'X':
            pygame.draw.line(s, lh, (0, 0), (math.floor(1 / 3 * w), math.floor(1 / 3 * h)), 4)
            pygame.draw.line(s, lh, (math.floor(1 / 3 * w), 0), (0, math.floor(1 / 3 * h)), 4)
        if tlX is False and pt == 'O':
            pygame.draw.circle(s, lh, (math.floor(w / 6), math.floor(h / 6)), math.floor(w / 6), 4)

    elif 0 + math.floor(2 / 3 * w) > m[0] > math.floor(w * 1 / 3) and math.floor(1 / 3 * h) > m[1] > 0:  # top mid
        pygame.draw.rect(s, b, (math.floor(1 / 3 * w), 0, math.floor(w * 1 / 3), math.floor(h * 1 / 3)))
        if tmY is False and pt == 'X':
            pygame.draw.line(s, lh, (math.floor(1 / 3 * w), 0), (math.floor(2 / 3 * w), math.floor(1 / 3 * h)), 4)
            pygame.draw.line(s, lh, (math.floor(1 / 3 * w), math.floor(1 / 3 * w)), (math.floor(2 / 3 * w), 0), 4)
        if tmX is False and pt == 'O':
            pygame.draw.circle(s, lh, (w / 2, math.floor(h / 6)), r, 4)
    elif math.floor(2 / 3 * w) + math.floor(w * 1 / 3) > m[0] > math.floor(w * 2 / 3) and math.floor(1 / 3 * h) > m[1] > 0:  # top right
        pygame.draw.rect(s, b, (math.floor(2 / 3 * w), 0, math.floor(w * 1 / 3), math.floor(h * 1 / 3)))
        if trY is False and pt == 'X':
            pygame.draw.line(s, lh, (math.floor(2 / 3 * w), 0), (w, math.floor(1 / 3 * h)), 4)
            pygame.draw.line(s, lh, (w, 0), (math.floor(2 / 3 * w), math.floor(1 / 3 * h)), 4)
        if trX is False and pt == 'O':
            pygame.draw.circle(s, lh, (math.floor(w * 5 / 6), math.floor(h / 6)), r, 4)

    elif 0 + math.floor(w * 1 / 3) > m[0] > 0 and math.floor(h * 2 / 3) > m[1] > math.floor(h * 1 / 3):  # mid left
        pygame.draw.rect(s, b, (0, math.floor(h * 1 / 3), math.floor(w * 1 / 3), math.floor(h * 1 / 3)))
        if mlY is False and pt == 'X':
            pygame.draw.line(s, lh, (0, math.floor(h * 1 / 3)), (math.floor(w * 1 / 3), math.floor(h * 2 / 3)), 4)
            pygame.draw.line(s, lh, (0, math.floor(h * 2 / 3)), (math.floor(w * 1 / 3), math.floor(h * 1 / 3)), 4)
        if mlX is False and pt == 'O':
            pygame.draw.circle(s, lh, (math.floor(w / 6), h / 2), r, 4)

    elif math.floor(2 / 3 * w) > m[0] > math.floor(1 / 3 * w) and math.floor(2 / 3 * h) > m[1] > math.floor(1 / 3 * h):  # center
        pygame.draw.rect(s, b, (math.floor(1 / 3 * w), math.floor(1 / 3 * h), math.floor(w * 1 / 3), math.floor(h * 1 / 3)))
        if cY is False and pt == 'X':
            pygame.draw.line(s, lh, (math.floor(1 / 3 * w), math.floor(1 / 3 * h)), (math.floor(2 / 3 * w), math.floor(2 / 3 * h)), 4)
            pygame.draw.line(s, lh, (math.floor(2 / 3 * w), math.floor(1 / 3 * h)), (math.floor(1 / 3 * w), math.floor(2 / 3 * h)), 4)
        if cX is False and pt == 'O':
            pygame.draw.circle(s, lh, (w/2, h/2), r, 4)


    elif math.floor(2 / 3 * w) + math.floor(w * 1 / 3) > m[0] > math.floor(2 / 3 * w) and math.floor(2 / 3 * h) > m[1] > math.floor(1 / 3 * h):  # mid right
        pygame.draw.rect(s, b, (math.floor(2 / 3 * w), math.floor(1 / 3 * h), math.floor(1 / 3 * w), math.floor(1 / 3 * h)))
        if mrY is False and pt == 'X':
            pygame.draw.line(s, lh, (math.floor(2 / 3 * w), math.floor(1 / 3 * h)), (w - 1, math.floor(2 / 3 * h)), 4)
            pygame.draw.line(s, lh, (math.floor(2 / 3 * w), math.floor(2 / 3 * h)), (w - 1, math.floor(1 / 3 * h)), 4)
        if mrX is False and pt == 'O':
            pygame.draw.circle(s, lh, (math.floor(5 / 6 * w), h / 2), r, 4)

    elif math.floor(1 / 3 * w) > m[0] > 0 and h > m[1] > math.floor(2 / 3 * h):  # bottom left
        pygame.draw.rect(s, b, (0, math.floor(2 / 3 * h), math.floor(1 / 3 * w), math.floor(1 / 3 * w)))
        if blY is False and pt == 'X':
            pygame.draw.line(s, lh, (0, h-1), (math.floor(1 / 3 * w), math.floor(2 / 3 * h)), 4)
            pygame.draw.line(s, lh, (0, math.floor(2 / 3 * h)), (math.floor(1 / 3 * w), h - 1), 4)
        if blX is False and pt == 'O':
            pygame.draw.circle(s, lh, (math.floor(w / 6), math.floor(5 / 6 * h)), r, 4)

    elif math.floor(math.floor(2 / 3 * w)) > m[0] > math.floor(1 / 3 * w) and h > m[1] > math.floor(2 / 3 * h):  # bottom middle
        pygame.draw.rect(s, b, (math.floor(1 / 3 * w), math.floor(2 / 3 * h), math.floor(1 / 3 * w), math.floor(1 / 3 * h)))
        if bmY is False and pt == 'X':
            pygame.draw.line(s, lh, (math.floor(1 / 3 * w), math.floor(2 / 3 * h)), (math.floor(2 / 3 * w), h - 1), 4)
            pygame.draw.line(s, lh, (math.floor(1 / 3 * w), h - 1), (math.floor(2 / 3 * w), math.floor(2 / 3 * h)), 4)
        if bmX is False and pt == 'O':
            pygame.draw.circle(s, lh, (w / 2, math.floor(5 / 6 * h)), r, 4)

    elif math.floor(2 / 3 * w) + math.floor(w * 1 / 3) > m[0] > math.floor(2 / 3 * w) and h > m[1] > math.floor(h * 2 / 3):  # bottom right
        pygame.draw.rect(s, b, (math.floor(2 / 3 * w), math.floor(2 / 3 * h), math.floor(1 / 3 * w), math.floor(1 / 3 * h)))
        if brY is False and pt == 'X':
            pygame.draw.line(s, lh, (math.floor(2 / 3 * w), math.floor(2 / 3 * h)), (w - 1, h - 1), 4)
            pygame.draw.line(s, lh, (math.floor(2 / 3 * w), h - 1), (w - 1, math.floor(2 / 3 * h)), 4)
        if brX is False and pt == 'O':
            pygame.draw.circle(s, lh, (math.floor(5 / 6 * w), math.floor(5 / 6 * h)), r, 4)

    else:
        s.fill(bg)


def check_squares_X(w, m, h, lh, s, b, bg, tlX, tmX, trX, l, mlX, cX, mrX, blX, bmX, brX, pt, tlY, tmY, trY, mlY, cY
                    , mrY, blY, bmY, brY):
    if tlX and tlY is False:
        pygame.draw.line(s, l, (0, 0), (math.floor(1 / 3 * w), math.floor(1 / 3 * w)), 10)
        pygame.draw.line(s, l, (math.floor(1 / 3 * w), 0), (0, math.floor(1 / 3 * h)), 10)
    if tmX and tmY is False:
        pygame.draw.line(s, l, (math.floor(1 / 3 * w), 0), (math.floor(2 / 3 * w), math.floor(1 / 3 * h)), 10)
        pygame.draw.line(s, l, (math.floor(1 / 3 * w), math.floor(1 / 3 * w)), (math.floor(2 / 3 * h), 0), 10)
    if trX and trY is False:
        pygame.draw.line(s, l, (math.floor(2 / 3 * w), 0), (w, math.floor(1 / 3 * h)), 10)
        pygame.draw.line(s, l, (w, 0), (math.floor(2 / 3 * w), math.floor(1 / 3 * h)), 10)
    if mlX and mlY is False:
        pygame.draw.line(s, l, (0, math.floor(h * 1 / 3)), (math.floor(w * 1 / 3), math.floor(h * 2 / 3)), 10)
        pygame.draw.line(s, l, (0, math.floor(h * 2 / 3)), (math.floor(w * 1 / 3), math.floor(h * 1 / 3)), 10)
    if cX and cY is False:
        pygame.draw.line(s, l, (math.floor(1 / 3 * w), math.floor(1 / 3 * h)), (math.floor(2 / 3 * w), math.floor(2 / 3 * h)), 10)
        pygame.draw.line(s, l, (math.floor(2 / 3 * w), math.floor(1 / 3 * h)), (math.floor(1 / 3 * w), math.floor(2 / 3 * h)), 10)
    if mrX and mrY is False:
        pygame.draw.line(s, l, (math.floor(2 / 3 * w), math.floor(1 / 3 * h)), (w - 1, math.floor(2 / 3 * h)), 10)
        pygame.draw.line(s, l, (math.floor(2 / 3 * w), math.floor(2 / 3 * h)), (w - 1, math.floor(1 / 3 * h)), 10)
    if blX and blY is False:
        pygame.draw.line(s, l, (0, h - 1), (math.floor(1 / 3 * w), math.floor(2 / 3 * h)), 10)
        pygame.draw.line(s, l, (0, math.floor(2 / 3 * h)), (math.floor(1 / 3 * w), h - 1), 10)
    if bmX and bmY is False:
        pygame.draw.line(s, l, (math.floor(1 / 3 * w), math.floor(2 / 3 * h)), (math.floor(2 / 3 * w), h - 1), 10)
        pygame.draw.line(s, l, (math.floor(1 / 3 * w), h - 1), (math.floor(2 / 3 * w), math.floor(2 / 3 * h)), 10)
    if brX and brY is False:
        pygame.draw.line(s, l, (math.floor(2 / 3 * w), math.floor(2 / 3 * h)), (w - 1, h - 1), 10)
        pygame.draw.line(s, l, (math.floor(2 / 3 * w), h - 1), (w - 1, math.floor(2 / 3 * h)), 10)


def check_squares_Y(s, l, w, h, tlY, tmY, trY, mlY, cY, mrY, blY, bmY, brY, blX):
    if tlY:
        pygame.draw.circle(s, l, (math.floor(w / 6), math.floor(h / 6)), math.floor(w / 6), 10)
    if tmY:
        pygame.draw.circle(s, l, (w / 2, math.floor(h / 6)), math.floor(h / 6), 10)
    if trY:
        pygame.draw.circle(s, l, (math.floor(w * 5 / 6), math.floor(h / 6)), math.floor(h / 6), 10)
    if mlY:
        pygame.draw.circle(s, l, (math.floor(w / 6), h / 2), math.floor(h / 6), 10)
    if cY:
        pygame.draw.circle(s, l, (w / 2, h / 2), math.floor(h / 6), 10)
    if mrY:
        pygame.draw.circle(s, l, (math.floor(5 / 6 * w), h / 2), math.floor(h / 6), 10)
    if blY and blX is False:
        pygame.draw.circle(s, l, (math.floor(w / 6), math.floor(5 / 6 * h)), math.floor(h / 6), 10)
    if bmY:
        pygame.draw.circle(s, l, (w / 2, math.floor(5 / 6 * h)), math.floor(h / 6), 10)
    if brY:
        pygame.draw.circle(s, l, (math.floor(5 / 6 * w), math.floor(5 / 6 * h)), math.floor(h / 6), 10)


def check_win(tile_place):
    column_1 = []
    column_2 = []
    column_3 = []
    diagonal_negative = []
    diagonal_positive = []
    for ele in tile_place:
        column_1.append(ele[0])
        column_2.append(ele[1])
        column_3.append(ele[2])
    diagonal_negative.append(column_1[0])
    diagonal_negative.append(column_2[1])
    diagonal_negative.append(column_3[2])
    diagonal_positive.append(column_1[2])
    diagonal_positive.append(column_2[1])
    diagonal_positive.append(column_3[0])
    for row in range(3):
        if tile_place[row].count(1) == 3:
            return 'X'
        if tile_place[row].count(2) == 3:
            return 'O'

    if diagonal_negative.count(1) == 3 or diagonal_positive.count(1) == 3:
        return 'X'
    if diagonal_negative.count(2) == 3 or diagonal_positive.count(2) == 3:
        return 'O'

    if column_1.count(1) == 3 or column_2.count(1) == 3 or column_3.count(1) == 3:
        return 'X'
    if column_1.count(2) == 3 or column_2.count(2) == 3 or column_3.count(2) == 3:
        return 'O'

    elif tile_place[0].count(0) + tile_place[1].count(0) + tile_place[2].count(0) == 0:
        return 'tie'
