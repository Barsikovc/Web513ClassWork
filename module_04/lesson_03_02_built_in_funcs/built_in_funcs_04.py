def get_evens(nums):
    evens_list = []
    for num in nums:
        if num % 2 == 0:
            evens_list.append(num)
    return evens_list


def is_even(num):
    return num % 2 == 0


if __name__ == '__main__':
    nums_list = list(range(8 + 1))
    print(nums_list)
    print(get_evens(nums_list))

    filtered_nums = list(filter(lambda x: x % 2 == 0, nums_list))
    print(filtered_nums)
    filtered_nums = list(filter(is_even, nums_list))
    print(filtered_nums)

    for num in nums_list:
        if is_even(num):
            print(num, end=' ')
