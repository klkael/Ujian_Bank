a = list('abcde')
b = list('bcfgh')
print(a)
print(b)
a = set(a)
b = set(b)
print(a)
print(b)
print(a.intersection(b)) #irisan
print(b&a) #irisan juga
print(a|b) #union
print(a.difference(b)) #anggota a yang ga ada di b
print (b-a)
print(a.symmetric_difference(b)) #yang kembar dibuang
print(b.symmetric_difference(a))
print(a^b) #sama kaya symmetric diffrence

p = {1,2,4,7,9,19}
q = {5,12,16,17,6,7,9,19}
r = {3,8,6,19}
print(p.intersection(q))
print(p&q&r)
print(q-p-r)

s = {-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9}
p = {-4,-3,-2,-1,0,1,2,3,4}
q = {-7,-6,-5,-4,-3,-2,-1,0,1}
r = {-1,0,1,0,1,2,3,4,5,6,7}
print(p|q)
print(p|r)
print(q|r)

s = {0,1,2,3,4,5,6,7,8,9,10}
a = {1,3,5,7}
b = {5,7,9}
print(a-b)
print(b-a)
print(a&b)
print(a|b)
print(a&(a|b))
print(b&(a|b))
print((a|b)&(a|b))
print((a&b)|(a|b))
