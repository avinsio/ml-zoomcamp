import numpy as np

X = np.array([
    [148, 24, 1385],
    [132, 25, 2031],
    [453, 11, 86],
    [158, 24, 185],
    [172, 25, 201],
    [413, 11, 86],
    [38,  54, 185],
    [142, 25, 431],
    [453, 31, 86],
])

y = np.array([
    10000, 20000, 15000, 20050, 10000,
    20000, 15000, 25000, 12000
])

# Add bias (intercept) term
ones = np.ones(len(X))
X = np.column_stack([ones, X])

# Normal Equation: w = (XᵀX)⁻¹Xᵀy
XTX = X.T.dot(X)
XTX_inv = np.linalg.inv(XTX)
w_full = XTX_inv.dot(X.T).dot(y)

# Separate bias and feature weights
w0 = w_full[0]
w = w_full[1:]

print("Bias:", w0)
print("Weights:", w)