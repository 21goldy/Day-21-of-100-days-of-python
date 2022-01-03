from math import gcd
from tabulate import tabulate

r1 = int(input("Enter the value of a: "))
r2 = int(input("Enter the value of b: "))
a = r1
b = r2
s1 = 1
s2 = 0
t1 = 0
t2 = 1

r2_list = []
s2_list = []
t2_list = []

while r2 != 0:
    quotient = int(r1 / r2)
    remainder = int(r1 % r2)
    s = s1 - quotient * s2
    t = t1 - quotient * t2
    algo = [["q", "r1", "r2", "r", "s1", "s2", "s", "t1", "t2", "t"],
            [f"{quotient}", f"{r1}", f"{r2}", f"{remainder}", f"{s1}", f"{s2}", f"{s}", f"{t1}", f"{t2}", f"{t}"]]
    print(tabulate(algo, tablefmt='fancy_grid'))
    r1 = r2
    r2 = remainder
    s1 = s2
    s2 = s
    t1 = t2
    t2 = t

    if remainder != 0:
        r2_list.append(r2)
        s2_list.append(s2)
        t2_list.append(t2)

# print(r2_list)
algo = [["q", "r1", "r2", "r", "s1", "s2", "s", "t1", "t2", "t"],
        ["-", f"{r2_list[-1]}", "-", "-", f"{s2_list[-1]}", "-", "-", f"{t2_list[-1]}", "-", "-"]]
print(tabulate(algo, tablefmt='fancy_grid'))

# print(a)
inverse = t1 % a
print("================================================")
print(f"Inverse: {inverse}")

LHS = s2_list[-1]*a + t2_list[-1]*b
RHS = gcd(a, b)


print("================================================")
print("Verification: \ns*a + t*b = gcd(a, b)")
print(f"{s2_list[-1]}*{a} + {t2_list[-1]}*{b} = gcd({a}, {b})")
print(f"{LHS} = {RHS}")
if LHS == 1 and RHS == 1:
    print("Inverse exists!")
else:
    print("Inverse does not exists!")
print("================================================")
