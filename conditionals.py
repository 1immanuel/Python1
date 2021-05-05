import random

num = int(input("What\'s your favorite numer: "))
number = 87

if num >= 0:
    print("Thats high.")
elif num < 50:
        print("Think bigger.")
else:
        print(num + number + random.randint(0,100))