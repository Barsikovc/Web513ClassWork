from functools import reduce

nums_list = [i + 1 for i in range(5)]
print(nums_list)

reduce_sum = reduce(lambda x, y: x + y, nums_list)  # 1 + 2 = 3|3 + 3 = 6|6 + 4 = 10|10 + 5 = 15
print(reduce_sum)
reduce_product = reduce(lambda x, y: x * y, nums_list)
print(reduce_product)

reduce_sum_init = reduce(lambda x, y: x + y, nums_list, 10)  # 10 + (1 + 2 = 3|3 + 3 = 6|6 + 4 = 10|10 + 5 = 15)
print(reduce_sum_init)
