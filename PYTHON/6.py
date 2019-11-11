x=4
if x==4: #sama dengannya harus 2x
    print('x nya 4')
else:
    print('bukan 4')

nilai = 81
if nilai > 80:
    print('Anda lulus')
elif nilai < 40:
    print('Anda Tidak lulus')
else:
    print('Anda remedial')

if nilai>80:
    print(f'Nilai Anda {nilai}, Anda Lulus')
elif nilai<40:
    print(f'Nilai Anda {nilai}, Anda Tidak Lulus')
else:
    print(f'Nilai Anda {nilai}, Anda Remedial')

jomblo = True
if jomblo:
    print('Anda Jomblo')
else:
    print('Anda taken')

jomblo = False; nganggur = False
if jomblo and nganggur:
    print('Kasian')
if not jomblo and nganggur:
    print('Lumayan')
if jomblo and not nganggur:
    print('Lumayan Juga')
else:
    print('Manteb')

x = 2; y=5
print(x<10 and y>0)

Nilai = 99
if Nilai >=82:
    print('nilai anda A')
elif Nilai <=81 and Nilai >=72:
    print('nilai anda B')
elif Nilai <=71 and Nilai >62:
    print('nilai anda C')
elif Nilai >=52 and Nilai <=61:
    print('nilai anda D')
else:
    print('nilai anda E')

x={1:True, 2:False}
print(x.items())
print(list(x.items()))