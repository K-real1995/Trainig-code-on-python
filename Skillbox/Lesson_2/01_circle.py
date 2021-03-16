#!/usr/bin/env python3
# -*- coding: utf-8 -*-

radius = 42

# сircle area
s=round(3.1415926*radius**2,4)
print(s)
# does the point enter the circle
point = (23, 34)

from math import sqrt
point_in=sqrt(point[0]**2+point[1]**2)
round(point_in)
print(point_in <= radius)

# For point № 2
point_2 = (30, 30)

point_in_2=sqrt(point_2[0]**2+point[1]**2)
round(point_in_2)
print(point_in_2 <= radius)



