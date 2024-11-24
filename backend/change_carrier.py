import numpy as np
import pandas as pd
import pandas as pd 


df = pd.read_csv('career_change_prediction_dataset.csv')   
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(df.drop(columns=['Likely to Change Occupation']),df['Likely to Change Occupation'],test_size=0.25,random_state=40)
from sklearn.preprocessing import StandardScaler, OneHotEncoder , OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import xgboost as xgb
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import GridSearchCV
import pickle 

                                                                                                                                                                   # Define a preprocessing pipeline for numeric and categorical columns
preprocessor = ColumnTransformer(
    transformers=[
        ('ordinal1',OrdinalEncoder(categories=[[False,True]]),['Job Satisfaction']),
        ('ordinal2',OrdinalEncoder(categories=[['0-30k', '30k-60k', '60k-100k', '100k-200k', '200k+']]),['Salary Group']),
        ('cat', OneHotEncoder(), ['Field of Study', 'Age','Job Opportunities','Years of Experience', 'Gender','Current Occupation','Industry Growth Rate', 'Family Influence','Education Level'])  # One-hot encode categorical features
    ])

# Create a pipeline that first preprocesses the data and then trains an XGBoost classifier
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', xgb.XGBClassifier(n_estimators=100, random_state=40))  # XGBoost Classifier
])




# Define your parameter grid for hyperparameter tuning
param_grid = {
    'classifier__learning_rate': [0.01, 0.05, 0.1, 0.2],  # Exploring different learning rates
    'classifier__max_depth': [3, 5, 7, 10],  # Explore different tree depths
    'classifier__n_estimators': [100, 200, 300],  # Varying number of estimators
    'classifier__subsample': [0.8, 1.0],  # Subsampling ratio
    'classifier__colsample_bytree': [0.7, 1.0],  # Column subsampling
    'classifier__gamma': [0, 0.1, 0.2]  # Regularization
}


# Create the GridSearchCV object
grid_search = GridSearchCV(model_pipeline, param_grid, cv=3, verbose=1,n_jobs=-1)

# Fit the grid search to find the best hyperparameters
grid_search.fit(X_train, y_train)

# Get the best model found by GridSearchCV
best_model = grid_search.best_estimator_

# Predict on the test set using the best model
y_pred = best_model.predict(X_test)

# Evaluate the best model
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))                                                                                                          # Step 1: Save the trained best_model to a pickle file
with open('best_model21.pkl', 'wb') as file:
    pickle.dump(best_model, file)
print("Model saved as 'best_model.pkl'.")

       