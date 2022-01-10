total=int(input("expense"))
paid=int(input("Paid"))


amount = paid - total

#1,2,5,10,20,50,100,500,1000

while (amount>0):
 if(amount>=1000):
   print("1000") 
   amount -=1000

    
 elif ( amount>=500):
  print("500")
  amount -=500
        
 elif(amount>=100):
  print("100")
  amount -=100


 elif(amount>=50):
  print("50")
  amount -=50
        
 elif(amount>=20):
  print("20")
  amount -=20
        
 elif(amount>=10):
  print("10")
  amount -=10

 elif(amount>=5):
  print("5")
  amount -=5
        
 elif (amount>=2):
  print("2")
  amount -=2
        
 elif (amount>=1):
  print("1")
  amount -=1


