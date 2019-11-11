# python : Lambda fuction
x = lambda a,b,c : a+b+c
def y(a,b,c):
    return a+b+c
print(x(2,3,4))
print(y(2,3,4))
print(type(x))

def myfunction(x):
    return lambda a : a ** x

pangkat2 = myfunction(2)
pangkat3 = myfunction(3)
pangkat4 = myfunction(4)

print(pangkat2(2))
print(pangkat3(4))
print(pangkat4(3))

x = lambda a : True if a%2==0 else False
print(x(2))

x = lambda a : print(a)
x('Hello')
print(x('Hello'))

def y(a):
    return len(a)
a=['Andi', 'Budi', 'Caca']

x=map(y,a)
print(x)
print(list(x))

a = ['Cokelat','Melon','Nangka']
b = ['Apel','Jeruk','Nanas']
def combi(a,b):
    return a+' '+b
x = map(combi,a,b)
print(x)
print(list(x))

a = [2,4,6,8,10]
def pangkat(a):
    return a**2
x = map(pangkat,a)
print(list(x))

z = map(lambda a:a**2,a)
print(list(z))

b = []
for i in a:
    b.append(i **2)
print(b)

x = range(11)

def kuranglima(x):
    if x<5:
        return False
    else:
        return True
y=filter(kuranglima,x)
print(list(y))

a=[1,2,3,4,5,6,7,8,9,10]
z=filter(lambda x:True if x>=5 else False,a)
print(list(z))

z = list(map(pow,[2,3],[2,3]))
print(z)

x = [1,2,3,4,5,99]
y = [1,2,6,7,8,99]
z = list(filter(lambda a:a in x,y))
print(z)

angka = [1,2,3,4]
hasil = 1
for i in angka:
    hasil *= i
print(hasil)

from functools import reduce
z = reduce(lambda x,y:x * y,angka)
print(z)

kata = ['ini','ibu','budi']
print(''.join(kata))

z = reduce(lambda x,y:x+y,kata)
print(z)

angka = [1,2,3,4]
z = list(map(lambda x:x*2,filter(lambda x:x>3,angka)))
print(z)

z = list(filter(lambda x:x>3,map(lambda x:x*2,angka)))
print(z)

angka = list(range(1,101))
z = reduce(lambda x,y:x+y,list(map(lambda x:x*2,filter(lambda x:x%2==0,angka))))
print(z)

for num in range(1,101):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)

