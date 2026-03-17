#Write a program to print input of marks subject
#Roll Number : 92400527154 : Name : Aarchi Nakum
mu1 = int(input("Enter marks of subject 1:"))
mu2 = int(input("Enter marks of subject 2:"))
mu3 = int(input("Enter marks of subject 3:"))
mu4 = int(input("Enter marks of subject 4:"))

total = m1 + m2 + m3 + m4
percentage = total / 4

if m1 < 40 or m2 < 40 or m3 < 40 or m4 < 40:
    result = "FAIL"
    grade = "No Grade"

else:
    result = "PASS"
    if percentage >=75:
        grade = "A"
    elif percentage >=60:
        grade = "B"
    elif percentage >=50:
        grade = "C"
    elif percentage >=40:
        grade = "D"

   print("Total:", total)
   print("Percentage:", percentage)
   print("Result:", result)
   print("Grade:", grade)
        
        
