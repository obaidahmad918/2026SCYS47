def calc_sum(*nums):
    total = 0
    for n in nums:
        total += n
    print("Total sum:", total)

calc_sum(10, 20, 30)
calc_sum(1, 2, 3, 4, 5)
