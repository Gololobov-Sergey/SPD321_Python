
'''
while condition:
    oper1
    oper1
    oper1
    oper1
'''

'''
a = 5
while a > 0:
    print(a, end=' ')
    a -= 1
'''

'''
a = int(input("a : "))
b = int(input("b : "))
if a < b:
    while a <= b:
        print(a, end=' ')
        a += 1
else:
    while a >= b:
        print(a, end=' ')
        a -= 1
'''

'''
a = int(input("a : "))
b = int(input("b : "))
k = 0
while a >= b:
    a -= b
    k += 1
print(k)
'''


'''
a = int(input("a : "))
s = 0
while a > 0:    
    r = a % 10
    s += r
    a //= 10
print(s)
'''

'''
a = 0
while True:
    a = int(input("a : "))
    if a > 0 and a < 10:
        break
'''

'''
a = 0
while a <= 20:
    a += 1
    if a % 2 == 1:
        continue
    print(a)
'''

'''
for i in range(5):
    print(i)
'''

'''
n = int(input("Кількість магазинів : "))
s = 0
for m in range(1, n + 1):
    h = int(input(f"Введіть кількість холодильників, яка є в магазині #{m} : "))
    s += h
print(s)
'''

'''
n = abs(int(input("введите количество школ >> ")))
total = 0
for i in range (n):
    am = abs(int(input(f"введите количество учеников в школе #{i+1} >> ")))
    if am > 1000:
        total+=1
print("всего", total, "школ где учатся больше или 1000 учеников")
'''

'''
for i in range(1, 1000):
    f = True
    for j in range(2, i):
        if i % j == 0:
            f = False
            break
    if f:
        print(i, end=", ")
print()
'''

'''
c = 0
for h in range(24):
    for m in range(60):
        h1 = h // 10
        h2 = h % 10
        m1 = m // 10
        m2 = m % 10
        if h1 == m2 and m1 == h2:
            c += 1
            print(f"{h1}{h2}:{m1}{m2}")
print(c)
'''

'''
c = 0
for h in range(24):
    for m in range(60):
        for s in range(60):
            h1 = h // 10
            h2 = h % 10
            m1 = m // 10
            m2 = m % 10
            s1 = s // 10
            s2 = s % 10
            if h1 == s2 and h2 == s1 and m1 == m2:
                c += 1
                print(f"{h1}{h2}:{m1}{m2}:{s1}{s2}")
print(c)
'''

'''
n = int(input("Розрядність чисел : "))
for i in range(10**(n-1), 10**n):
    sum = 0
    num = i
    while num > 0:
        r = num % 10
        sum += r ** n
        num //= 10
    if sum == i:
        print(i, end=' ')
'''