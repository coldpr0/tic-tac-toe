import pygame
import checking_stuff
import sys
import math


pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('tic tac toe')
background_color = (200, 230, 222)
bgh = (200, 255, 222)
line_color = (83, 104, 138)
line_hovered = (150, 150, 255)
tile_placement = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]
game_running = True
top_left_X = False
top_mid_X = False
top_right_X = False
mid_left_X = False
center_X = False
mid_right_X = False
bot_left_X = False
bot_mid_X = False
bot_right_X = False
top_left_Y = False
top_mid_Y = False
top_right_Y = False
mid_left_Y = False
center_Y = False
mid_right_Y = False
bot_left_Y = False
bot_mid_Y = False
bot_right_Y = False
player_turn = 'X'
ending_screen = False


def new_game():
    global tile_placement, game_running, top_left_X, top_mid_X, top_right_X, mid_left_X, center_X, mid_right_X\
        , bot_left_X, bot_mid_X, bot_right_X, top_left_Y, top_mid_Y, top_right_Y, mid_left_Y, center_Y, mid_right_Y\
        , bot_left_Y, bot_mid_Y, bot_right_Y, player_turn, ending_screen
    tile_placement = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    game_running = True
    top_left_X = False
    top_mid_X = False
    top_right_X = False
    mid_left_X = False
    center_X = False
    mid_right_X = False
    bot_left_X = False
    bot_mid_X = False
    bot_right_X = False
    top_left_Y = False
    top_mid_Y = False
    top_right_Y = False
    mid_left_Y = False
    center_Y = False
    mid_right_Y = False
    bot_left_Y = False
    bot_mid_Y = False
    bot_right_Y = False
    player_turn = 'X'
    ending_screen = False
X_wins = pygame.image.load('/Users/gabrielpasulka/PycharmProjects/pygamepractice/tic_tac_toe/images/X_wins.png')
O_wins = pygame.image.load('/Users/gabrielpasulka/PycharmProjects/pygamepractice/tic_tac_toe/images/O_wins.png')
tie = pygame.image.load('/Users/gabrielpasulka/PycharmProjects/pygamepractice/tic_tac_toe/images/Tie.png')
play_again = pygame.image.load('/Users/gabrielpasulka/PycharmProjects/pygamepractice/tic_tac_toe/images/play_again.png')


def draw_lines():
    pygame.draw.line(screen, line_color, ((1 / 3) * screen_width, 0), ((1 / 3) * screen_width, screen_height), 5)
    pygame.draw.line(screen, line_color, ((1 / 3) * screen_width, 0), ((1 / 3) * screen_width, screen_height), 5)
    pygame.draw.line(screen, line_color, ((2 / 3) * screen_width, 0), ((2 / 3) * screen_width, screen_height), 5)
    pygame.draw.line(screen, line_color, (0, (1 / 3) * screen_height), (screen_width, (1 / 3) * screen_height), 5)
    pygame.draw.line(screen, line_color, (0, (2 / 3) * screen_height), (screen_width, (2 / 3) * screen_height), 5)
    pygame.draw.line(screen, line_color, (0, (2 / 3) * screen_height), (screen_width, (2 / 3) * screen_height), 5)


while game_running:
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_turn == 'X':
                if 0 + math.floor(screen_width * 1 / 3) > mouse[0] and math.floor(screen_height * 1 / 3) > mouse[1] and top_left_Y is False and top_left_X is False:
                    top_left_X = True
                    tile_placement[0][0] = 1
                    player_turn = 'O'
                elif 0 + math.floor(2 / 3 * screen_width) > mouse[0] > math.floor(screen_width * 1 / 3) and math.floor(
                        1 / 3 * screen_height) > mouse[1] > 0 and top_mid_Y is False and top_mid_X is False:
                    top_mid_X = True
                    tile_placement[0][1] = 1
                    player_turn = 'O'
                elif math.floor(2 / 3 * screen_width) + math.floor(screen_width * 1 / 3) > mouse[0] > math.floor(
                        screen_width * 2 / 3) and math.floor(1 / 3 * screen_height) > mouse[1] > 0 and top_right_Y is False and top_right_X is False:
                    top_right_X = True
                    tile_placement[0][2] = 1
                    player_turn = 'O'
                elif 0 + math.floor(screen_width * 1 / 3) > mouse[0] > 0 and math.floor(
                        screen_height * 2 / 3) > mouse[1] > math.floor(screen_height * 1 / 3) and mid_left_X is False and mid_left_Y is False:
                    mid_left_X = True
                    tile_placement[1][0] = 1
                    player_turn = 'O'
                elif math.floor(2 / 3 * screen_width) > mouse[0] > math.floor(1 / 3 * screen_width) and math.floor(
                        2 / 3 * screen_height) > mouse[1] > math.floor(1 / 3 * screen_height) and center_X is False and center_Y is False:
                    center_X = True
                    tile_placement[1][1] = 1
                    player_turn = 'O'
                elif math.floor(2 / 3 * screen_width) + math.floor(screen_width * 1 / 3) > mouse[0] > math.floor(
                        2 / 3 * screen_width) and math.floor(2 / 3 * screen_height) > mouse[1] > math.floor(
                        1 / 3 * screen_height) and mid_right_X is False and mid_right_Y is False:
                    mid_right_X = True
                    tile_placement[1][2] = 1
                    player_turn = 'O'
                elif math.floor(1 / 3 * screen_width) > mouse[0] > 0 and screen_height > mouse[1] > math.floor(
                        2 / 3 * screen_height) and bot_left_Y is False and bot_left_X is False:
                    bot_left_X = True
                    tile_placement[2][0] = 1
                    player_turn = 'O'
                elif math.floor(math.floor(2 / 3 * screen_width)) > mouse[0] > math.floor(
                        1 / 3 * screen_width) and screen_height > mouse[1] > math.floor(2 / 3 * screen_height)\
                        and bot_mid_X is False and bot_mid_Y is False:
                    bot_mid_X = True
                    tile_placement[2][1] = 1
                    player_turn = 'O'
                elif math.floor(2 / 3 * screen_width) + math.floor(screen_width * 1 / 3) > mouse[0] > math.floor(
                        2 / 3 * screen_width) and screen_height > mouse[1] > math.floor(screen_height * 2 / 3)\
                        and bot_right_X is False and bot_right_Y is False:
                    bot_right_X = True
                    tile_placement[2][2] = 1
                    player_turn = 'O'
            elif 470 > mouse[1] > 420 and math.floor(1 / 3 * screen_width) + 100 > mouse[0] \
                    > math.floor(1 / 3 * screen_width) and ending_screen is True:
                new_game()

            if player_turn == 'O':
                if 0 + math.floor(screen_width * 1 / 3) > mouse[0] and math.floor(screen_height * 1 / 3) > mouse[1] and top_left_X is False and top_left_Y is False:
                    top_left_Y = True
                    tile_placement[0][0] = 2
                    player_turn = 'X'
                elif 0 + math.floor(2 / 3 * screen_width) > mouse[0] > math.floor(screen_width * 1 / 3) and math.floor(
                        1 / 3 * screen_height) > mouse[1] > 0 and top_mid_X is False and top_mid_Y is False:
                    top_mid_Y = True
                    tile_placement[0][1] = 2
                    player_turn = 'X'
                elif math.floor(2 / 3 * screen_width) + math.floor(screen_width * 1 / 3) > mouse[0] > math.floor(screen_width * 2 / 3) and math.floor(
                    1 / 3 * screen_height) > mouse[1] > 0 and top_right_X is False and top_right_Y is False:
                    top_right_Y = True
                    tile_placement[0][2] = 2
                    player_turn = 'X'
                elif 0 + math.floor(screen_width * 1 / 3) > mouse[0] > 0 and math.floor(screen_height * 2 / 3)\
                        > mouse[1] > math.floor(screen_height * 1 / 3) and mid_left_X is False and mid_left_Y is False:
                    mid_left_Y = True
                    tile_placement[1][0] = 2
                    player_turn = 'X'
                elif math.floor(2 / 3 * screen_width) > mouse[0] > math.floor(1 / 3 * screen_width) and math.floor(2 / 3 * screen_height) > mouse[1] > math.floor(
                    1 / 3 * screen_height) and center_X is False and center_Y is False:
                    center_Y = True
                    tile_placement[1][1] = 2
                    player_turn = 'X'
                elif math.floor(2 / 3 * screen_width) + math.floor(screen_width * 1 / 3) > mouse[0] > math.floor(2 / 3 * screen_width) and math.floor(
                    2 / 3 * screen_height) > mouse[1] > math.floor(1 / 3 * screen_height) and mid_right_X is False and mid_right_Y is False:
                    mid_right_Y = True
                    tile_placement[1][2] = 2
                    player_turn = 'X'
                elif math.floor(1 / 3 * screen_width) > mouse[0] > 0 and screen_height > mouse[1] > math.floor(
                        2 / 3 * screen_height) and bot_left_Y is False and bot_left_X is False:
                    bot_left_Y = True
                    tile_placement[2][0] = 2
                    player_turn = 'X'
                elif math.floor(math.floor(2 / 3 * screen_width)) > mouse[0] > math.floor(1 / 3 * screen_width) and screen_height > mouse[1] > math.floor(
                    2 / 3 * screen_height) and bot_mid_X is False and bot_mid_Y is False:
                    bot_mid_Y = True
                    tile_placement[2][1] = 2
                    player_turn = 'X'
                elif math.floor(2 / 3 * screen_width) + math.floor(screen_width * 1 / 3) > mouse[0] > math.floor(2 / 3 * screen_width) and screen_height > mouse[
                    1] > math.floor(screen_height * 2 / 3) and bot_right_X is False and bot_right_Y is False:
                    bot_right_Y = True
                    tile_placement[2][2] = 2
                    player_turn = 'X'
            elif 470 > mouse[1] > 420 and math.floor(1 / 3 * screen_width) + 100 > mouse[0] \
                    > math.floor(1 / 3 * screen_width) and ending_screen is True:
                new_game()
    screen.fill(background_color)
    checking_stuff.check_hover_X(screen_width, mouse, screen_height, line_hovered, screen, bgh, background_color, top_left_X
                                 , top_mid_X, top_right_X, line_color, mid_left_X, center_X, mid_right_X, bot_right_X, bot_mid_X
                                 , bot_left_X, player_turn, top_left_Y, top_mid_Y, top_right_Y, mid_left_Y
                                 , center_Y, mid_right_Y, bot_left_Y, bot_mid_Y, bot_right_Y)
    checking_stuff.check_squares_X(screen_width, mouse, screen_height, line_hovered, screen, bgh, background_color
                                   , top_left_X, top_mid_X, top_right_X, line_color, mid_left_X, center_X, mid_right_X, bot_left_X
                                   , bot_mid_X, bot_right_X, player_turn, top_left_Y, top_mid_Y, top_right_Y, mid_left_Y
                                   , center_Y, mid_right_Y, bot_left_Y, bot_mid_Y, bot_right_Y)
    checking_stuff.check_squares_Y(screen, line_color, screen_width, screen_height, top_left_Y, top_mid_Y, top_right_Y
                                   , mid_left_Y, center_Y, mid_right_Y, bot_left_Y, bot_mid_Y, bot_right_Y, bot_left_X)
    checking_stuff.check_win(tile_placement)
    draw_lines()
    if checking_stuff.check_win(tile_placement) == 'X' or checking_stuff.check_win(tile_placement) == 'O'\
            or checking_stuff.check_win(tile_placement) == 'tie':
        pygame.draw.rect(screen, (211, 211, 211), (200, 300, 400, 200))
        ending_screen = True
    if ending_screen:
        pygame.draw.rect(screen, (102, 113, 115), (math.floor(2 / 3 * screen_width) - 100, 420, 100, 50)) #  right rect
        pygame.draw.rect(screen, (61, 102, 110), (math.floor(1 / 3 * screen_width), 420, 100, 50)) #  left rect
        screen.blit(play_again, (math.floor(1 / 3 * screen_width), 420))
        if 470 > mouse[1] > 420 and math.floor(1 / 3 * screen_width) + 100 > mouse[0] > math.floor(1 / 3 * screen_width): #  left rect
            red_rect = pygame.draw.rect(screen, (52, 87, 94), (math.floor(1 / 3 * screen_width), 420, 100, 50))
            screen.blit(play_again, (math.floor(1 / 3 * screen_width), 420))
        if 470 > mouse[1] > 420 and math.floor(2 / 3 * screen_width) > mouse[0] > math.floor(2 / 3 * screen_width) - 100: #  right rect
            blue_rect = pygame.draw.rect(screen, (92, 103, 105), (math.floor(2 / 3 * screen_width) - 100, 420, 100, 50))
        if checking_stuff.check_win(tile_placement) == 'X':
            screen.blit(X_wins, (300, 310))
        elif checking_stuff.check_win(tile_placement) == 'O':
            screen.blit(O_wins, (300, 310))
        elif checking_stuff.check_win(tile_placement) == 'tie':
            screen.blit(tie, (300, 310))
    p   ygame.display.flip()
