# def fgm(x,z,y):
#     if z == '+':
#         return x + y
#     elif z == '-':
#         return x - y
#     elif z == '*':
#         return x * y
#     elif z == '/':
#             if y==0:
#                 print('Так нельзя')
#             else:
#                 return x / y
#     else:
#         print("Неверный оператор")
# try:
#     value = fgm(int(input("x=")),input("z="),int(input("y=")))
#     print(value)
# except(ValueError):
#     print('нет такого числа')
                   #def login():
   # login = input('y=')
    #login1 = 'x'
    #if login1 == login:
    #    print('good')
   # else:
 #       print('not')
##login()
while True:
    x = float(input('Введите первое число '))
    y = float(input('Введите второе число '))
    z = input('Введите знак')
    if z =='+':
        print(x+y)
    elif z == "-":
        print(x-y)
    elif z == "*":
        print(x*y)
    elif z == "/":
        if x == 0:
            print('на ноль делить нельзя')
        print(x/y)

    else:
        print("ТАКОГО ЗНАКА НЕТ")
    otvet = input('Желаете продолжить? ').lower()
    if otvet == 'нет':
        break
    
#
