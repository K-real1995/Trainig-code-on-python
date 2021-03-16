#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#training with lists


my_family = ["son", "daughter" "father", "grand father", "mother", "grand mother"]



my_family_height = [["son",158],["daughter",149],["father",186],["grand father",185], ["mother",175],
                ["grand mother", 165]]



print(my_family_height[3][1], "см")

height_son = my_family_height[0][1]
height_daughter=my_family_height[1][1]
height_father=my_family_height[2][1]
height_grand_father=my_family_height[3][1]
height_mother=my_family_height[4][1]
height_grand_mother=my_family_height[5][1]
common_family_height=height_grand_father+height_father+height_daughter+height_grand_mother+\
                     height_mother+height_son
print("Общий рост моей семьи -",common_family_height,"см")
