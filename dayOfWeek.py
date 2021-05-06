cero = "sunday"
one = "monday"
two = "tuesday"
three = "wednesday"
four = "thursday"
five = "friday"
six = "saturday"
work = "Go to work."

print("Choose a value 0-6.")
answer = input("Enter value: ")

if answer == "0" or "zero":
    print("Today is %s. Blessings." % (cero))
elif answer == "1" or "one":
    print("Today is %s. %s." % (one, work))
elif answer == "2" or "two":
    print("Today is %s. %s." % (two, work))
elif answer == "3" or "three":
    print("Today is %s. %s." % (three, work))
elif answer == "4" or "four":
    print("Today is %s. %s." % (four, work))
elif answer == "5" or "five": 
    print("Today is %s. %s." % (five, work))
elif answer == "6" or "six":
    print("weekendVibes." % (six))
else:
    print("You\'re so clever -_-.")