"""STRING"""


shahar = "Қўқон"
viloyat = 'Фарғона'

matn = "Men yangi 📱 oldim"
print(matn)

#STRING USTIDA AMALLAR

ism = 'Ahmad'
print("Mening ismim " + ism)

ism = 'Ahad'
familiya = 'Qayum'
print(ism + familiya)

ism = 'Ahad'
familiya = 'Qayum'
print(ism + ' ' + familiya) # ikki o'zgaruvchi orasiga bo'sh joy qo'shamiz

#f-string


ism = "Ahad"
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)

ism = "James"
familiya = 'Bond'
print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")

#Mahsus belgilar

print('Hello World!')
print('Hello \tWorld!')
print('Hello \nWorld!')



"""STRING METODLARI"""


#upper() va lower() metodlari

ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper())

ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.lower())

#title() va capitalize() metodlari

ism_sharif = 'james bond'
print(ism_sharif.capitalize())

print('james bond'.upper())

#strip(), rstrip() va lstrip() metodlari

meva = "     olma     "
print("Men " + meva.lstrip() + " yaxshi ko'raman")
print("Men " + meva.rstrip() + " yaxshi ko'raman")
print("Men " + meva.strip() + " yaxshi ko'raman")
print("Men " + meva + " yaxshi ko'raman")

#INPUT —FOYDALANUVCHI BILAN MULOQOT


ism = input("Ismingiz nima?")
print("Assalom alaykum, " + ism)

ism = input("Ismingiz nima?\n>>>") # Foydalanuvchi ismini yangi qatordan kiritadi
print("Assalom alaykum, " + ism.title())

