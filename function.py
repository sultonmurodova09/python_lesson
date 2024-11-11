"""FUNKSIYA YARATAMIZ"""

def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum!")
    
#FUNKSIYAGA QIYMAT UZATISH

def salom_ber(ism):
    """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")
#Mana endi fuknsiyamiz foydalanuvchidan ism degan qiymatni ham kutadi.

salom_ber('hasan')
#Natija: Assalomu alaykum, hurmatli Hasan!

#Agar funksiyaga murojat qilishda, unga qiymat bermasak xatolik vujudga keladi:

salom_ber()
#Natija: TypeError: salom_ber() missing 1 required positional argument: 'ism'

#DOCSTRING

def salom_ber(ism):
    """Fodyalanuvchi ismini qabul qilib, 
        unga salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")
    
#FUNKSIYAGA BIR NECHA BOR MUROJAT QILISH

def salom_ber(ism):
    """Fodyalanuvchi ismini qabul qilib, 
        unga salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")
    
salom_ber('hasan')
salom_ber('olim')

#ARGUMENT VA PARAMETER

# Funksiya yaratishda, qavs ichida berilgan, funksiya to'g'ri ishlashi uchun uzatiladigan qiymat parameter deb ataladi. 
# Yuqoridagi misolda ism bu salom_ber funksiyasining parametri. 

# Foydalanuvchi funksiyaga murojat qilishda funksiyaga uzatgan qiymat esa argument deb ataladi.
# salom_ber('hasan') kodida 'hasan' bu argument. 

"""FUNKSIYAGA BIR NECHTA ARGUMENT UZATISH"""

#TO'G'RI TARTIBDA UZATISH

def toliq_ism(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")
    
toliq_ism('olim','hakimov')

#Agar argumentlarni noto'g'ri ketma-ketlikda bersak, natija ham biz kutganday chiqmaydi:

toliq_ism('hakimov','olim')


def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {2020-tugilgan_yil} yoshda")
    
yosh_hisobla('olim', 1997)

#Ko'p xolatlarda esa, argumentlarni noto'g'ri tartibda uzatish xatolikka ham olib kelishi mumkin.

def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {2020-tugilgan_yil} yoshda")

yosh_hisobla(1997, 'olim')

#KALIT SO'Z BILAN UZATISH

def yosh_hisobla(tugilgan_yil=1997, ism='olim'):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {2020-tugilgan_yil} yoshda")
    
#Huddi shu kabi yuqoridagi toliq_ism funksiyasiga murojat qilishimiz mumkin:

def toliq_ism(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")
toliq_ism(familiya='hakimov',ism='olim')

#STANDART QIYMAT

def yosh_hisobla(tugilgan_yil, joriy_yil=2020): # joriy yil uchun st.qiymat 2020
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
# Keling avval funksiyani ikkala argument bilan chaqiramiz:

yosh_hisobla(1995,2020)

# Endi esa faqat bitta argument (tugilgan_yil) bilan chaqiramiz:

yosh_hisobla(1993)

# FUNKSIYAGA MUROJAT QILISHDA XATOLIKLAR

def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
    
    
tyil = input("Tug'ilgan yilingizni kiriting: ")
yosh_hisobla(tyil)
# Natija: TypeError: unsupported operand type(s) for -: 'int' and 'str'



def yosh_hisobla(tugilgan_yil, joriy_yil):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

yosh_hisobla(1993)
# Natija: TypeError: yosh_hisobla() missing 1 required positional argument: 'joriy_yil'



def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum!")

salom_ber('hasan')
# Natija: TypeError: salom_ber() takes 0 positional arguments but 1 was given


def toliq_ism(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")
 
toliq_ism('olim hakimov')
# Natija: TypeError: toliq_ism() missing 1 required positional argument: 'familiya'
