# Sodda lug'at

car_0 = {'model':'ferrari','rang':'qizil'}

car_0 = {'model':'ferrari','rang':'qizil'}
print(car_0['model'])

#Lug'atdagi qiymatlar son (int, float), matn (string), ro'yxat (list, tuple) va
#  hatto boshqa lug'at ham bo'lishi mumkin.


talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
print(f"{talaba_0['ism'].title()},\
 {talaba_0['t_yil']}-yilda tu'gilgan,\
 {talaba_0['yosh']} yoshda")

#YANGI JUFTLIK QO'SHISH

talaba_0['kurs'] = 4 # yangi, 'kurs' nomli kalit so'zga 4 qiymatini yuklaymiz
talaba_0['fakultet'] = 'informatika' # 'fakultet' ga esa 'informatika' 

# BO'SH LUG'AT

talaba_1 = {}
talaba_1['ism'] = 'qobil rasulov'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 20
print(talaba_1)
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

#QIYMATNI O'ZGARTIRISH

talaba_1['kurs'] = 4 # 'kurs' ni 4 ga o'zgartiramiz.
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

#KALIT SO'Z-QIYMAT JUFTLIGINI O'CHIRISH

talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
print(talaba_0)
del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
print(talaba_0)

#LUG'ATNI QATORLARGA BO'LIB YOZISH

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

#get() METODI

phone = telefonlar['ali']
print(f"Alining telefoni {phone}")

phone = telefonlar['hasan']
print(f"Hasanning telefoni {phone}")

phone = telefonlar.get('hasan','Bunday ism mavjud emas')

phone = telefonlar.get('hasan')
print(phone)

