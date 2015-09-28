# """
# struct { double v; int t; char c;};
# """
# from ctypes import *

# class YourStruct(Structure):
#     _fields_ = [('v', c_double),
#                 ('t', c_int),
#                 ('c', c_char)]

# with open('c_structs.bin', 'rb') as file:
#     result = []
#     x = YourStruct()
#     while file.readinto(x) == sizeof(x):
#         result.append((x.v, x.t, x.c))

# print(result)

"""
struct { double v; int t; char c;};
"""
from struct import Struct

x = Struct('dicxxx')
with open('c_structs.bin', 'rb') as file:
    result = []
    while True:
        buf = file.read(x.size)
        if len(buf) != x.size:
            break
        result.append(x.unpack_from(buf))

print(result)