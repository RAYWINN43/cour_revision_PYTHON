# Écrivez un programme Python pour convertir les températures vers et depuis Celsius et Fahrenheit.

# temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")

# Saisissez la température que vous souhaitez convertir ? (par exemple, 45F, 102C etc.) : 104f                                     
# La température en Celsius est de 40 degrés.

a = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")
value = float(a[:-1])

if a[-1]=='c' or a[-1]=='C':
    b = (value * 9 / 5) + 32
    print(b)
else :
    b = (value - 32) * 5 / 9
    print(b)