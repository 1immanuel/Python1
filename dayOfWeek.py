cero = "sunday"
one = "monday"
two = "tuesday"
three = "wednesday"
four = "thursday"
five = "friday"
six = "saturday"
work = "Go to work."

print("Choose a value 0-6.")
answer = int(input("Enter value: "))

if answer == 0:
    print("Today is %s. Blessings." % (cero))
elif answer == 1:
    print("Today is %s. %s." % (one, work))
elif answer == 2:
    print("Today is %s. %s." % (two, work))
elif answer == 3:
    print("Today is %s. %s." % (three, work))
elif answer == 4:
    print("Today is %s. %s." % (four, work))
elif answer == 5: 
    print("Today is %s. %s." % (five, work))
elif answer == 6:
    print("weekendVibes." % (six))
else:
    print("You\'re so clever -_-.")