class X:
    def __init__(self,name,age):
        self.nama = name
        self.usia = age
    def pensiun(self):
        return 55 - self.usia

class Y(X):
    def __init__(self,name,age,city):
        X.__init__(self,name,age)
        self.kota = city


objA = Y('Ali',22,'Jakarta')
print(objA.kota)
objX = X('Andi',22)
print(objX.pensiun())
objY = Y('Budi',23,'Bandung')
print(objY.pensiun())