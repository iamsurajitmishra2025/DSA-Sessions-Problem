"""
5.Given an array of positive and negative numbers, find if there is a subarray (of size at-least one) with 0 sum.
Examples :

Input: {4, 2, -3, 1, 6}
Output: true
Explanation:
There is a subarray with zero sum from index 1 to 3.
Input: {4, 2, 0, 1, 6}
Output: true
Explanation :
The third element is zero. A single element is also a sub-array.
Input: {-3, 2, 3, 1, 6}
Output: false
"""

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



