import numpy as np


# Task №1
def filter_list(my_list):
    new_list = []
    for index in my_list:
        if type(index) is int:
            new_list.append(index)
    return new_list


# Task №2
def first_non_repeatflacing_letter(snt):
    for i in range(len(snt)):
        count = 0
        for j in range(len(snt)):
            if snt[i] == snt[j] or snt[i] == snt[j].lower() \
                    or snt[i] == snt[j].upper():
                count = count + 1
        if count == 1:
            return snt[i]
            break
    return 'Nore'


# Task №3
def sum_digit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


def digital_root(n):
    while n > 9:
        n = sum_digit(n)
    return n


# Task №4
def find_p(my_array, p):
    i = 0
    lst = []
    while i < len(my_array):
        j = i + 1
        while j < len(my_array):
            if my_array[i] + my_array[j] == p:
                lst.append([my_array[i], my_array[j]])
            j += 1
        i += 1
    f_set = set(frozenset(x) for x in lst)
    lst = [list(x) for x in f_set]
    return lst


# Task №5
def transformation(snt):
    snt = snt.upper()
    d = list([i for i in kv.split(':')] for kv in snt.split(";"))
    d_sort = sorted(d, key=lambda d: (d[1], d[0]))
    return d_sort


# Task №6
def find_next(number):
    num = [int(i) for i in str(number)]
    len_num = len(num)
    if len_num == 1:
        return "-1"
    for i in range(len_num - 1, 0, -1):
        if num[i] > num[i - 1]:
            break
    if i == 1 and num[i] <= num[i - 1]:
        return "-1"
    n = num[i - 1]
    pos = i
    for j in range(i + 1, len_num):
        if (num[j] > n) and (num[j] < num[pos]):
            pos = j
    num[pos], num[i - 1] = num[i - 1], num[pos]
    n = 0
    for j in range(i):
        n = n * 10 + num[j]
    num1 = sorted(num[i:])
    for j in range(len_num - i):
        n = n * 10 + num1[j]
    return n


# Task №7
def convert(i):
    st = str(bin(i + 2 ** 32)[-32:])
    st1 = st[:8]
    st2 = st[8:16]
    st3 = st[16:24]
    st4 = st[24:]
    st_v = str(int(st1, 2)) + "." + str(int(st2, 2)) + "." + str(int(st3, 2)) \
                            + "." + str(int(st4, 2))
    return st_v


print("Task №1")
print(filter_list([1, 0, "fin", "434", 5, 2]))
print(filter_list([1, 2, 'aasf', '1', '123', 123]))
print("Task №2")
print(first_non_repeatflacing_letter("rtetridg"))
print(first_non_repeatflacing_letter("stress"))
print(first_non_repeatflacing_letter("sTreSS"))
print(first_non_repeatflacing_letter("dfgSSdFG"))
print("Task №3")
print(digital_root(493193))
print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print("Task №4")
my_array = np.array([1, 3, 6, 2, 2, 0, 4, 5, -1])
p = 5
print(find_p(my_array, p))
print("Task №5")
s = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;" \
    "Alfred:Tornbull;Raphael:Corwill;Alfred:Corwill"
sort_d = transformation(s)
for i in sort_d:
    print(f'({i[1]},{i[0]})')
assert find_next(4) == '-1'
assert find_next(333) == '-1'
assert find_next(9876) == '-1'
assert find_next(300) == '-1'
assert find_next(25543) == 32455
assert find_next(4546) == 4564
assert find_next(513) == 531
print("Task №6 Completed")
print("Task №7(додаткове 2)")
print(convert(2149583361))
print(convert(32))
print(convert(0))
