import json

with open('ccNasabah.json','r') as x:
    out = json.load(x)

valid = []
invalid = []
for index in range(len(out)):
    creditcard = out[index]["noCreditCard"]
    creditcard = creditcard.split("-")
    creditcard = "".join(creditcard)
    

    if creditcard[0]=="4" and len(creditcard) == 16:    
        if " " in creditcard:
            invalid.append(out[index])
        elif creditcard[index].isalpha():
            invalid.append(out[index])
        elif "-" in creditcard:
            invalid.append(out[index])
        else: 
            valid.append(out[index])

    elif creditcard[0] == "5" and len(creditcard) == 16:
        if " " in creditcard:
            invalid.append(out[index])
        elif creditcard[index].isalpha():
            invalid.append(out[index])
        elif "-" in creditcard:
            invalid.append(out[index])
        elif "9999" in creditcard:
            invalid.append(out[index])
        else:
            valid.append(out[index])

    elif creditcard[0] == "6" and len(creditcard) == 16:
        if " " in creditcard:
            valid.append(out[index])
        elif creditcard[index].isalpha():
            invalid.append(out[index])
        elif "-" in creditcard:
            invalid.append(out[index])
        elif "61234" in creditcard:
            invalid.append(out[index])
        else: 
            valid.append(out[index])
    else:
        invalid.append(out[index])

with open("valid.json","w") as y:
    json.dump(valid,y)
with open("invalid.json","w") as z:
    json.dump(invalid,z)