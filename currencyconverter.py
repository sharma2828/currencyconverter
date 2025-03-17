with open("currencydata.txt.txt") as f:
    lines=f.readlines()
    print(lines)   #FOR UNDERSTANDING
dict={}
for line in lines:
    x=line.split("\t")
    print(x)   #FOR UNDERSTANDING
    dict[x[0]]=x[1]
    print(dict) #FOR UNDERSTANDING
amount=float(input("ENTER AMOUNT IN INDIAN RUPEES: "))
print("ENTER THE CURRENCY YOU WANT TO CONVERT THIS AMOUNT TO ? AVAILABLE OPTION:\n")
for y in dict.keys():
    print(y)
z=input("ENTER ONE OF THESE CURRENCIES: ")
print(f"{amount} INR IS EQUAL TO {amount*float(dict[z])} {z}")