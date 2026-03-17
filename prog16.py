#Write a program to add square roots number.
# Roll Number : 92400527154 : Name : Aarchi Nakum
n = int(input("Enter a number: "))


square_list = []

for i in range(1, n + 1):
    square_list.append(i * i)


print("squares: ", square_list)
