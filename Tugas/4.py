days = {
    'senin':'monday','selasa':'tuesday',
    'rabu':'wednesday','kamis':'thursday',
    'jumat':'friday','sabtu':'saturday',
    'minggu':'sunday'
}
# nama_hari=input('Ketik nama hari : ')
InggrisList = list(days.values())
IndoList = list(days.keys())
day = input('Masukan Nama Hari : ')
daylower = day.lower()
#harinya = (InggrisList.index(daylower))
# translate = (IndoList[harinya])
# print(f'{day} Dalam Bahasa Indonesia Adalah {translate}')

if daylower in InggrisList:
    harinya = (InggrisList.index(daylower))
    translate = (IndoList[harinya])
    print(f'{day} Dalam Bahasa Indonesia Adalah {translate}')
else:
    harinya2 = (IndoList.index(daylower))
    translate2 = (InggrisList[harinya2])
    print(f'Hari {day} Dalam Bahasa Inggris Adalah {translate2}')