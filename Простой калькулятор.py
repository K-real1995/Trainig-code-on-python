# Простой калькулятор v1
what = input("Что вы хотите сделать? (+,-):")
a = float(input ("Введите первое число:"))
b = float(input ("Введите второе число:"))
if what == "+":
    c = a + b
    print("Результат:" + str(c))
elif what == "-":
    c = a - b
    print("Результат:" + str(c))
else:
    print("Выбрана не верная операция")

