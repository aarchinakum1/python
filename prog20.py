#Write a program read names from keyboard.
# Roll Number : 92400527154 : Name : Aarchi Nakum

# open a file in write mode
file = open("names.txt", "w")

# ask how many names to enter
n = int(input("How many names do you wnat to enter? "))

# Loop to take input
for i in range(n):
    name = input("enter name:")
    file.write(name + "\n") #write  name into file

#close the file
file.close()

print("names saved successfully!")    
