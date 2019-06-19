"""
d 	Signed integer decimal.
i 	Signed integer decimal.
o 	Unsigned octal.
u 	Obsolete and equivalent to 'd', i.e. signed integer decimal.
x 	Unsigned hexadecimal (lowercase).
X 	Unsigned hexadecimal (uppercase).
e 	Floating point exponential format (lowercase).
E 	Floating point exponential format (uppercase).
f 	Floating point decimal format.
F 	Floating point decimal format.
g 	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.
G 	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.
c 	Single character (accepts integer or single character string).
r 	String (converts any python object using repr()).
s 	String (converts any python object using str()).
% 	No argument is converted, results in a "%" character in the result.
"""
print("Art: %5d, Price: %8.2f" % (453, 59.087))
print("%10.3e"% (356.08977))
print("%10.3E"% (356.08977))
print("%10o"% (25))
print("%10.3o"% (25))
print("%10.5o"% (25))
print("%5x"% (47))
print("%5.4x"% (47))
print("%5.4X"% (47))
print("Only one percentage sign: %% " % ())


"""
# 	Used with o, x or X specifiers the value is preceded with 0, 0o, 0O, 0x or 0X respectively.
0 	The conversion result will be zero padded for numeric values.
- 	The converted value is left adjusted
  	If no sign (minus sign e.g.) is going to be written, a blank space is inserted before the value.
+ 	A sign character ("+" or "-") will precede the conversion (overrides a "space" flag).
"""
print("%#5X"% (47))
print("%5X"% (47))
print("%#5.4X"% (47))
print("%#5o"% (25))
print("% d"% (42))
print("%2d"% (42))


print("Art: {a:5d},  Price: {b:8.2f}".format(a=453, b=59.058))
