# To take input from the user
inp = int(input("Enter a number: "))

ans = False

if inp > 1:
    for i in range(2, int((inp**(1/2)+1))):
        if (inp % i) == 0:
            ans = True
            break

if ans == True:
    print(inp, "is not a prime number")
else:
    print(inp, "is a prime number")