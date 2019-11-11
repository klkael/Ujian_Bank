x = [(1,2,3),(4,5,6)]
x[0]='Andi'
print(x)

x=[(1,['a','b','c'],3),(4,5,6)]
x[0][1][2]='Andi'
print(x)
x[0][1].append('d')
print(x)

x = [1,2,3,1,2,3]
y = (1,2,3,1,2,3)
z = {1,2,3,1,2,3} #set/himpunan, tidak bisa indexing(tidak bisa print angkanya satu-satu)
print(x)
print(y)
print(z)
#set/himpunan:
#1. no indexing
#2. duplicate element not allowed
#3. set itu muteable, tp elemennya immutable (bisa ditambah tuple tapi gabisa tambah list)
z = {1,2,3,1,2,3}
z.add('a')
z.add(('c','d','e'))
print(z)

z = {1,2,3,1,2,3}
a = []
for i in z:
    a.append(i)
print(a)

z.update('Andi')
z.update([6,7,8])
z.update({'z','budi'})
print(z)
z.update('andi')
print(z)
print('budi' in z)
z.remove('budi')
z.discard('deni') #bedanya sama remove, kalo discard walau elemennya ga ada tetep ga error, kalo remove error
print(z)
z.pop()
print(z)

x = set([1,2,3])
y = frozenset([1,2,3])
x.remove(2)
# y.remove(2) #jadi error kalo diaktifin, frozen set mirip tuple, gabisa di ubah-ubah
print(type(y))
print(len(y))