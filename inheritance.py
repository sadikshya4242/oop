# inheritance inherit method and properties from another class
# syntax : class classname(baseclass)

# class student:
#     def st(self):
#         print("i am student")
#         return "hello"
# class course(student):
#     def cou(self):
#         print("this is a course")
# c=course()
# print(c.st())



# Multiple inheritance
class A:
    def m1(self):
        print("I am from class A")
class B(A):
    def m2(self):
        print("I am from class b")
    def m1(self):
        print("i am from class b")
class C(B):
    def m3(self):
        print("I am from class c")

# c=C()
# c.m1()
# Multi level inheritance
class A:
    def m1(self):
        print("I am from class A")
class B():
    def m2(self):
        print("I am from class b")
    def m1(self):
        print("I am from class B")

class C(B,A):
    def m3(self):
        print("I am from class c")
    def m1(self):
        print("I am from class c")
c=C()
c.m1()

# MRO= Method resolution order (If we call have same function in two different class it give priority to order of inheritance)


