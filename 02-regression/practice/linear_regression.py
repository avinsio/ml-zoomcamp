# single example
import numpy as np
xi = [453, 11, 86]
w0 = 7.17
w = [0.01,0.04,0.002]

g_xi = w0 + xi[0] * w[0] + xi[1] *w[1]  + xi[2] * w[2]
print("predication:", g_xi)

def linear_regression(xi):
    m = len(xi)
    pred = w0
    for i in range(m):
        pred += w[i]*xi[i]
    return pred
        
pred = linear_regression(xi)
print(pred)
print(np.expm1(pred))
print(np.log1p(222347.2221101062))
