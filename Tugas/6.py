from functools import reduce

angka = list(range(1,101))
z = reduce(lambda x,y:x+y,list(map(lambda x:x*2,filter(lambda x:x%2==0,angka))))
print(z)

for num in range(1,101):
    prima = []
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
            