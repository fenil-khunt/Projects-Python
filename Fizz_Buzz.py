inp = int(input("Enter any number => "))

if inp == 0:
    print(f"There is no output for {inp}.")
elif inp%3==0 and inp%5==0:
    print("Fizz Buzz")
elif inp%3 == 0:
    print("Fizz",end=" ")
elif inp%5 == 0:
    print("Buzz")
else:
    print(f"There is no output for {inp}.")