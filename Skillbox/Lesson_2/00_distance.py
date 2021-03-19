#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# TODO Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2
from pprint import pprint
from math import sqrt
moscow= sites["Moscow"]
london=sites["London"]
paris=sites["Paris"]
moscow_london_x=moscow[0]-london[0]
moscow_paris_x=moscow[0]-paris[0]
london_paris_x=london[0]-paris[0]
moscow_london_y=moscow[1]-london[1]
moscow_paris_y=moscow[1]-paris[1]
london_paris_y=london[1]-paris[1]
distances = {"distance_moscow_london":(sqrt((moscow_london_x)**2+(moscow_london_y)**2)),
             "distance_moscow_paris":(sqrt((moscow_paris_x)**2+(moscow_paris_y)**2)),
             "distance_london_paris":(sqrt((london_paris_x)**2+(london_paris_y)**2)),}

pprint(distances)




