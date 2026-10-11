Year=int(input("Enter your birth year:"))
Zodiac=["Monkey","Rooster","Dog","Pig","Rat","Ox","Tiger","Rabbit","Dragon","Snake","Horse","Goat"]

if Year > 0:
    print("Your Chinese Zodiac is:",Zodiac[Year % 12])
else:
    print("Invalid year")