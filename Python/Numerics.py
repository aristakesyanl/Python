import sys
import math

# There are three distinct numeric types integers, floating point numbers and complex numbers
# booleans are subtypes of integers
# Integers have unlimited precision
# Floating point numbers are usually implemented using double in C

# get information about floating point numbers
print(sys.float_info)

# Complex numbers have real and imaginary parts which are floating point number
x = 2.3
y = -6.1
z = complex(x, y)
print(z)

# To get real and imaginary parts use z.real and z.imag
print(z.real, z.imag)

# Python fully supports mixed arithmetic
# Constructor int(), float() and complex() can be used to produce numbers of specific types

x = int(x)
print(x)

# All numeric types(except complex) support following operations
# x + y addition
# x - y subtraction
# x / y division
# x // y floor division
# x * y multiplication
# x % y remainder of x//y
# -x
# +x
# abs(x)
# int(x)
# z = complex(x, y)
# z.conjugate()
# divmod(x,y) pair(x//y, x%y)
# pow(x,y) x to power y
# x**y x to power y

# Rounding methods
x = -3.264125
print(math.trunc(x)) # to the integral
print(round(x, 3)) # rounding first n digits
print(math.floor(x)) #<=x
print(math.ceil(x)) #>=x

# Bitwise operations
x = 6
y = 14
n = 2

# x | y or
# x ^ y exclusive or
# x & y and
# x << n left shift by n digits =multiply by 2**n
# x >> n right shift by n digits = floor division by 2**n
# ~x bits are inverted

# Additional methods on integers


n = -37
print(bin(n))
print(n.bit_length())
# Return an array of bytes representing an integer.
# To know native byteorder
print(sys.byteorder)
n = 1024
print(n.to_bytes(2, byteorder='big', signed=False))
n = -1024
print(n.to_bytes(2, byteorder='big', signed=True))
print(n.to_bytes(2, byteorder='little', signed=True))
# int.from_bytes()
print(int.from_bytes(b'\x00\x10', byteorder='big'))

x = 10
# Always returns number as a numerator and 1 as a denominator in case of integers
numerator, denominator = x.as_integer_ratio()
print(numerator, denominator)

# Additional methods on floats

x = 3.26
numerator, denominator = x.as_integer_ratio()
print(numerator, denominator)
print(x.is_integer())
print(x.hex())
print(float.fromhex('0x3.a7p10'))
print(float.fromhex('-0x3da.a7p10'))


