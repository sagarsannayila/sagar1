# from __future__ import print_function
# b=int(input("enter the number:"))
# # print(*range(1, b +  1), sep="") 
# c=[] 
# for i in xrange (1,b+1):
# 	c.append(i)
# print(c)
# class Myclass():
# 	__a=20
# 	def __init__(self,b,c):
# 		self.__b=b
# 		self.__c=c
# o=Myclass(23,45)
# print(o._Myclass__a)
# print(o._Myclass__b)
# print(o._Myclass__c)
# # print(dir(o))
# class Gmail():
# 	__username="nag"
# 	__password="nag"
# 	def myclass(self,username,password):
# 		self.__username=username and self.__password=password
# 		return "this is my class"
class Employee:
	def __init__ (self, first, last, pay):
		self.first = first
		self.last=last
		self.pay= pay
		self.gmail = first+last+'@gmail.com'
emp = Employee('sagarsannayila','72',678)
emp_2 = Employee('python','sql',789)
print(emp)
print(emp_2)
print(emp.gmail)




        