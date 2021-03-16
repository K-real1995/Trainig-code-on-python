#!/usr/bin/env python
# -*- coding: utf-8 -*-

#trainig with list № 2

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

zoo.insert(1,"bear")
print(zoo)


birds = ['rooster', 'ostrich', 'lark', ]

zoo.extend(birds)
print(zoo)

zoo.pop(3)
print(zoo)

lion_place=zoo.index("lion")
print("Лев сидит в клетке №",lion_place+1)
lark_place=zoo.index("lark")
print("Жаворонок сидит в клетке №",lark_place+1)

