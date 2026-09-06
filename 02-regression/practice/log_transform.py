import numpy as np

# log(x)
x = [1, 10, 1000, 10000]
print(np.log(x))

# log(0) → -inf
x = [0, 1, 10, 1000, 10000]
print(np.log(x))

# log(x + 1)
x = [0, 1, 10, 1000, 10000]
print(np.log(np.array(x) + 1))

# log1p(x) → log(1 + x)
print(np.log1p(x))