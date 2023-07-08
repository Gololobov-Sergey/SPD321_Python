
import random

#autos1 = ["BMW", "Audi", "Mercedes", "BMW X10"]

#autos2 = list(("BMW", "Audi", "Mercedes"))

#autos2 = autos1[:]

#autos1[1] = "Renault"



#print(autos1)
#print(autos2)

#autos3 = list()
#autos4 = []
#print(autos3)
#print(autos4)

#list1 = list("BMW")
#print(list1)

#list2 = [i*i for i in range(10)]
#print(list2)

#list3 = [random.randint(0, 100) for i in range(10)]
#print(list3)


#list4 = [random.choice("abcdef") for i in range(10)]
#print(list4)

#list5 = [i for i in autos1 if i != "BMW"]
#print(list5)

#print(autos1[::-1])

#print(len(list3))
#print(max(list3))
#print(min(list3))
#print(sum(list3))
#print(sorted(list3))


#maxnum = list3[0]

#for i in list3:
#    if i > maxnum:
#        maxnum = i

#print(maxnum)


#print(autos1 * 3)

list3 = [random.randint(-5, 5) for i in range(10)]
print(list3)

neg = 0
dob_i_3 = 1
maxnum = list3[0]
minimum = list3[0]
imax = 0
imin = 0
for i in range(len(list3)):
    if list3[i] < 0:
        neg += list3[i]

    if i % 3 == 0:
        dob_i_3 *= list3[i]

    if list3[i] > maxnum:
        maxnum = list3[i]
        imax = i

    if list3[i] < minimum:
        minimum = list3[i]
        imin = i


if imin > imax:
    imax, imin = imin, imax

d = 1
for i in range(imin + 1, imax):
    d *= list3[i]

d1 = 1
for i in list3[imin+1:imax]:
    d1 *= i

print(d)
print(d1)

dot1 = -1
for i in range(len(list3)):
    if list3[i] > 0:
        dot1 = i
        break

dot2 = -1
for i in range(len(list3) - 1, -1, -1):
    if list3[i] > 0:
        dot2 = i
        break

sum = 0
if dot1 != -1 and dot2 != -1:
    for i in range(dot1 + 1, dot2):
        sum += list3[i]

print(sum)


#list3.append("mama")
#print(list3)

list4 = list3.copy()

print(list3.count(0))

list3.extend(list4)
print(list3)

if 0 in list3:
    print(list3.index(0))

imax = list3.index(max(list3))
imin = list3.index(min(list3))
print(list3[imin : imax])


list3.insert(2, 999)
print(list3)

#list3.pop(2)
if 999 in list3:
    list3.remove(999)
print(list3)

list3.sort(reverse=True)
print(list3)



list8 = [[1,2,3],
         [4,5,6]]
print(list8[1][2])

for i in range(len(list8)):
    for j in range(len(list8[i])):
        print(list8[i][j], end=" ")
    print()

for i in list8:
    print(i)

print(list8)