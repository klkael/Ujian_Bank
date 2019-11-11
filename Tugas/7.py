def romawitoint(s):
        romawi = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and romawi[s[i]] > romawi[s[i - 1]]:
                int_val += romawi[s[i]] - 2 * romawi[s[i - 1]]
            else:
                int_val += romawi[s[i]]
        return int_val

print(romawitoint('MMMCMLXXXVI'))


x = [1,2,3,4,5,6,7,8,9,9,94,5,6,3,]
def mean(self,x):
    mean = sum(x) / len(x)
    return mean
def median(self,x):
    x.sort()
    tengah = int(len(x)/2)
    if len(x) % 2 != 0:
        median = x[tengah]
    else:
        median = (x[tengah]+x[tengah-1])/2
    return median
def modus(self,x):
    hitung = []
    for y in x:
        hitung.append(x.count(y))
        imax = hitung.index(max(hitung))
        mode = x[imax]
    return mode