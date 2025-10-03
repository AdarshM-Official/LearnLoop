# This script must be run once to generate a dummy ML model file 
# that the Django application's tasks.py can load successfully.

import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
import os

# 1. Define dummy features for the model training
# Feature order: [ast_nodes_count, max_ast_depth, cyclomatic_complexity]
X = np.array([
    [10, 3, 1],   # Simple function (Low seniority)
    [50, 8, 5],   # Complex logic with branches (Mid seniority)
    [150, 15, 20] # Very complex or long code (High complexity/potential Senior)
])

# Define corresponding target seniority scores (0.0 to 1.0)
y = np.array([0.3, 0.6, 0.9])

# 2. Train a dummy Linear Regression model
model = LinearRegression()
model.fit(X, y)

# 3. Save the model to a joblib file
model_path = 'seniority_model.joblib'
joblib.dump(model, model_path)

print(f"Dummy ML model saved successfully to: {os.path.abspath(model_path)}")
print("Run this file first, then configure and run your Django server.")

# Example function to test the model:
def predict_seniority(features):
    # Features must be in the order: [nodes, depth, complexity]
    return model.predict([features])[0]

# Test cases:
simple_features = [15, 4, 2] # Should predict low
complex_features = [80, 10, 10] # Should predict high

print(f"Prediction for simple code: {predict_seniority(simple_features):.2f}")
print(f"Prediction for complex code: {predict_seniority(complex_features):.2f}")
