# import datetime as dt
# x = dt.datetime.now()

# class time:
#     def __init__ (self):
#         days = {
#             'Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu',
#             'Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu','Sunday':'Minggu'
#         }
#         self.hari = days[x.strftime('%A')]
#         self.tanggal = x.strftime('%d')
#         self.bulan = x.strftime('%m')
#         self.tahun = x.strftime('%Y')
#         self.jam = x.strftime('%H')
#         self.menit = x.strftime('%M')
#         self.detik = x.strftime('%S')

# import statistics
# x = [1,2,3,4,5,6,7,8,9]
# print(statistics.mean(x))
# print(statistics.median(x))

# x = [1,4,5,9,9,11,13]
# x.sort()
# print(x)
# mean = sum(x)/len(x)
# print(mean)

# tengah = round(len(x)/2)

# if len(x) %2 != 0:
#     median = x[tengah]
# else:
#     median = (x[tengah]+x[tengah-1])/2

# print(median)

from functools import reduce
class itung:
    def __init__ (self):
        self.mean = sum(x)/len(x)

class statistik:
    def ratarata(self,x):
        total = reduce(lambda a,b:a+b,x)
        return total / len(x)
    def nilaitengah(self,x):
        x.sort()
        if len(x) %2 != 0:
            iTengah = [int(len(x)/2)]
        else:
            iTengah = [int(len(x)/2)-1,int(len(x)/2)]
        aTengah = list(map(lambda a: x[a], iTengah))
        total = reduce(lambda x,y:x+y,aTengah)
        return total / len(aTengah)        

stat = statistik()
print(stat.ratarata([1,2,3,4,5,6,7,8,9,9,9,9,10]))
print(stat.nilaitengah([1,2,3,4,5,6,7,8,9]))
        

# angka = itung()
# print(angka.mean)