from sys import path

path.append(r'..\Task_4_2_1')

import Modules.module_1
import Modules.module_2
print()

from Packages.Bad.bad_1 import func_bad_1
from Packages.Bad.bad_2 import func_bad_2
print(func_bad_1())
print(func_bad_2())
print()

from Packages.Good import good_1, good_2

print(good_1.func_good_1())
print(good_2.func_good_2())
print()

from Packages.Good.Best import best_1, best_2

print(best_1.func_best_1())
print(best_2.func_best_2())
print()

from Packages.Ugly import ugly_1, ugly_2

print(ugly_1.func_ugly_1())
print(ugly_2.func_ugly_2())