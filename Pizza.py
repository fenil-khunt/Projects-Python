#Find the reduce of pizza and reduce of one piece of pizza

[print("Find the reduce of pizza and reduce of one piece of pizza we need some information from you ...")]
new=("-----------------------------------------------------------------------------------------------")

print(colored(new, 'red'))

r = int(input("Enter reduce of pizza = "))
a = (r**2)*3.14
print("The area of pizza is =>", a)

print(colored(new, 'red'))

t = int(input( "Howmany pieces you you want to make = "  ))
na = a/t
print("The area of one piece is =>",na)

print(colored(new, 'red'))
