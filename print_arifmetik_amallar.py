"""PRINT"""

print("Assalom alaykum")

print(Hayrli tong!)#Natija: SyntaxError: invalid syntax .
# Bu safar esa Hayrli tong! yozuvi o'rniga, Syntax Error (sinteksda xatolik) xabari chiqdi. Xatolik qayerda?
# Avval aytganimizdek, print() funktsiyasi matn yoki ifodalarni konsolga chiqarish vazifasini bajaradi.
# Lekin bu funktsiya to'g'ri ishlashi uchun bir nechta qoidalarga amal qilish lozim.
# Jumladan, agar konsolga matn chiqarmoqchi bo'lsak, matnimiz albatta qo'shtirnoq yoki (" ") yoki birtirnoq(' ') orasida yozlishi kerak.

print("Hayrli tong!")

print('Hayrli tong!')

print('Men "Dell" markasidagi noutbuk sotib oldim')

#Agar matnni bir necha qatorga bo'lib yozish talab qilinsa,
# uchtalik qo'shtirnoq(""" """)yoki birtirnoqdan (''' ''')foydalanish mumkin:

print("""Odami ersang, demagil odami,
Oniki, yo'q xalq g'amidin g'ami""")

#Qatorga bo'lishning yana bir usuli, qator so'nggida \n belgisini qo'yish.

print("Odami ersang, demagil odami,\nOniki, yo'q xalq g'amidin g'ami")

#Yuoqridagi matnni birtirnoq orqali ham konsolga chiqarish mumkinmi? 
# Matndagi yo'q, g'am so'zlaridagi birtirnoqlar bunga to'sqinlik qilmaydimi? Qiladi.
# Buning oldini olish uchun esa matndagi birtirnoq belgisidan avval \ belgisini qo'yish lozim. 

print('Odami ersang, demagil odami, \nOniki, yo\'q xalq g\'amidin g\'ami')

# Yuqoridagi kodga e'tibor bergan bo'lsangiz "yo'q" so'zi yo\'q ko'rinishida "g'am" so'zi esa g\'am ko'rinishida yozilgan.
# Umuman olganda \ belgisi har qanday mahsus belgi oldidan qo'yiladi.
# Agar yuqordagi kodimizda \ belgisini ishlatmaganimizda natija qanday bo'lar edi?


print('Odami ersang, demagil odami,\nOniki, yo'q xalq g'amidin g'ami') 
    #   Natija: SyntaxError: invalid syntax
    
"""ARIFMETIK AMALLAR"""

print(2+4*2)
print(19/5)
print(20/5)
print(16//4)
print(10//3)
print(2**4)



# print() yordamida matn va ifodalarni jamlab chiqarish ham mumkin. Buning uchun har bir ifoda va matn vergul (,) bilan ajratiladi.

print("To'qqizning kvadrati", 9**2, "ga teng")

print('3x3=',3*3)

# IZOHLAR (COMMENTS)

print(2*5*3.14159)

#Radiusi 5 ga teng bo'lgan aylananing uzunligi quyidagicha hisoblanadi
print(2*5*3.14159)

#Yuqoridagi misolda # belgisidan keyin yozilgan matn izoh (comment) deyiladi. 


# Izoh alohida qatorda yoki qator oxiridan ham yozilishi mumkin. 
# Python # dan keyingi har qanday matnni (qator oxirigacha) e'tiborsiz qoldiaradi.
# dan keyin yozligan kodlar ham bajarilmaydi:

print("Assalom alaykum!") # Bu matn konsolda chiqadi
#Keyingi qator esa bajarilmaydi
#print("Mening ismim Anvar")