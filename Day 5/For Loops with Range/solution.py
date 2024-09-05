#if number is divisible by 3 print Fizz by 5 Fuzz and by both FizzFuzz
#all between 1-100

for number in range (1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzFuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Fuzz")
    else:
        print(number)