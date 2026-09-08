actual = [10, 12, 14]
predicted = [11, 10, 13]

error = [a - p for a, p in zip(actual, predicted)]
squared_error = [e**2 for e in error]

mse = sum(squared_error) / len(squared_error)
rmse = mse ** 0.5

print(rmse)  