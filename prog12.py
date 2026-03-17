#Write a program to whether number prime or not
# Roll Number : 92400527154 : Name : Aarchi Nakum

n=int(input("enter Number : "))

flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break
if flag==1:
    print("Not prime")
else:
    print("prime")
    

