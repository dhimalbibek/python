english =int(input("Enter marks of English"))
math =int(input("Enter marks of Math"))
nepali =int(input("Enter marks of Nepali"))
science =int(input("Enter marks of Science"))
elements =int(input("Enter marks of Elements"))

total =english+math+nepali+science+elements
per = (total/100)*500

if per>=80 :
    print("A+")

elif per>=60 :
    print("A") 

elif per>=50:
    print("B+")



