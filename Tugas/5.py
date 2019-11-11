# Nilai = 99
# if Nilai >=82:
#     print('nilai anda A')
# elif Nilai <=81 and Nilai >=72:
#     print('nilai anda B')
# elif Nilai <=71 and Nilai >62:
#     print('nilai anda C')
# elif Nilai >=52 and Nilai <=61:
#     print('nilai anda D')
# else:
#     print('nilai anda E')


# def ganjilgenap(x):
#     if x%2 == 0:
#         print(x, 'Tergolong GENAP')
#     else:
#         print(x, 'Tergolong GANJIL')

# print(ganjilgenap(5))

# def kalkulator():
#     x = float(input('Masukan Angka Pertama :'))
#     op = input('Masukan Operator (+-*/) :')
#     y = float(input('Masukan Angka Kedua :'))
#     if op == '+':
#         print(x+y)
#     elif op == '-':
#         print(x-y)
#     elif op == '*':
#         print(x*y)
#     elif op == '/':
#         print(x/y)
#     else:
#         print('Maaf Operator Belum Tersedia')
# kalkulator()

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

# angka(15)

# MORSE_CODE = {'A':'.-', 'B':'-...', 
# 'C':'-.-.', 'D':'-..', 'E':'.', 
# 'F':'..-.', 'G':'--.', 'H':'....', 
# 'I':'..', 'J':'.---', 'K':'-.-', 
# 'L':'.-..', 'M':'--', 'N':'-.', 
# 'O':'---', 'P':'.--.', 'Q':'--.-', 
# 'R':'.-.', 'S':'...', 'T':'-', 
# 'U':'..-', 'V':'...-', 'W':'.--', 
# 'X':'-..-', 'Y':'-.--', 'Z':'--..', 
# '1':'.----', '2':'..---', '3':'...--', 
# '4':'....-', '5':'.....', '6':'-....', 
# '7':'--...', '8':'---..', '9':'----.', 
# '0':'-----', ', ':'--..--', '.':'.-.-.-', 
# '?':'..--..', '/':'-..-.', '-':'-....-', 
# '(':'-.--.', ')':'-.--.-'}

# def morse(kalimat):
#     final_string = ''
#     for letter in kalimat:
#         final_string += MORSE_CODE[letter]
#     return final_string

# print(morse('KELVIN'))
# print(MORSE_CODE['X'])

# alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n'
# ,'o','p','q','r','s','t','u','v','w','x','y','z']

# def cesarcipher(kalimat,jarak):
#     kalimatbaru = ''
#     for letter in kalimat:
#         if letter in alfabet:
#             index = alfabet.index(letter)
#             letterbaru = alfabet[(index + jarak) % len(alfabet)]
#             kalimatbaru += letterbaru
#         else:
#             kalimatbaru += letter
#     return kalimatbaru

# print(cesarcipher(input('Masukan Kata :'), int(input('Masukan Jaraknya :'))))

# def palindromee(kata):
#     if kata==kata[::-1]:
#         return True
#     else:
#         return False

# print(palindromee('kelvin'))
# print(palindromee('katak'))

# def palindrome(s):
#     i=0
#     while i<=(len(s)/2):
#         if s[i]!=s[-i-1]:
#             return False
#         i += 1
#     return True

# print(palindrome('poiuytr'))

def vocal():
    nama = input('Ketik Nama :')
    print(nama.lower().replace('a','o')
    .replace('i','o').replace('u','o').replace('e','o'))
vocal()

