# %%
%load_ext line_profiler

# %%
def my_func():
    a = 1
    b = 2
    return a + b
%lprun -f my_func my_func()

# %%
