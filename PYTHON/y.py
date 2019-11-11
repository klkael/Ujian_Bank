import x

print(x.nama)
print(x.usia)
print(x.halo('Ali'))
objA = x.test()
print(objA.nama)

import datetime as dt
x = dt.datetime.now()
print(x)
print(x.strftime('%d')) #tanggal
print(x.strftime('%A')) #hari
print(x.strftime('%m')) #bulan
print(x.strftime('%B')) #nama bulan
print(x.strftime('%Y')) #tahun
print(x.strftime('%H')) #24 jam
print(x.strftime('%I')) #12 jam
print(x.strftime('%p')) #am/pm
print(x.strftime('%M')) #min
print(x.strftime('%S')) #sec