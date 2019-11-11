x = [1,2,3,4]
asd = []
for item in x:
    asd.append(item**3)
print(asd)

def hello():
    print('Hello World!')

hello();hello();hello()

def kuadrat(x):
    print(x**2)
kuadrat(2)
kuadrat(3)

# def pangkat(angka1, angka2):
#     print(angka1**angka2)
# pangkat(2,3)
# pangkat(2,4)
# pangkat(
#     float(input('Ketik angka pertama :')),
#     float(input('Ketik angka kedua :'))
#     )

# def ganjilgenap(x):
#     if x%2 == 0:
#         print(x, 'Tergolong GENAP')
#     else:
#         print(x, 'Tergolong GANJIL')

# ganjilgenap(2)
# ganjilgenap(99.28678)

# def kalkulator():
#     x = float(input('Masukan Angka Pertama :'))
#     op = input('Masukan Operator (+-*/) :')
#     y = float(input('Masukan Angka Kedua :'))
#     if op == '+':
#         print(x+y)
#     elif op == '-':
#         print(x-y)
#     elif op == '*':
#         print(x*y)
#     elif op == '/':
#         print(x/y)
#     else:
#         print('Maaf Operator Belum Tersedia')
# kalkulator()

students = ['Andi','Budi','Caca']
def tes(x):
    print(x[0])
    print('Caca' in x)
tes(students)

# def vocal():
#     nama = input('Ketik Nama :')
#     print(nama.lower().replace('a','o')
#     .replace('i','o').replace('u','o').replace('e','o'))
# vocal()

def LuasPersegi(sisi):
    print('Luas =', sisi*sisi)
def LuasPersegiReturn(sisi):
    return sisi*sisi
LuasPersegi(4)
print(LuasPersegi(4))
LuasPersegiReturn(4)
print(LuasPersegiReturn(4))

i=1
while i<10:
    # print(i) #dia bakal ngeprint terus
    print(i)
    i = i+1 #i +=1
i = 20
while i>1:
    print(i)
    i = i-2 #i -=2

students = ['andi','budi','caca']
index = 0 #mau mulai dari mana
while index <= len(students) -1: #-1 karena kalo len pasti kluarnya 3, indexnya cuma sampe 2
    print(students[index])
    index += 1

x = [1,2,3,4,5,6,7,8,9,10]
y = []
index = 0
while index<= len(x)-1:
    y.append(x[index]**2)
    index += 1
print(y)

i=1
while i < 10:
    print(i)
    if i == 5:
        break #buat nge stop sampe i
    i += 1
i=0
while i < 10:
    i+= 1
    if i==5:
        continue #buat nge skip i
    print(i) 

# password = '12345'
# inputuser = ''
# while inputuser != password:
#     inputuser = input('Ketik Password :')
#     if inputuser != password:
#         print('Password Salah')
#     else:
#         print('Password Benar')

password = '12345'
inputuser = ''
jumlahInput = 0
batasInput = 5
lebih = False

while inputuser != password and not lebih:
    if jumlahInput < batasInput:
        inputuser = input(f'Input ke-{jumlahInput+1}, Ketik Password :')
        jumlahInput +=1
    else:
        lebih=True
if lebih!=True:
    print('Selamat Datang')
else:
    print('Coba lagi 24 Jam')
    