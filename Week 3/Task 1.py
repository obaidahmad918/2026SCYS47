def calc_fact(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def calc_perm(n, r):
    return calc_fact(n) // calc_fact(n - r)

def calc_comb(n, r):
    return calc_fact(n) // (calc_fact(r) * calc_fact(n - r))

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
print("Permutation P(", n, ",", r, ") is: ", calc_perm(n, r))
print("Combination C(", n, ",", r, ") is: ", calc_comb(n, r))
