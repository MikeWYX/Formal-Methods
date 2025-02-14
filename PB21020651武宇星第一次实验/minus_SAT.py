from z3 import *

s = Solver()
# d = a - b
a = 8
b = 13
c = []
d = []  

def int_to_bool(a):
    binary_str = bin(a)[2:] 
    bool_str = []
    for bit in binary_str:
        bool_str.append(bit == '1')
    return bool_str

def bool_to_int(bool_str):
    binary_str = ''.join(['1' if val == True else '0' for val in bool_str])
    decimal_value = int(binary_str, 2)  
    return decimal_value

a_bool = int_to_bool(a)
b_bool = int_to_bool(b)
#make sure the length of a and b is the same
if len(a_bool) > len(b_bool):
    b_bool = [False] * (len(a_bool) - len(b_bool)) + b_bool
elif len(a_bool) < len(b_bool):
    a_bool = [False] * (len(b_bool) - len(a_bool)) + a_bool

for i in range(len(a_bool)):
    d.append(Bool(f"d_{i}"))

for i in range(len(a_bool)+1):
    c.append(Bool(f"c_{i}"))

def solve(a, b, d): # assuming a > b, d = a - b, a = b + d
    for i in range(len(a)):
        s.add(d[i] == (a[i] == (b[i] == c[i+1])))
    for i in range(1, len(a)):
        s.add(c[i] == Or(And(a[i], b[i]), And(a[i], c[i+1]), And(b[i], c[i+1])))
    s.add(Not(c[0]))
    s.add(Not(c[len(a)]))
    for i in range(len(d)):
        if d[i] == True:
            s.add(d[i])
        else:
            s.add(Not(d[i]))
    for i in range(len(a)):
        if a[i] == True:
            s.add(a[i])
        else:
            s.add(Not(a[i]))      
    print(s.check())
    print(s.model())
    b_values = []
    for i in range(len(b)):
        b_values.append(s.model().eval(b[i]))
    return b_values

def main():
    if a > b:
        result = solve(d = a_bool, b = d, a = b_bool)
        result = bool_to_int(result)
    else:
        result = solve(a = a_bool, b = d, d = b_bool)
        result = bool_to_int(result)
        result = -result
    print("The result is:", result)

if __name__ == "__main__":
    main()