# %%
from bmi_functions import calc_bmi_lists
from bmi_functions import calc_bmi_arrays
import random
import numpy as np

# %%
hts = np.array([random.uniform(0.5, 2.2) for _ in range(480)])
wts = np.array([random.uniform(50, 220) for _ in range(480)])
indices = np.array([i % 480 for i in range(25000)])


# %%
%load_ext memory_profiler

# %%
%mprun -f calc_bmi_lists calc_bmi_lists(indices, hts, wts)

# %%
%mprun -f calc_bmi_arrays calc_bmi_arrays(indices, hts, wts)

# %%
