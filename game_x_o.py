#!user/bin/env python3
# -*- coding: iso-8859-15 -*-
"""
game_x_o
desenvolvido por: 948alfa
programa sob licença GNU v3
"""

from curses import initscr, wrapper
from random import randint

def boas_vindas(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 1, 'Bem vindo ao jogo X_O.')
    stdscr.addstr(2, 1, 'Pressione q para sair e h para obter ajuda.')
    stdscr.addstr(16, 1, 'KUKINA_tech')
    stdscr.addstr(17, 1, 'by Manuel Andre')
    stdscr.refresh()


def reiniciar_tela(stdscr, limpar=True):
    if limpar is True:
        stdscr.clear()
    stdscr.border()
    boas_vindas(stdscr)
    stdscr.refresh()

def draw_tabuleiro(stdscr, posicoes, X_center):
    stdscr.clear()
    reiniciar_tela(stdscr, limpar=False)

    stdscr.addstr(10, X_center - 3, '------')
    stdscr.addstr(12, X_center - 3, '------')
    i = 9
    for linha in posicoes:
        tela = '%s|%s|%s' % tuple(linha)
        stdscr.addstr(i, X_center - 3, tela)
        i += 2

def limites(pos_x, pos_y):
    if pos_x > 2:
        pos_x = 0
    if pos_x < 0:
        pos_x = 2

    if pos_y > 2:
        pos_y = 0
    if pos_y < 0:
        pos_y = 2
    return (pos_x, pos_y)

def espaco_do_tabuleiro(pos_x, pos_y, entrada):
    if entrada == 'a':
        pos_x, pos_y = limites(pos_x - 1, pos_y)
    if entrada == 'd':
        pos_x, pos_y = limites(pos_x + 1, pos_y)
    if entrada == 'w':
        pos_x, pos_y = limites(pos_x, pos_y - 1)
    if entrada == 's':
        pos_x, pos_y = limites(pos_x - 1, pos_y + 1)
    else:
        pass
    return (pos_x, pos_y)
    
def cursor(stdscr, pos_x, pos_y, X_center):
    cursor_y = 9
    cursor_x = X_center - 3
    if pos_x == 1:
        cursor_x += 2
    if pos_x == 2:
        cursor_x += 4
    if pos_y == 1:
        cursor_y += 2
    if pos_y == 2:
        cursor_y += 4
    stdscr.move(cursor_x, cursor_y)


def ajuda(stdscr):
        stdscr.clear()
        stdscr.addstr(1, 1, 'Pressione Q para sair e H para ajuda')
        stdscr.addstr(2, 1, 'Para mudar a posicao, use as teclas A, D, S, W')
        stdscr.addstr(3, 1, 'Para definir uma posicao, use a tecla L')
        stdscr.addstr(4, 1, 'Para reiniciar a partida, digite Y')
        stdscr.addstr(5, 1, 'Pressione ESPAÇO para sair desta tela')
        stdscr.refresh()




def main(stdscr):
    
    reiniciar_tela(stdscr)
    width = stdscr.getmaxyx()[1]
    X_center = (width - 1) // 2
    posicoes = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    pos_x, pos_y = 0, 0

    while (True):
        tecla = stdscr.getkey()
        if tecla == 'q':
            break
        if (tecla in ['a', 'd', 'w', 's']):
            pos_x, pos_y = espaco_do_tabuleiro(pos_x, pos_x, tecla)
        if tecla == 'h':
            ajuda(stdscr)
        else:
            draw_tabuleiro(stdscr, posicoes, X_center)
            cursor(stdscr, pos_x, pos_y, X_center)

        #pass


if __name__ == "__main__":
    initscr()
    wrapper(main)
