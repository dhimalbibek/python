total_marks =500

aj = int(input("Enter marks AdvancedJava: "))
mp = int(input("Enter marks MobileProgramming: "))
ap = int(input("Enter marks AppliedEconomics: "))
np = int(input("Enter marks NetworkProgramming: "))
ds = int(input("Enter marks DistributedSystem: "))

total =aj+mp+ap+np+ds

percentage =(total/total_marks)*100

print("-------MARKSHEET------")
print("-----------------------")
# status =("")    
if percentage>=90:
 print("A+")
 
    # status("A+")

elif percentage>=80:
 print("A")
    # status("A")

elif percentage>=70:
 print("B+")
    # status("B+")

elif percentage>=60:
 print("B")
    # status("B")

elif percentage>=50:
 print("C+")
    # status("C+")

elif percentage>=40:
 print("C")
    # status("C")

else :
    print("Failed")

print("-----------------")
print("Good Luck for your future")


