x = 18
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(1+8*2)
print((1+8)*2)
# nomor 6 typenya float (koma-komaan), pembagian selalu jadi float, kalo float ada angka belakang komanya
print(int(x / y))
print('1234.890')
print(float('1234.890'))
print(y**2)
print(pow(2,2))
# sisa pembagian 
print(10%5)
print(9%5)
print(5%5)
# absolut (abs) buat ilangin minus, buat ambil value nya aja
x = -90.123
print(abs(x))
# akar pangkat
print(4**(1/2))
print(27**(1/3))
print(max(1,2,3,4,5,6,7,8,9,10))
print(min(1,2,3,4,5,6,7,8,9,10))
print(min(1,2,3,4,5,6,7,8,10,0.1,0.2))
print(round(3.6743))
print(round(3.6743,2))
print(0.1+0.2)
print(round(0.1+0.2,1))

import math
print(math.pi)
print(math.floor(3.9))
print(math.ceil(3.1))
print(math.sqrt(196))
# sqrt = akar pangkat = square root
print(math.factorial(3))

jH = 13 #ayam = jH-kambing
jK = 32 #kA*ayam + kK*kambing = jK
kA = 2
kK = 4
# kA*ayam + kK*kambing = jK
# kA*(jH-kambing)+(kK*kambing)=jK
# (kA*jH)-(kA*kambing)+(kK*kambing)=jK #yang mau dicari 'kambing'nya
# -(kA*kambing)+(kK*kambing)=jK-(kA*jH)
# kambing(-kA+kK)=jK-(kA*jH)
# kambing=(jK-(kA*jH)/(-kA+kK))

ayam = (jK - (kK * jH))/ (kA - kK)
kambing = (jK - (kA * jH))/ (kK - kA)

print(ayam)
print(kambing)


jumlah_hewan = input('Ketik total hewan? : ')
va = int(jumlah_hewan)
jumlahkaki = input('Ketik total kaki hewan? : ')
vava = int(jumlahkaki)
kakihewana = input('Ketik jumlah kaki hewan A? : ')
vavava = int(kakihewana)
kakihewanb = input('Ketik jumlah kaki hewan B? : ')
vavavava = int(kakihewanb)
hewanA = (((va*vavavava)-vava)/vavava)
hewanB = va-hewanA
print('Jumlah Hewan A adalah : ',hewanA,'Jumlah Hewan B adalah : ',hewanB )

x = 4
y = 3
z = 2
w = (((x+y*z)/x*y)**2)
print(w)

tahun = (781/360)
jumlahtahun = round(tahun)
jumlah_tahun = int(jumlahtahun)
sisahari = (781%360)
bulan = (sisahari/30)
jumlahbulan = round(bulan)
jumlah_bulan = int(jumlahbulan)
sisanya = (sisahari%30)
print(jumlah_tahun,'Tahun',jumlah_bulan,'Bulan',sisanya,'Hari')