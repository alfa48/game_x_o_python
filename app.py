# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alfa-97 <948manuel@gmail.com>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/21 20:49:32 by alfa-97           #+#    #+#              #
#    Updated: 2024/11/21 21:14:06 by alfa-97          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!user/bin/env python3
# -*- coding: iso-8859-15 -*-
"""
game_x_o
desenvolvido por: 948alfa
programa sob licença GNU v3

"""
from random import randint

print('game init ...');

while(1):
    num = int(input('Escolhe um numero entre 1 e 10:'))
    dado = randint(1, 10)
    if num == dado:
        print('parabens, saiu o seu número')
    else:
        print('lamento, nao foi desta')
        print('o número sorteado foi {0}'.format(dado))
    continuar = input('Digite S para continuar e N para sair:');
    if continuar != 'S' or continuar != 's':
        break
    else :
        continue

