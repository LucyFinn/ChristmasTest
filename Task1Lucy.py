#Computer Science Summer Exam
#Lucy Finn
#Task 1

students = [45, 97, 9, 10, 8, 85, 64, 56, 1, 4, 25, 36, 78] #1. creating a list
print("These are the student grades:", students) #2. printing out the list

#3. getting the lenght of the list
print("There are", len(students), "student grades in the list")

#Sorting the list into smallest to largest
print("") #using these to break up the code to make it easier to read
list.sort(students)
print("The sorted list:", students)

#4.adding in a loop
for i in range(4):
    students.pop(0)
print("This is the list with the correct grades:" ,students)

#5. adding in a new grade 6.appending it to the list
print("")
newGrade = int(input("Please enter the grade for the new student: "))
students.append(newGrade)
print("This is the list with the added grade:" ,students)

#7.putting the list in decending order and printing that out
print("")
list.reverse(students)
print("Grades from highest to lowest:" ,students)

#8.finding the mean of the list
print("")
total = sum(students)
average = total // len(students)
print("The mean of the grades is:" ,average)

#9.highest value
print("")
highest = students[0]
print("The highest grade is:" ,highest)

#10.lowest value
lowest = students[-1]
print("The lowest value is:" ,lowest)
