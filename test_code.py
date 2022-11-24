import run_python
import run_cython
import time


from random import randint
size=1000000
array_of_numbers=[]
for _ in range(size):
    value=randint(0,size)
    array_of_numbers.append(value)


start = time.time()
print(run_python.test(array_of_numbers, size, 4))
end =  time.time()

py_time = end - start
print(py_time)

start = time.time()
print(run_cython.test(array_of_numbers, size, 4))
end =  time.time()

cy_time = end - start
print(cy_time)

# print("Speedup = {}".format(py_time / cy_time))