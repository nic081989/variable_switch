12# Author: Nicholas Ngobi
# This program switches the value stored in the variables a and b
a = input("Enter the value for variable a:\n")
b = input("Enter the value for variable b:\n")
# print("a")
# print("b")
#create a temporary variable to help in swapping
temp =a 
a=b
b =temp
print("after swapping")
print("a  = ", a)
print("b  = ", b)