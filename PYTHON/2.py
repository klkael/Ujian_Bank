x = 12
x = 13
x +=2  # x = x + 2
x -=2  # x = x - 2
x *=2  # x = x * 2
x /=2  # x = x / 2

x = 'abcdefghijklmnopqrstuvwxyzgg'
print(x)
print(x[0::2])
print('g' in x) #cek ada g atau engga di 'x'
print('12' in x) #cek ada 12 atau engga di 'x'
print(x.count('g'))

kalimat = 'Hari ini Andi tidak masuk kuliah'
huruf = 'h'
print(huruf.lower()in kalimat.lower())
print(kalimat.lower().count(huruf.lower()))

x = ['Andi','Budi','Caca',123,True]
print(x[len(x)-1])
print(x[0:4])

hari = ['senin','selasa','rabu','kamis','jumat','sabtu','minggu'] #kalo list buka tutup kurungnya harus yang kotak
now = 'minggu'
jumlah_hari = 100 #kalo mau itung mundur tinggal di minus
indexnow = hari.index(now)
sisahari = jumlah_hari%len(hari)
haricari = hari[(indexnow+sisahari)%7]
print(haricari)

print('senin' in hari)
print(hari.index('senin'))
hari.append('senin2') #nambahin paling belakang
print(hari)
hari.insert(4, 'senin3') #nyelipin tulisan di list (index ke berapa, tulisannya apa)
print(hari)
hari.clear()
print(hari)

x = [12,32,45,21,2]
x.sort() #ngurutin
print(x)
y = [1,2,3,4]
y.reverse() #puter balik urutan
print(y)
hari = hari[::-1] #puter balik urutan juga, ga muncul karena udah di clear di atas
print(hari)
x = [1,2,3,4,5]
print(list(reversed(x))) #puter balik urutan juga

x = [1,2,3,4,5,6,7,8,9]
y = x[::2].copy()
print(y)
print(x+y)
print(y*2)

z = [[1,2,3],[4,5,6],[7,8,9]]
print(z[0][1])
print(z[1][1])

a = [1,2,3] #list
b = (1,2,3) #tuple
#isi tuple tidak bisa diubah-ubah seperti insert,append,dll

# totalumur = 50
# umurayah + umurandi = 50
# umurayah = 50-umurandi
# umurandi = 50-umurayah
# 6(umurandi-4) = umurayah-4
# 6(umurandi) - 24 = umurayah-4
# 6(umurandi) = umurayah + 20
# 6(50 - umurayah) = umurayah + 20
# 300 - 6(umurayah) = umurayah + 20
# -7(umurayah) = -280
# umurayah = 40



