import pandas as pd
from sklearn import linear_model
import matploitlib.pyplot as plt

# read data
data_frame = pd.read_fwf('data.txt')
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]

# train model on data
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

# visualize result
plt.scatter(x_values, y_values)
plt.plot(x_values, body_reg.predict(x_values))
plt.show()
