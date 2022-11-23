cpdef int test(array, n, k):

    for j in range(0, n):

        if (array[j] == k):

            return j

    return -1