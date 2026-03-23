#Write a program to read any text file line by line.  
# Roll Number : 92400527154 : Name : Aarchi Nakum


filename = input("enter the file name: ")

with open(filename, "r") as file:
    for line in file:
        print(line,end="")
