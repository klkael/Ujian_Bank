# def angka(number):
#     for i in range(1,number+1):
#         if(i%3==0 and i%5==0):
#             print('xy'),
#         elif(i%5==0):
#             print('y'),
#         elif(i%3==0):
#             print('x'),
#         else:
#             print(i),

# angka(16)       

# a=[4,5,6,7,3,3,2,1,7,4,7,9,0,8]
# b=[]
# for i in a:
#     if(i<5):
#         b.append(i)

# b.sort()
# print(b)

# for i in range(2,10,2):
#     print(i)
# else:
#     print('OK')

# for i in range(2,10):
#     if i==7:
#         continue #bisa pake break juga
#     print(i)

# for i in range(0,11):
#     if(i%2==0):
#         print('WOW'),
#     else:
#         print('TIDAK WOW'),

# z = ''
# for item in range(5): #print enter kebawah
#     for item2 in range(5-item): #print bintang ke kanan
#         z+= '*'
#     z += '\n'
# print(z)

x=[0,1,2,3,4,5,6,7]
y=['Andi','Budi','Caca']

def balikposisi(mylist):
    hasil = []
    for i in range(len(mylist)):
        hasil.insert(0,mylist[i])
    return hasil
print(balikposisi(x))
print(balikposisi(y))

x=['Andi','Budi','Caca']
y=[3,5,7,9]
def balikPosisi(mylist):
    for e in range(round(len(mylist)/2)):
        asli = mylist[e]
        mylist[e] = mylist[len(mylist)-1-e]
        mylist[len(mylist)-1-e] = asli
    return mylist
print(balikPosisi(x))
print(balikPosisi(y))

def ubahVokal(kata):
    output = ''
    for huruf in kata:
        if huruf in 'aiueo':
            output = output + 'o'
        else:
            output = output + huruf
    return output
print(ubahVokal('kelvin'))

def palindrome(s):
    i=0
    while i<=(len(s)/2):
        if s[i]!=s[-i-1]:
            return False
        i += 1
    return True

# print(palindrome('poiuytr'))

x = 'kelvin'
y = list(x[::-1])
print(y) #masi list
y = ''.join(y) #buat ubah jadi string
print(y) 

def palindromee(kata):
    if kata==kata[::-1]:
        return True
    else:
        return False

print(palindromee('kelvin'))

def reversewordsentence(sentence):
    words = sentence.split(' ')
    newWords = [word[::-1] for word in words]
    newSentence = ' '.join(newWords)
    return newSentence
print(reversewordsentence('hai apa kabar'))

#kode morse
#caesar cipher positif

MORSE_CODE = {'A':'.-', 'B':'-...', 
'C':'-.-.', 'D':'-..', 'E':'.', 
'F':'..-.', 'G':'--.', 'H':'....', 
'I':'..', 'J':'.---', 'K':'-.-', 
'L':'.-..', 'M':'--', 'N':'-.', 
'O':'---', 'P':'.--.', 'Q':'--.-', 
'R':'.-.', 'S':'...', 'T':'-', 
'U':'..-', 'V':'...-', 'W':'.--', 
'X':'-..-', 'Y':'-.--', 'Z':'--..', 
'1':'.----', '2':'..---', '3':'...--', 
'4':'....-', '5':'.....', '6':'-....', 
'7':'--...', '8':'---..', '9':'----.', 
'0':'-----', ', ':'--..--', '.':'.-.-.-', 
'?':'..--..', '/':'-..-.', '-':'-....-', 
'(':'-.--.', ')':'-.--.-'}

def morse(kalimat):
    final_string = ''
    for letter in kalimat:
        final_string += MORSE_CODE[letter]
    return final_string

print(morse('KELVIN'))
print(MORSE_CODE['X'])

alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n'
,'o','p','q','r','s','t','u','v','w','x','y','z']

# indextokalimat

def cesarcipher(kalimat,jarak):
    kalimatbaru = ''
    for letter in kalimat:
        if letter in alfabet:
            index = alfabet.index(letter)
            letterbaru = alfabet[(index + jarak) % len(alfabet)]
            kalimatbaru += letterbaru
        else:
            kalimatbaru += letter
    return kalimatbaru

print(cesarcipher(input('Masukan Kata :'), int(input('Masukan Jaraknya :'))))


