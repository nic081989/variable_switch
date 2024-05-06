


python
Copy code
# Author: Nicholas Ngobi

# Prompt the user to input values for variables a and b
a = input("Enter the value for variable a:\n")
b = input("Enter the value for variable b:\n")

# Temporary variable to facilitate swapping
temp = a  # Store the value of a in temp
a = b     # Assign the value of b to a
b = temp  # Assign the value stored in temp (initial value of a) to b

# Print the result after swapping
print("After swapping:")
print("a  = ", a)  # Print the value of a after swapping
print("b  = ", b)  # Print the value of b after swapping
