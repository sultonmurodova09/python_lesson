"""RO'YXATNI TARTIBLASH"""

cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort()
print(cars)

cars = ['Bmw','mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
cars.sort()
print(cars)
# Yuqoridagi misolda 'Bmw' elementi katta harf bilan boshlangani uchun ro'yxatning boshidan joy oldi.

# .sort() metodi ichida reverse=True argumenti

cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort(reverse=True)
print(cars)

# sorted() funktsiyasi

mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)

# sorted() funktsiyasi yordamida teskari tartiblash uchun ham  reverse=True
#  argumentini ishlatishimiz mumkin

ages = [12, 98, 34, 65, 34, 76, 11]
ages.sort()
print(ages)
print(sorted(ages, reverse=True))

# RO'YXATNI AYLANTIRISH

fruits = ['pear','banana','apple','watermelon','lemon']
fruits.reverse()
print(fruits)

# RO'YXATNING UZUNLIGINI BILISH

fruits = ['pear','banana','apple','watermelon','lemon']
print("Elementlar soni:",len(fruits)) # len(fruits) ro'yxat uzunligini qaytaradi

# range() FUNKTSIYASI

sonlar = list(range(0,10)) # 
print(sonlar)

# range() yordamida qadamni ham berishimiz mumkin

juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
print("Juft sonlar: ", juft_sonlar)
print("Toq sonlar: ", toq_sonlar)

# SONLI RO'YXAT USTIDA SODDA AMALLAR

narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
arzon = min(narhlar)
qimmat = max(narhlar)
jami = sum(narhlar)
print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)

# RO'YXATNI KESISH

cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
print(my_cars) 

# Bu usul bilan ro'yxatning istalgan joyidan bo'lishimiz mumkin:

print(cars[2:5]) # 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)

# Agar boshlang'ich indeksni bermasangiz, Python avtomat ravishda 0 indeksdan boshlab kesadi.
#  Agar 2-indeksni kiritmasangiz, ro'yxat oxirigacha kesadi

print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

# RO'YXATDAN NUSXA OLISH

sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
print("Bu sonlar ro'yxati:", sonlar)
print("Bu sonlar2 ro'yxati:", sonlar2)

# TUPLES - O'ZGARMAS RO'YXAT

tomonlar = (20, 30, 55.2)
print(tomonlar)

# Tuple ichidagi elementlarga huddi ro'yxat elementlariga murojat qilingani kabi murojat qilinaveradi


toys = ('bus','car','bear','dino','snake','lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])

# o'zgarmas ro'yxatni o'zgartirish kodi

toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# Ro'yxatga o'zgartirishlar kiritamiz
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
print(toys)


