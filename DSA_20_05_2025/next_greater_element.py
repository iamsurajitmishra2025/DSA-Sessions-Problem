def find_nge(arr: [int]) -> [int]:
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

