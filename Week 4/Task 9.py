def calc_avg(*nums):
    s = 0
    for n in nums:
        s += n
    print("Average:", s / len(nums))

calc_avg(10, 20, 30)
calc_avg(5, 15, 25, 35)
