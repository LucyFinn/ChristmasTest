#Computer Science Summer Exam
#Lucy Finn
#Task 2

print("Hello welcome to Finn's Taxi Company!")

travel = int(input("How many kilometers will you be travelling today? ")) #1. asking how far the person is going to be travelling

#2. asking how many people travelling and not allowing more than 4 
passengers = int(input("How many people will be travelling today? ")) 
if passengers > 4:
    print("Sorry the maximum people allowed to travel is 4!")
    
#3. Calculating the Taxi Fare!
print("")
costT = travel * 0.78
print("Cost for travel:" ,costT,"euros" )

costP = passengers * 2.50
print("Cost for passengers:" ,costP,"euros" )

print("")
total =  costT + costP
print("Your total is:", total,"euros")
