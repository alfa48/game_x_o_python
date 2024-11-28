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




def main(stdscr):

    init_screen(stdscr)
    width = stdscr.getmaxyx()[1]
    x_center = (width) // 2
    position = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    pos_x, pos_y = 0, 0

    while (True):
        key = stdscr.getkey()
        if key == 'q':
            break
        if (key in ['a', 'd', 'w', 's']):
            pos_x, pos_y = space_of_table(pos_x, pos_y, key)
        if key == 'h':
            help(stdscr)
        else:
            draw_table(stdscr, position, x_center)
            #stdscr.move(pos_x, pos_y)
            cursor(stdscr, pos_x, pos_y, x_center)

        #pass


if __name__ == "__main__":
    initscr()
    wrapper(main)