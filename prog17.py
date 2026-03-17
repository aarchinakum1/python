#Write a program to add square roots number dictionary.
# Roll Number : 92400527154 : Name : Aarchi Nakum
n = int(input("Enter a number: "))


square_dict = {}

for i in range(1, n + 1):
    square_dict[i] = (i * i )


print("squares: ", square_dict)

