# %%
# Measure time on a cell
%%timeit
import numpy as np
rand_nums = np.random.rand(1000)

# %%
# Measure time on a single line
time = %timeit -o np.random.rand(1000)

# %%
# List all the available magic commands
%lsmagic

# %%
# dict() vs literal {}
f_time = %timeit -o dict()
l_time = %timeit -o {}
diff = (f_time.average - l_time.average) / f_time.average * 100
print(f"Dict() is {diff:.2f}% slower than {{}}")
 
# %%
## List comprehension vs unpacking
time_comp = %timeit -o [i for i in range(1000)]
time_unpack = %timeit -o [*range(1000)]
diff = (time_comp.average - time_unpack.average) / time_comp.average * 100
print(f"List comprehension is {diff:.2f}% slower than unpacking")

# %%
# Modify the number of runs and loops
time = %timeit -r 10 -n 1000 np.random.rand(1000)
# %%
