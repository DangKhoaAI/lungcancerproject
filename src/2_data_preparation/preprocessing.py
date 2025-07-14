
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
df = pd.read_csv('data/raw/luncgancerdataset.csv')

# Drop rows with missing values (if any)
df.dropna(inplace=True)

# Encode categorical features
categorical_cols = ['GENDER', 'SMOKING', 'FINGER_DISCOLORATION', 'MENTAL_STRESS', 
                    'EXPOSURE_TO_POLLUTION', 'LONG_TERM_ILLNESS', 'IMMUNE_WEAKNESS', 
                    'BREATHING_ISSUE', 'ALCOHOL_CONSUMPTION', 'THROAT_DISCOMFORT', 
                    'CHEST_TIGHTNESS', 'FAMILY_HISTORY', 'SMOKING_FAMILY_HISTORY', 
                    'STRESS_IMMUNE', 'PULMONARY_DISEASE']
for col in categorical_cols:
    if col in df.columns:
        df[col] = df[col].astype('category').cat.codes

# Normalize numerical features
numerical_cols = ['AGE', 'ENERGY_LEVEL', 'OXYGEN_SATURATION']
scaler = MinMaxScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Save the cleaned dataset
df.to_csv('data/processed/lung_cancer_cleaned.csv', index=False)

print("Preprocessing complete. Cleaned data saved to data/processed/lung_cancer_cleaned.csv")
