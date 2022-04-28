starting_range = int(input("Enter Starting Range : "))
ending_range = int(input("Enter Ending Range : "))
M_num = int(input("Enter Number which multiple list you want : "))
E_num = int(input("Enter Number which multiples you want to remove from the list : "))


M_list = []  
print(f"The list of multiple from the given range ({starting_range},{ending_range}) is :" ,end = " ")
for i in range(starting_range, (ending_range)+1):
    if i % M_num == 0:  
        M_list.append(i)
    i += 1

print(M_list)


E_list = []
print(f"The list exclude multiple from the given range ({starting_range},{ending_range}) is :" ,end = " ")
for i in range(starting_range, (ending_range)+1):
    if i % E_num != 0:
        E_list.append(i) 
    i += 1
    
print(E_list)