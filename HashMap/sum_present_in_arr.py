"""
6.Given an unsorted array arr of nonnegative integers and an integer sum, find a continuous subarray which adds to a given sum. There may be more than one subarrays with sum as the given sum, print first such subarray.
Examples :
Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Output: Sum found between indexes 2 and 4
Sum of elements between indices 2 and 4 is 20 + 3 + 10 = 33

Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
Output: Sum found between indexes 1 and 4
Sum of elements between indices 1 and 4 is 4 + 0 + 0 + 3 = 7
"""

def sum_present_in_arr(arr: [int], target: int) -> [int]:
    """
    Explanation:
    While iterating the arr, I will keep a track of the current sum of elements and current index.
    Also, I will keep searching in the hash map, if (sum - target) sum has already occured.
    For example, target = 33
    current sum = 38.
    sum - target = 38 - 33 = 5
    I want to know, if 5 has already occured. If yes, that means, the sum of subarray in between will be equal to target.
    :param arr:
    :param target:
    :return: [int] of size 2
    """


    n = len(arr)
    sum_dict = {}
    sum = 0
    for i in range(n):
        sum += arr[i]
        if sum_dict and (sum - target) in sum_dict:
            return [sum_dict[(sum - target)] + 1, i]
        sum_dict[sum] = i

    return [-1, -1]

if __name__ == '__main__':
    print("Test Case 1: ")
    arr = [1, 4, 20, 3, 10, 5]
    target = 33
    print("Arr", arr)
    print(sum_present_in_arr(arr, target))  # [2,4]

    print("Test Case 2: ")
    arr =  [1, 4, 0, 0, 3, 10, 5]
    target = 7
    print("Arr", arr)
    print(sum_present_in_arr(arr, target))  # [1, 4]

    print("Test Case 2: ")
    arr = [1, 4]
    target = 0
    print("Arr", arr)
    print(sum_present_in_arr(arr, target))  # [-1,-1]


