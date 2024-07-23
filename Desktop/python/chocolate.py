def findMinDiff(arr, n, m):

    # if there are no chocolates or number of students is 0
    if (m==0 or n==0):
        return 0

    # Sort the given packets
    arr.sort()

    # Number of students cannot be more than number of packets
    if (m > n):
        return -1

    # Largest number of chocolates
    min_diff = arr[n-1] - arr[0]

    # Find the subarray of size m such that
    # difference between last (maximum in case
    # of sorted) and first (minimum in case of
    # sorted) elements of subarray is minimum.
    for i in range(len(arr) - m + 1):
        min_diff = min(min_diff ,
                       arr[i + m - 1] - arr[i])

    return min_diff

# Driver Code
if _name_ == "_main_":
    arr = [7,6,3,2,9]

    # Number of students
    m = 2
    n = len(arr)
    print("Minimum difference is", findMinDiff(arr, n, m))
