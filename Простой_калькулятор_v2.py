# Простой калькулятор v2
#
from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init()
print(Fore.BLACK)
print(Back.GREEN)
what = input("Что вы хотите сделать? (+,-):")
print(Back.MAGENTA)
a = float(input ("Введите первое число:"))
b = float(input ("Введите второе число:"))
if what == "+":
    c = a + b
    print(Back.CYAN)
    print("Результат:" + str(c))
elif what == "-":
    c = a - b
    print(Back.CYAN)
    print("Результат:" + str(c))
else:
    print(Back.CYAN)
    print("Выбрана не верная операция")
    input()

