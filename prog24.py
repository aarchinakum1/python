#write a program  that creates a class with function overloading.
# Roll Number : 92400527154 : Name : Aarchi Nakum

class Calculator:
    def addition(self,*args):
        return sum(args)

c=Calculator()
print(c.addition(5))
print(c.addition(5,10))
print(c.addition(5,10,15))
print(c.addition(5,10,15,20))



