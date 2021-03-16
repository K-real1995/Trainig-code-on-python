#!/usr/bin/env python3
# -*- coding: utf-8 -*-


violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

#Training with lists № 3

common_time_songs=violator_songs_list[3][1]+violator_songs_list[5][1]+\
                  violator_songs_list[-1][1]
print("Три песни звучат примерно", round(common_time_songs), "минут")

#training with dictionaries

violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}


sweet_perfection=violator_songs_dict["Sweetest Perfection"]
police_of_truth=violator_songs_dict["Policy of Truth"]
blue_dress=violator_songs_dict["Blue Dress"]
common_time_songs_in_dict=sweet_perfection+police_of_truth+blue_dress
print("А другие три песни звучат примерно", round(common_time_songs_in_dict), "минут")
