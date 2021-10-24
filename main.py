def convert(i):
     st=str(bin(i+2**32)[-32:])
     st1 = st[:8]
     st2 = st[8:16]
     st3 = st[16:24]
     st4 = st[24:]
     s = str(int(st1, 2)) + "." + str(int(st2, 2)) + "." + str(int(st3, 2)) + "." + str(int(st4, 2))
     return s
print(convert(2149583361))
print(convert(32))
print(convert(0))