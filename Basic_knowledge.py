#task1
def filter_list(my_list):
 new_list = []
 for i in my_list:
    if type(i) is int:
      new_list.append(i)
 return new_list

#task2
def first_non_repeating_letter(s):
    for i in range(len(s)):
        count = 0
        for j in range(len(s)):
            if s[i] == s[j] or s[i] == s[j].lower() or s[i] == s[j].upper():
                count = count + 1
        if count == 1:
           return(s[i])
           break
    return "Nore"
#task3
def sum_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
def Digital_root(n):
    while n>9:
        n=sum_digit(n)
    return n
#task4
import numpy as np
def findp(my_array,p):
    i = 0
    lst = []
    while i < len(my_array):
        j = i + 1
        while j < len(my_array):
            if my_array[i] + my_array[j] == p:
                lst.append([my_array[i], my_array[j]])
            j += 1
        i += 1
    fset = set(frozenset(x) for x in lst)
    lst = [list(x) for x in fset]
    return lst
#task5
def transformation(s):
    s = s.upper()
    d = list([i for i in kv.split(':')] for kv in s.split(";"))
    sort_d = sorted(d, key=lambda d: (d[1], d[0]))
    return sort_d
#task6
def func(n):
    lst = [int(i) for i in str(n)]
    if (len(lst) == 1) or (len(set(lst)) == 1):
        return -1
    else:
        lst1 = lst
        pos = len(lst) - 1
        pos_lst = len(lst) - 2
        temp = 0
        t = 0
        while (pos > 0) and (temp == 0):
            while pos_lst >= 0:
                if lst[pos_lst] < lst[pos]:
                    lst[pos_lst], lst[pos] = lst[pos], lst[pos_lst]
                    temp = 1
                    break
                if lst[pos_lst] == lst[pos]:
                    pos -= 1
                    t = 1
                pos_lst -= 1
            if (t == 0):
                pos -= 1
            else:
                t = 0
            pos_lst = pos - 1

    if temp==1:

        return int("".join(str(x) for x in lst))
    else:
        return -1
#task7
def convert(i):
    st = str(bin(i + 2 ** 32)[-32:])
    st1 = st[:8]
    st2 = st[8:16]
    st3 = st[16:24]
    st4 = st[24:]
    s = str(int(st1, 2)) + "." + str(int(st2, 2)) + "." + str(int(st3, 2)) + "." + str(int(st4, 2))
    return s

print("Task 1")
print(filter_list([1,0,"fin","434",5,2]))
print(filter_list([1,2,'aasf','1','123',123]))
print("Task 2")
print(first_non_repeating_letter("rtetridg"))
print(first_non_repeating_letter("stress"))
print(first_non_repeating_letter("sTreSS"))
print(first_non_repeating_letter("dfgSSdFG"))
print("Task 3")
print(Digital_root(493193))
print(Digital_root(16))
print(Digital_root(942))
print(Digital_root(132189))
print("Task 4")
my_array = np.array([1, 3, 6, 2, 2, 0, 4, 5,-1])
p = 5
print(findp(my_array,p))
print("Task 5")
s = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Alfred:Tornbull;Raphael:Corwill;Alfred:Corwill"
sort_d=transformation(s)
for i in sort_d:
    print(f'({i[1]},{i[0]})')
print("Task 6(додаткове 1)")
a=[232,5435,1354,3300032,4534,243043,111103,11111110,1000000,10,0,11,531,987654321,123456789]
for i in a:
 print(i," --> ",func(i))
 print("Task 7(додаткове 22)")
 print(convert(2149583361))
 print(convert(32))
 print(convert(0))
