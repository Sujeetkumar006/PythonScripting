#Types of Operator: Python language supports the following types of operators −
"""
Arithmetic Operators
Comparison (Relational) Operators
Assignment Operators
Logical Operators
Bitwise Operators
Membership Operators
Identity Operators """

## 
a=10
b=3
a=10
b=3
print(a+b)
print(a+b)
print(a*b)
print(a/b) #Divides left hand operand by right hand operand, result will always be float
print(a%b) #Divides left hand operand by right hand operand and returns remainder
print(a**b) #Performs exponential (power) calculation on operators
print(9//2,9.0//2.0,-11//3)#Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity):


####
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)


#####
#Bitwise operator works on bits and performs bit-by-bit operation. Assume if a = 60; and b = 13; Now in binary format they will be as follows −
a = 0011 1100
b = 0000 1101
print(a&b)# Binary AND	Operator copies a bit, to the result, if it exists in both operands	(a & b) (means 0000 1100)
print(a|b)# Binary OR	It copies a bit, if it exists in either operand.	(a | b) = 61 (means 0011 1101)
print(a^b)# Binary XOR	It copies the bit, if it is set in one operand but not both.	(a ^ b) = 49 (means 0011 0001)
print(a~b)# Binary Ones Complement	It is unary and has the effect of 'flipping' bits.	(~a ) = -61 (means 1100 0011 in 2's complement form due to a signed binary number.
print(a<<b)# Binary Left Shift	The left operand's value is moved left by the number of bits specified by the right operand.	a << 2 = 240 (means 1111 0000)
print(a>>b)# Binary Right Shift	The left operand's value is moved right by the number of bits specified by the right operand.	a >> 2 = 15 (means 0000 1111)



#### Logical operator
a=True
b=False
print(a and b)#Logical AND	If both the operands are true then condition becomes true.	(a and b) is False
print(a or b)#Logical OR	If any of the two operands are non-zero then condition becomes true.	(a or b) is True
print(not(a and b))# Logical NOT	Used to reverse the logical state of its operand.	Not(a and b) 
 
## MEmbership
in 
not in

## Identity.
is
is not

 
 