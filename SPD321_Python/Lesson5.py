from codecs import utf_16_be_encode
from encodings import utf_8

'''
for i in "12345":
    print(i)


st = 'hello'
print(type(st))

a = "123.3"
print(float(a))


st1 = 
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
'''
print(st[2])
print(st[-4])

st2 = st + " Python, c++, java, c++"

print(st * 5)

print(len(st2))

print(st2.capitalize())
print(st2.lower())
print(st2.upper())
print(st2.title())
print(st2.swapcase())

print(st2.count("c++", 1, 10))
print(st2.find("c++"))
print(st2.rfind("c+ +"))
#print(st2.index("c+ +"))

print("mama".isalnum())
print("mama".isalpha())
print("1233".isdigit())
print("1233".islower())
print("AAAA".isupper())
print("AAAA".isspace())

print("mama".center(15, '.'), "papa")
print("mama".ljust(15, '.'), "papa")
print("mama".rjust(15, '.'), "papa")



st = "Hello Python"
print(st[2:5])
print(st[2:])
print(st[:8])
print(st[:])
print(st[-8:-3])
print(st[::-1])


st = "Serhiy Gololobov"
i = st.find(' ')
stn = st[i + 1:] + " " + st[0:i]
print(stn)



num = 99.989999
s = "mama"
print(f"Ilkdf {num:^15.3f} kjkler {s:>15}")
print("Ilkdf {0} liewie {1}".format(num, s))


import string

print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.punctuation)

import random


print("".join(random.sample(string.ascii_letters + string.digits, 8)))

import re

pat = re.compile("^\d+$")
while(True):
    sss = input()
    print(bool(pat.search(sss)))
'''



#count = 0

#for i in range(100, 1000):

#   if str(i)[0] == str(i)[1] == str(i)[2]:

#       count += 1

#print(count)

