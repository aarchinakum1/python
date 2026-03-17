#Write a program to  prime number 1 to 100
# Roll Number : 92400527154 : Name : Aarchi Nakum

for num in range(2,101):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
            print(num,end= " ")
