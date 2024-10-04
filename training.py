# Import necessary libraries for training
import pandas as pd
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearnex import patch_sklearn
import joblib

# Load the dataset
df = pd.read_csv('conv2.csv')

# Features and target variable
X = df.drop('Time_Between_Flares', axis=1)
y = df['Time_Between_Flares']

patch_sklearn()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest Regressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
rf_regressor.fit(X_train, y_train)

# Get predictions
y_pred = rf_regressor.predict(X_test)

# Print the original predictions
print(f"Original Predictions (Decimal): {y_pred}")

# Round predictions to the nearest integer
y_pred_rounded = [int(round(pred)) for pred in y_pred]  # Explicitly round to nearest integer

# Print the rounded predictions
print(f"Rounded Predictions (Integer): {y_pred_rounded}")

# Evaluate the model using MAE and RMSE with rounded predictions
mae = mean_absolute_error(y_test, y_pred_rounded)
rmse = mean_squared_error(y_test, y_pred_rounded, squared=False)

print(f"Mean Absolute Error: {mae}")
print(f"Root Mean Squared Error: {rmse}")

# Cross-validation (using original y for cross-validation but rounded output for results)
cv_results = cross_validate(rf_regressor, X, y, cv=5, scoring=['neg_mean_absolute_error', 'neg_mean_squared_error'])

# Print results of each fold
print("Cross-validation results:")
print("MAE:", -cv_results['test_neg_mean_absolute_error'])
print("RMSE:", [-(-mse)**0.5 for mse in cv_results['test_neg_mean_squared_error']])  # Taking sqrt of negative MSE

# Print the average of each metric across all folds
print("\nAverage MAE:", -cv_results['test_neg_mean_absolute_error'].mean())
print("Average RMSE:", (-cv_results['test_neg_mean_squared_error'].mean())**0.5)

# Save the trained model
joblib.dump(rf_regressor, 'rf_flare_predictor_regressor.pkl')