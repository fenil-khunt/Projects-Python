#Takking input from user 
x = input("Please enter any two word = ")
inp = x.lower()

#Adding error
string = inp.split(" ")
lenos = len(string)
if ((lenos) > 2):
    
  print("Plz check your input it must me 2 words only ")
  print("Try again")
else:
    print("Your answer is :",end = " ")

#Spliting frist and last words from string
    fristW = inp.split(" ")[0]
    lastW = inp.split(" ")[1]

#Splitting character excluding frist and last character
    c1 = fristW[:-1]
    d1 = lastW[:-1]

#Splitting last characters from each string 
    c2 = fristW[-1]
    d2 = lastW[-1]

#Printing output
    print(d1+d2.upper()+" "+c1+c2.upper())
    print("Thank you !!!")