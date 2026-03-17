#Write a program to print interest
# Roll Number : 92400527154 : Name : Aarchi Nakum
p = float(input("Enter Amount: "))
r = float(input("Enter Rate : "))
t = float(input("Enter Time : "))


ci = p * (1 + r / 100) ** t - p


print("Compound Interest is:", ci)
