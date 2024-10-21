"""INTAGERS"""

a = 20  # Sonlar musbat yoko
b = -30 # manfiy bo'lishi mumkin
c = a + b
print(c)

# Kvadratning yuzini hisoblaymiz

kvdrt_tmni = 20 # Kavdratning tomoni 20 ga teng
kvdrt_yuzi = kvdrt_tmni**2 # Kvadrat yuzini hisoblaymiz
print(kvdrt_yuzi)

"""FLOATS — O'NLIK SONLAR"""

pi = 3.14159 # o'nlik son (float)
radius = 10  # butun son (integer)
diametr = 2*radius
print("Aylana uzunligi ", pi*diametr, " ga teng.")

"""BUTUN SONDAN O'NLIK SONGA"""

a = -20
b = 40
c = b/a
print(c) # natija o'nlik son bo'ladi

a = 2
b = 3.0
# Quyidagi arifmetik amallarning natijasi o'nlik son hosil qiladi
print(a+b) 
print(a*b)
print(a**b)
print(2*(a+b))

"""UZUN SONLARNI KIRITISH"""

aholi_soni = 7_594_000_000 # o'zmizga qulay bo'lishi uchun shinday yozdik
print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")

"""KONSTANTA"""

PI = 3.14159
raduis = 21.2

"""BIR NECHTA O'ZGARUVCHIGA QIYMAT BRISH"""

x, y, z = 10, -7.25, -30

"""O'ZGARUVCHI TURINI ALMASHTIRISH"""

ism = 'Jobir'
yosh = 36
xabar = ism + ' ' + yosh + ' yoshda'
print(xabar)

"""O'ZGARUVCHI TURINI TEKSHIRISH"""

ism = 'Jobir'
yosh = 36
print(type(ism))  # ism degan o'zgaruvchining turini konsolga chiqaramiz
print(type(yosh)) # ismyosh degan o'zgaruvchining turini konsolga chiqaramiz

"""INPUT() VA SONLAR"""


#1 foydalanuvchining tug'ilgan yilini so'raymiz
t_yil = input("Tug'ilgan yilingizni kiriting: ")
#2 foydalanuvchi yoshini xisoblaymiz
yosh = 2020 - t_yil # 
#3 foydalanuvchi yoshini konsolga chiqaramiz
print("Siz " + yosh + " yoshda ekansiz")


#1 foydalanuvchining tug'ilgan yilini so'raymiz va qiymatni int ga aylantiramiz
t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
#2 foydalanuvchi yoshini xisoblaymiz
yosh = 2020 - t_yil # 
#3 foydalanuvchi yoshini konsolga chiqaramiz
print("Siz " + str(yosh) + " yoshda ekansiz")


#1.1 foydalanuvchining tug'ilgan yilini so'raymiz
t_yil = input("Tug'ilgan yilingizni kiriting: ")
#1.2 t_yil o'zgaruvchini int ga aylantiramiz
t_yil = int(t_yil)
#2 foydalanuvchi yoshini xisoblaymiz
yosh = 2020 - t_yil # 
#3 foydalanuvchi yoshini konsolga chiqaramiz
print("Siz " + str(yosh) + " yoshda ekansiz")