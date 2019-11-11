# dictionary
andi = {'name':'Andi','age':'22','is_married':False}
print(andi['name'])
print(andi['age'])
print(andi['is_married'])
print(andi.get('name'))
print(andi.get('job'))
# print(andi['job']) pasti error
# Pake get kalo ga ada isinya hasilnya jadi none

print(andi.get('job', 'Maaf andi masih nganggur'))
print(andi)
print(type(andi))
andi['name'] = 'budi'
print(andi)

andi = {'name':'Andi','age':'22','is_married':False,'job':'pns','cars':['Alphard','Xpander','Innova'],'address':{'street':'Mawar_Ungu','RT':'5','RW':'121','kecamatan':'x','zip_code':'12332','geo':{'lat':111.11,'lng':65.89}}}
print(andi['cars'][0])
print(andi['address']['geo'])

andi['salary']=25000000 #nambah property/elemen dalam dictionary
print(andi)
andi.update({'ktp':123123123})
print(andi)
print(list(andi))
print(andi.keys()) #kalo ga pake list depannya, nanti muncul dict_values di hasilnya
print(list(andi.keys()))
print('\n')
print(andi.values())
print(list(andi.values()))

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