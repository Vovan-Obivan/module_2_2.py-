# module_2_2.py
first = int(input('ВВедите ваше число: '))
second = int(input('ВВедите ваше число: '))
third =int(input('ВВедите ваше число: '))
a=first
b=second
c=third
print(a,b,c)
if a==b and a==c:
    input(3)
elif a==b or b==c or c==a:
    input(2)
else:
    input(0)