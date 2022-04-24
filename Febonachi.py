n = int(input("Enter the value of n : "))
a = 0
b = 1
sum = 0
count = 1

#Adding errors and loops 
if n == 0 :
    print("Enter the value of n > 0")
    print("Try Again")
else:
    while(count <= n):
        print(sum ,end="  ")
        count += 1
        a = b
        b = sum
        sum = a + b