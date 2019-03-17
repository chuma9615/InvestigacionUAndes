
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
diabetes = datasets.load_diabetes()


# Use only one feature
diabetes_X_train = [ np.sin(3*np.pi*i/39) for i in range(60)]
diabetes_X_test = [ np.sin(3*np.pi*i/39) for i in range(60)]
diabetes_t_train = [ [i] for i in range(len(diabetes_X_train))]
diabetes_t_test = [ [i] for i in range(len(diabetes_X_train))]
# Split the data into training/testing sets

# Split the targets into training/testing sets


# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_t_train, diabetes_X_train)

# Make predictions using the testing set


predictions = regr.predict(diabetes_t_test)
print(predictions)
plt.plot(diabetes_t_train,diabetes_X_test)
plt.plot(predictions)
plt.show()
