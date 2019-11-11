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