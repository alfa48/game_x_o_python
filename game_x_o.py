#!user/bin/env python3
# -*- coding: iso-8859-15 -*-
"""
game_x_o
desenvolvido por: 948alfa
programa sob licença GNU v3
"""

from curses import initscr, wrapper
from random import randint

def welcome_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 1, 'Bem vindo ao jogo X_O.')
    stdscr.addstr(2, 1, 'Pressione q para sair e h para obter ajuda.')
    stdscr.addstr(3, 1, 'Pressione r para reiniciar.')
    stdscr.addstr(16, 1, 'Create by Manuel Andre')
    stdscr.refresh()

def init_screen(stdscr, clean=True):
    if clean is True:
        stdscr.clear()
    stdscr.border()
    welcome_screen(stdscr)
    stdscr.refresh()

def draw_table(stdscr, posicoes, X_center):
    stdscr.clear()
    init_screen(stdscr, clean=False)

    stdscr.addstr(10, X_center - 3, '------')
    stdscr.addstr(12, X_center - 3, '------')
    i = 9
    for line in posicoes:
        screen = '%s|%s|%s' % tuple(line)
        stdscr.addstr(i, X_center - 3, screen)
        i += 2

def limites(pos_x, pos_y):
    if pos_x > 2:
        pos_x = 0
    elif pos_x < 0:
        pos_x = 2

    elif pos_y > 2:
        pos_y = 0
    elif pos_y < 0:
        pos_y = 2
    return (pos_x, pos_y)

def space_of_table(pos_x, pos_y, key):
    if key == 'a':
        pos_x, pos_y = limites(pos_x - 1, pos_y)
    elif key == 'd':
        pos_x, pos_y = limites(pos_x + 1, pos_y)
    elif key == 'w':
        pos_x, pos_y = limites(pos_x, pos_y - 1)
    elif key == 's':
        pos_x, pos_y = limites(pos_x, pos_y + 1)
    return (pos_x, pos_y)

def cursor(stdscr, pos_x, pos_y, x_center):
    cursor_y = 9
    cursor_x = x_center - 3
    if pos_x == 1:
        cursor_x += 2
    if pos_x == 2:
        cursor_x += 4
    if pos_y == 1:
        cursor_y += 2
    if pos_y == 2:
        cursor_y += 4
    #print("X: {0} Y: {1}".format(cursor_x, cursor_y))
    stdscr.move(cursor_y, cursor_x)


def help(stdscr):
        stdscr.clear()
        stdscr.addstr(1, 1, 'Para mudar a posicao, use as teclas A, D, S, W')
        stdscr.addstr(2, 1, 'Para definir uma posicao, use a tecla L')
        stdscr.addstr(3, 1, 'Para reiniciar a partida, digite Y')
        stdscr.addstr(4, 1, 'Pressione ESPAÇO para sair desta tela')
        stdscr.refresh()

def debug(stdscr, pos_x, pos_y):
        stdscr.addstr(17, 1, f"pos_x: {pos_x}, pos_y: {pos_y}")

def gamer(pos_x, pos_y, positions):
    if positions[pos_y][pos_x] == ' ':
        positions[pos_y][pos_x] = 'X'
        return True, positions
    return False, positions


def robot(positions):
    empty = []
    for i in range(0, 3):
        for j in range(0, 3):
            if positions[j][i] == " ":
                empty.append([j, i])
    n_choese = len(empty)
    if n_choese != 0:
        j, i = empty[randint(0, n_choese - 1)]
        positions[j][i] = "O"
    return (positions)

def is_table_full (positions):
    for row  in positions:
        if ' ' in row:
            return False
    return True

def won(positions, gamer):
    # linhas
    for row in positions:
        if all(cell == gamer for cell in row):
            return gamer, True
    # colunas
    for col in range(3):
        if all(row[col] == gamer for row in positions):
            return gamer, True
    # diagonal principal
    if all(positions[i][i] == gamer for i in range(3)):
        return gamer, True
    # diagonal secundária
    if all(positions[i][2 - i] == gamer for i in range(3)):
        return gamer, True
    return gamer, False

def game_over(stdscr, won):
        if (won == 'Empate'):
            stdscr.addstr(6, 1, '..%s ...' % won)
        else:
            stdscr.addstr(6, 1, '%s venceu...' % won)
        stdscr.refresh()

def reboot(stdscr):
    positions = [
                    [' ', ' ', ' '],
                    [' ', ' ', ' '],
                    [' ', ' ', ' ']
                ]
    pos_x, pos_y = 0, 0
    winner, won_o, won_x = ' ', False, False
    stdscr.clear()
    return positions, pos_x, pos_y, winner, won_o, won_x

def main(stdscr):

    width = stdscr.getmaxyx()[1]
    x_center = (width - 1) // 2
    positions, pos_x, pos_y, winner, won_o, won_x = reboot(stdscr)
    init_screen(stdscr)

    while (True):
        key = stdscr.getkey()
        if key == 'r':
            positions, pos_x, pos_y, winner, won_o, won_x = reboot(stdscr)
            pass
        if key == ('q' or is_table_full(positions)):
            break
        if (key in ['a', 'd', 'w', 's']):
            pos_x, pos_y = space_of_table(pos_x, pos_y, key)
        if (key == '\n'):
            played, positions = gamer (pos_x, pos_y, positions)
            if played:
                positions = robot(positions)
            winner, won_x = won(positions, 'X')
            if won_x == False:
                winner, won_o = won(positions, 'O')
        if key == 'h':
            help(stdscr)
        else:
            draw_table(stdscr, positions, x_center)
            cursor(stdscr, pos_x, pos_y, x_center)
            if won_x or won_o:
                game_over(stdscr, winner)
            if is_table_full(positions):
                game_over(stdscr, "Empate")
        #   stdscr.move(pos_x, pos_y)
        #pos_x, pos_y = 2, 2;
            #debug(stdscr, pos_x, str(pos_y))


if __name__ == "__main__":
    initscr()
    wrapper(main)