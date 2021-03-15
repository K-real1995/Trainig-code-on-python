age = 18
street = 'Ленина'
first_name = 'Олег'
house = 58
city_r = 'Москве'
d = {"name":first_name , "age":age, "city":city_r, "street":street, "house":house}
hello = 'Привет! Меня зовут %(name)s, мне %(age)d лет. Я живу в %(city)s, на улице %(street)s, дом %(house)d.' % d
print(hello)
