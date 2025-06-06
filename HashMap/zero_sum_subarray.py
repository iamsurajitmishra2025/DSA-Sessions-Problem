def zero_sum_subarray(arr: [int]) -> bool:
    """
    Intuition:
    I will be summing all the contigious elements and check if the current sum has previously occured or not.
    If a same sum has occured previously, then we can conclude that all the elements in between will sum up to zero.
    :param arr:
    :return: bool
    """

    sum_set = set()
    sum = 0
    n = len(arr)

    for i in range(n):
        sum += arr[i]
        if sum in sum_set: return True
        sum_set.add(sum)

    return False

if __name__ == '__main__':
    print("Test Case 1: ")
    arr = [4, 2, -3, 1, 6]
    print("Arr", arr)
    print(zero_sum_subarray(arr)) # True

    print("Test Case 2: ")
    arr = [4, 2, 0, 1, 6]
    print("Arr", arr)
    print(zero_sum_subarray(arr))  # True

    print("Test Case 3: ")
    arr =  [-3, 2, 3, 1, 6]
    print("Arr", arr)
    print(zero_sum_subarray(arr))  # False



