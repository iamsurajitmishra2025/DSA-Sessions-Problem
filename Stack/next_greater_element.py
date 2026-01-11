"""
3.Given an array, print the Next Greater Element (NGE) for every element.
The Next greater Element for an element x is the first greater element on the right side of x in the array. Elements for which no greater element exist, consider the next greater element as -1.
Example:
Input: arr[] = [ 4 , 5 , 2 , 25 ]
Output:  4      -->   5
               5      -->   25
               2      -->   25
              25     -->   -1
Explanation: except 25 every element has an element greater than them present on the right side
Input: arr[] = [ 13 , 7, 6 , 12 ]
Output:  13      -->    -1
                7       -->     12
                6       -->     12
               12      -->     -1
Explanation: 13 and 12 don't have any element greater than them present on the right side
"""


def find_nge(arr: [int]) -> [int]:
    """
    Explanation: Starting from end of the array.
        While the current element is greater than the top elements of the stack, keep popping them.
        Because, these elements will never contribute to the answer.
    :param arr:
    :return: [int]
    """
    n = len(arr)
    nge = [-1]*n
    st = []
    for i in range(n-1, -1, -1):
        while st and arr[i] >= st[-1]:
            st.pop()

        nge[i] = st[-1] if st else -1
        st.append(arr[i])

    return nge

if __name__ == '__main__':
    print("Test Case 1:")
    arr = [4,5,2,25]
    nge = find_nge(arr)
    print("Input Arr:", arr)
    print("Output Arr:", nge) # [5, 25, 25, -1]

    print("Test Case 2:")
    arr = [ 13 , 7, 6 , 12 ]
    nge = find_nge(arr)
    print("Input Arr:", arr)
    print("Output Arr:", nge) # [-1, 12, 12, -1]

