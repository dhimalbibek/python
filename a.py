def add (a , b):
 return a + b

def sub(a,b):
 return(a-b)

def mul( a , b ):
 return a*b

def div(a,b):
 return(a/b)

print(" select Operations .")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")

number =int(input("Enter number(1/2/3/4): "))

a=int(input("Enter the 1st number"))
b=int(input("Enter the 2nd number"))

if number == 1:
 print (a,"+", b, "=", add(a,b))




