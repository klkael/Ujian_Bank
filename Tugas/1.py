
nama = 'Hari ini Hari tidak masuk sekolah'
# jumlah huruf h
cari = 'h'
x = nama.upper().replace(cari.upper(), '')
print(x)
h = len(nama) - len(x)
print(f'Jumlah huruf \'{cari}\' ada = {h}')

#jumlah kalimat hari
cari = 'hari'
x = nama.upper().replace(cari.upper(), '')
print(x)
jumlahcari = int((len(nama) - len(x)) / len(cari))
print(f'jumlah kata \'{cari}\' ada = {jumlahcari}')