import run_cython
import time

from random import randint

def test(arr,length,search_val):
    for c in range(0,length):
        if arr[c]==search_val:
            return 1
            break
    if c==length:
        return  0

# basic test case
start_py = time.time()
print(run_cython.test([1, 1, 4, 1], 4, 4))
end_py = time.time()


# Tested for 100, 200, 1000,15000,25000,50000,100000
size=100
array_of_numbers=[]
for _ in range(size):
    value=randint(0,size)
    array_of_numbers.append(value)



start_py = time.time()
print(run_cython.test(array_of_numbers, 4, 4))
end_py = time.time()




