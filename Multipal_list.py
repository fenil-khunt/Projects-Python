inp1 = int(input("enter inp 1 : "))
inp2 = int(input("enter inp 2 : "))
M_num = int(input("Enter Number which multiple you want to find: "))


M_list = []  
print(f"The list of multiple from the given range ({inp1},{inp2}) is :" ,end = " ")
for i in range(inp1, (inp2)+1):
    if i % M_num == 0:  
        M_list.append(i)
    i += 1

print(M_list)


E_list = []
print(f"The list exclude multiple from the given range ({inp1},{inp2}) is :" ,end = " ")
for i in range(inp1, (inp2)+1):
    if i % M_num != 0:
        E_list.append(i) 
    i += 1
    
print(E_list)