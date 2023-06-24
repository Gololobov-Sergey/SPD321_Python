

# not
# ==  !=  >  <  >=  <= # !_=
# and or ^(xor)

'''print(5 == 4)
print(5 != 4)
print(5 > 5)
print(5 < 4)
print(5 >= 5)
print(5 <= 4)
print(not 5 < 4)'''

'''print(not 4 != 4 and 4 == 0 or 4 == 4)

# or || + 
print(True or True)
print(False or True)
print(True or False)
print(False or False)
print()


# and && * 
print(True and True)
print(False and True)
print(True and False)
print(False and False)
print()


# xor ^ 
print(True ^ True)
print(False ^ True)
print(True ^ False)
print(False ^ False)'''


## Дано целое число A. Проверить истинность высказывания: «Число
## A является положительным».

'''a = int(input("Number A: "))
res = a > 0
print(res)'''



## Дано целое число A. Проверить истинность высказывания: «Число A
## является нечетным».
'''a = int(input("Number A: "))
res = a % 2 == 1
print(res)'''



## Даны два целых числа: A, B. Проверить истинность высказывания:
## «Каждое из чисел A и B нечетное».
'''a = int(input("Number A: "))
b = int(input("Number B: "))
res = a % 2 == 1 and b % 2 == 1
print(res)'''


## Даны два целых числа: A, B. Проверить истинность высказывания:
## «Числа A и B имеют одинаковую четность».
'''a = int(input("Number A: "))
b = int(input("Number B: "))
res = a % 2 == b % 2
print(res)'''


'''
a = int(input("Number A: "))
if a > 0:
    print("Positive")
elif a < 0:
    print("Negstive")
else:
    print("Zero")
'''


'''
a = int(input("Number A: "))
b = int(input("Number B: "))
if b != 0:
    print (a / b)
else:
    print ("impossible")
'''


'''
a = int(input("Number A: "))
b = int(input("Number B: "))
c = int(input("Number C: "))
d = int(input("Number D: "))
res = 0

if a % 2 == 0:
    res += 1

if b % 2 == 0:
    res += 1

if c % 2 == 0:
    res += 1

if d % 2 == 0:
    res += 1

print(res)
'''

## Даны две переменные целого типа: A и B. Если их значения не равны, то
## присвоить каждой переменной большее из этих значений, а если равны, то
## присвоить переменным нулевые значения. Вывести новые значения пере-
## менных A и B.
'''
a = int(input("Number A: "))
b = int(input("Number B: "))

if a != b:

    if a > b:
        b = a
    else:
        a = b
else:
    a = b = 0

print(a, b)
'''