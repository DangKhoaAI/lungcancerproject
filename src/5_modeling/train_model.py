
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the cleaned dataset
df = pd.read_csv('/mnt/data/FPTStudy/Semester4/DAP391m/project/lung_cancer_project/data/processed/lung_cancer_cleaned.csv')

# Define features (X) and target (y)
X = df.drop('PULMONARY_DISEASE', axis=1)
y = df['PULMONARY_DISEASE']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model to a file
with open('/mnt/data/FPTStudy/Semester4/DAP391m/project/lung_cancer_project/5_modeling/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model training complete. Model saved to 5_modeling/model.pkl")
