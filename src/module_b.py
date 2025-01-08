# module_b.py
import src.module_c as module_c

module_c.global_var_c = "This is global variable C in module B"

print(module_c.global_var_c)