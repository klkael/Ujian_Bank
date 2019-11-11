star = ''
for i in range(5):
    star += '*'
    print(star)

def star(x):
    star = ''
    for i in range(x):
        star += '*'
        print(star)
star(10)

def star(x):
    star = ''
    for i in range(x):
        for j in range(x-i):
            star += '*'
        star += '\n'
    print(star)
star(10)

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