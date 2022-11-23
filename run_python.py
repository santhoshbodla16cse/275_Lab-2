from random import randint
import time

def test(array, n, k):

    for j in range(0, n):

        if (array[j] == k):

            return j

    return -1

# Tested for 100, 200, 1000,15000,25000,50000,100000

size=100
array_of_numbers=[]
for _ in range(size):
    value=randint(0,size)
    array_of_numbers.append(value)


start_py = time.time()
print(test(array_of_numbers, 4, 4))
end_py = time.time()
