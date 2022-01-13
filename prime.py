# num =8

# number =int(input("Enter the number: "))
num =9
flag =False
if num>1 :
    for i in range(2,num):
        if (num % i) ==0:
            flag =True
            break
if flag :
    print (num,"isnot a prime number")
else:
    print(num,"it is a prime number")


