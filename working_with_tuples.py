#1. Создать кортеж чисел от 1 до n. Заполнить кортеж числами с клавиатуры и проверить его на упорядоченность
#по возрастанию
#2. Введите список с клавиатуры до 0. Распечатайте элементы с четными индексами. Пользоваться if нельзя.
#3. Введите список через пробел. Удалите из списка все элементы, находящиеся на нечетных позициях
n=int(input("Введите длину предполагаемого кортежа (не включительно):"))
my_tuple = tuple(i for i in range(1, n))
print(my_tuple)

my_list=[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(my_list[1::2])

l = [int(i) for i in input().split()]
def modify_list(l):
    l[:] = [i // 2 for i in l if i % 2 == 0]
print(modify_list(l))
print(l)