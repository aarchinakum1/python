#Write a program numbers with total and average at the last.
# Roll Number : 92400527154 : Name : Aarchi Nakum

with open("number.txt","r") as file:
    total = 0
    count = 0
    
    print("Numbers in file:")

    for line in file:
        num = int(line.strip())
        print(num)
        total += num
        conut += 1
average = total / count

print(total)
print(avg)


