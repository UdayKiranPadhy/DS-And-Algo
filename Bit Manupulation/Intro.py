# Important for interview perpespective only not asked in coding exams because
# these are Gun shot questions and need to be implemented in O(1) time so
# Every one just hard memorize it . Remember these are O(1) time .

a = 10
print(bin(a).lstrip("0b"))
# print(~a) #-11
"""
Bitwise Not returns like this
~10
-(1010 +1)
-11
"""
print(a & 9)  # 8
# 1010
# 1001


# print(a << 1)  # 10100 20
# print(a << 2)  # 101000 40
# print(a >> 1)  # 101 5a

# Binary to decimal
# int('11111111', 2)
# 255

# If we right shift a number n by 1 it will be eqaul to n/2
# 1010 -10
# 0101 - 5
