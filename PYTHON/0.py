print(1+1)
nama = "asd"
umur = 12
print(nama)
print("halo, aku " + nama)
print("umurku" + str(umur))
print("umurku", umur)
print('saya ' + nama + 'usia ' + str(umur))
print('saya', nama, 'usia', umur)
print('saya %s umur %d' %(nama, umur))
print('saya {} usia {}'.format(nama, umur))
print(f'saya {nama} usia {umur}')
print('-\n-')
print("jum'at")
print('jum\'at')
print('purwadhika\tSchool')
print('purwadhika\nSchool')
print('-\n-')
nama = 'andi raharja'
print(nama.lower())
print(nama.upper())
print('-\n-')
print(nama.islower())
print(nama.isupper())
print(nama.lower().isupper())
print(nama.upper().islower())
print('-\n-')
namaa = 'python oke sekali'
print(len(namaa))
print(namaa[0])
print(namaa[0:len(namaa)])
print(namaa[0:5])
# [start : stop : step]
print(namaa[0:len(namaa):2])

# huruf paling belakang ke berapa
print(namaa[len(namaa)-2])
print(namaa.index('a'))
print(namaa.replace('oke', 'keren'))

nama = 'Purwadhika Startup & Coding school'
# mencari jumlah huruf
print(len(nama.replace(' ', '')))
print(len(nama))
print(nama.lower().count('c'))

nama = 'Hari ini Hari tidak masuk sekolah'
# jumlah huruf h
cari = 'h'
x = nama.upper().replace(cari.upper(), '')
print(x)
h = len(nama) - len(x)
print(f'Jumlah huruf \'{cari}\' ada = {h}')

cari = 'hari'
x = nama.upper().replace(cari.upper(), '')
print(x)
jumlahcari = int((len(nama) - len(x)) / len(cari))
print(f'jumlah kata \'{cari}\' ada = {jumlahcari}')