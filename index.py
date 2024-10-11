texts=input("Ixtiyoriy matn kiriting: ")
print(len(texts))


numbers=list(range(1,50))
for number in range(1,50):
    if number%3 ==0:
        print("fiz")
    if number %5==0:
        print("buz")
    if number%3==0 and number%5==0:
        print("fizbuz")

