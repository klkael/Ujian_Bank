class Mobil:
    warna = 'merah'
    tahun = 2010

#create objek mobil1
mobil1 = Mobil()
print(mobil1.warna)
print(mobil1.tahun)

class MobilCustom():
    def __init__(self,warna,tahun,model):
        self.color = warna
        self.tahun = tahun
        self.model = model
    #method
    def jadul(self):
        if self.tahun < 2010:
            return True
        else:
            return False
    def tes(self):
        print(self.color,self.tahun,self.model,self.jadul())

#syntatic sugar
mobil1 = MobilCustom('pink',2018,['A','B']) #kalo mau salah satu atribut kosong, dikasi string kosong ('')
mobil2 = MobilCustom('blue',2010,'X')
mobilA = MobilCustom('red',1998,'A')
mobilB = MobilCustom('red',2010,'B')

print(mobil1.color)
print(mobil2.tahun)
print(mobil1.model)
print(mobilA.jadul())
print(mobilB.jadul())
print(mobilB.tes())

class Mobil:
    def __init__(self,warna,seat):
        self.warna = warna
        self.seat = seat

class Car(Mobil): #inheritance
    # pass pass untuk salin persis
    gps = True

mobil1 = Mobil('pink',4)
car1 = Car('red',5)
print(mobil1.warna, mobil1.seat)
print(car1.warna, car1.seat, car1.gps)

class X:
    def __init__(self,nama,gelar):
        self.nama = nama
        self.gelar = gelar

# class Y(X):       #ada 3 pilihan untuk copy X
#     pass

# class Y(X):
#     def __init__(self,nama,gelar):
#         X.__init__(self,nama,gelar)

class Y(X):
    def __init__(self,nama,gelar):
        super().__init__(nama,gelar)
        self.kampus = 'UGM'

objX = X('Budi','DR')
objY = Y('Mamang','S.E')

print(objX.nama)
print(objY.gelar)
print(objY.kampus)

from pprint import pprint
pprint(vars(objY))

print(vars(objX))
print(vars(objY)) #beda lagi sama yg pprint

# buat nambah atribut

setattr(objX,'alamat','BSD')
objY.warna = 'merah'

print(vars(objX))
print(vars(objY))

class Z:
    nama = 'Z'
    usia = 21

objZ = Z()
print(objZ.nama)
print(objZ.usia)

del Z.nama
print(objZ.usia)
# print(objZ.nama) error

nama = 'ultraman'
vars()[nama] = 12345
#mau bikin ultraman = 12345
print(ultraman)

class student:
    def __init__(self,nama,usia):
        self.nama = nama
        self.usia = usia

data = [
    {'nama' : 'Andi','usia' :21},
    {'nama':'Budi','usia':22},
    {'nama': 'Caca','usia' : 23},
    {'nama':'Deni','usia' : 24}
]

# def createobj(x):
#     nama = x['nama']
#     vars()[nama] = student(x['nama'],x['usia'])
#     return vars()[nama]

# def createObj(x):
#     return student(x['nama'], x['usia'])     #ada 3 cara

objNew = list(map(lambda x: student(x['nama'], x['usia']),data))


print(objNew)
print(objNew[0].nama)
print(objNew[0].usia)

class persegi:
    def __init__(self,sisi):
        self.sisi = sisi
        self.keliling = self.sisi *4
        self.luas = self.sisi **2

persegiA = persegi(4)
persegiB = persegi(3)
persegiC = persegi(5)

print(vars(persegiA))
print(vars(persegiB))
print(vars(persegiC))

# class roman:
#     def angkatoromawi(self,num):


class Orang:
    def __init__(self,nama):
        self.nama = nama

class Pria(Orang):
    def __init__(self,nama):
        Orang.__init__(self,nama)
        self.gender = 'Laki - Laki'

ObjA = Orang('Andi')
ObjB = Pria('Andi')
print(vars(ObjA))
print(vars(ObjB))

class X:
    def __init__(self,x):
        self.x = x

class Y(X):
    def __init__(self,x,y):
        X.__init__(self,x)
        self.y = y

class Z(Y):
    def __init__(self,x,y,z):
        Y.__init__(self,x,y)
        self.z = z

objA = Z('Andi','PNS',True)
print(vars(objA))

class Karnivora:
    def __init__(self):
        self.daging = True
        self.nama = 'Karnivora'

class Herbivora:
    def __init__(self):
        self.tumbuhan = True
        self.nama = 'Herbivora'

class Omnivora(Karnivora,Herbivora):
    def __init__ (self):
        Karnivora.__init__(self)
        Herbivora.__init__(self) #nentuin urutannya dari sini
        self.mcd = True
        # self.nama = 'omnivora'

objA = Omnivora()
print(vars(objA))
print(Omnivora.__mro__) #ngeliat urutan