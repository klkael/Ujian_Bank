def segitigaKata(kata):
    hasil = ''
    for i in range(0,len(kata)):
        for j in range(0,i+1):
            print(kata[j],end="")
        print()
segitigaKata('halo')

# def segitigakata(kata):
#     index = 0
#     while index <= len(kata) -1:
#         print(kata[index])
#         index += 1

# segitigakata('haloapakabar')

def contalpha(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(num)
            print(ch, end=" ") 
            num = num +1
        print("")
n = 5
contalpha(n) 


