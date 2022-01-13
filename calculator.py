def addition(x , y):
 return x + y

def subtract(x , y):
 return x - y

def multiply(x , y):
 return x * y

def division(x , y):
 return x / y


# print("select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiply")
print("4.Division")
choice =int(input("Enter choice(1/2/3/4): "))

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
  
if choice == 1:
    print(x, "+", y, "=",
                    addition(x, y))
  
elif choice == 2:
    print(x, "-", y, "=",
                    subtract(x, y))
  
elif choice == 3:
    print(x, "*", y, "=",
                    multiply(x, y))
  
elif choice == 4:
    print(x, "/", y, "=",
                    division(x, y))
else:
    print("Invalid input")    