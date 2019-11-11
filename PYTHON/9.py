# star = ''
# for i in range(5):
#     star += '*'
#     print(star)

# def star(x):
#     star = ''
#     for i in range(x):
#         star += '*'
#         print(star)
# star(10)

# def star(x):
#     star = ''
#     for i in range(x):
#         for j in range(x-i):
#             star += '*'
#         star += '\n'
#     print(star)
# star(10)

def rStar(x):
    star = ''
    for i in range(x):
        star = '*' * (x-i)
        print(star)
rStar(10)

def star(x):
    star = ''
    for i in range(x):
        star += str(i+1)+' '
        print(star)
star(5)

def star(x):
    z=x+1
    for i in range(1,z):
        star = ''
        for j in range(1,(z+1-i)):
            star += str(j) + ' '
        print(star)
star(5)

def rstar(x):
    for i in range(1,(x+1)):
        star = ''
        star += (str(i) +' ') * i
        print(star)
rstar(5)

def rstar(x):
    z = x+1
    for i in range(1,z):
        star =''
        star += (str(i)+' ')*(z-i)
        print(star)
rstar(5)

def star(x):
    star = ''
    for i in range(x):
        star += str(x-i)+' '
        print(star)
star(5)

def star(x):
    z = x+1
    for i in range(1,z):
        star = ''
        for j in range(1,(z+1-i)):
            star += str(z-j)+' '
        print(star)
star(5)

# n = int(input('Jumlah Baris :'))
# for i in range(0,n+1):
#     for j in range(1,n-i+1):
#         print(j,end='')
#     print()
# for i in range(0,n+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()
   
def pangkatB(x,y):
    if(y==1):
        return x
    else:
        return x * pangkatB(x,y-1)
print(pangkatB(2,3))
        
def faktorial(z):
    if z <=2:
        return z
    else:
        return z * faktorial(z-1)
print(faktorial())

def faktorial1(z):
    angka = 1
    for i in range(z):
        angka = angka * z
        z -=1
    print(angka)
faktorial1(5)

def faktorial2(x):
    angka = 1
    for i in range(1, x+1):
        angka *= i
    return angka
print(faktorial2(5))