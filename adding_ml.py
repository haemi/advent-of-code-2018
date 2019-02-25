import numpy as np
import pandas as pd
from random import shuffle

# generate input
import sklearn
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

entries = 3

input_list = np.zeros((0, 3))
for x1 in range(1, entries + 1):
    for x2 in range(1, entries + 1):
        for x3 in range (1, entries + 1):
            inner_array = [x1, x2, x3]
            input_list = np.append(input_list, [inner_array], axis=0)

shuffle(input_list)

y = []
for row in input_list:
    y.append(row[0] + row[1] + row[2])

df = pd.DataFrame(data=input_list)

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(df, y)

regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)
y_pred = regr.predict(X_test)
print(mean_squared_error(y_test, y_pred))
print(r2_score(y_test, y_pred))
new_X_test = pd.DataFrame(data={'x1': [7, -236, 10], 'x2': [14, 2973, 100], 'x3': [28, 23089, -10]})
print(regr.predict(new_X_test))
