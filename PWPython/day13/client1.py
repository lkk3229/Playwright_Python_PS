
# ------ Approach 1: Importing full modules -----
# import pack1.module1
# import pack1.module2
#
# pack1.module1.display()   # Calls display() from module1
# pack1.module2.show()      # Calls show() from module2


# ------ Approach 2: Importing everything (*) ------
from pack1.module1 import *
from pack1.module2 import *

display()   # Directly calls display() without module name
show()      # Directly calls show()
show()      # Can be called multiple times

