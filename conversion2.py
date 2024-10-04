import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the dataset
file_path = 'dataset.csv'
df = pd.read_csv(file_path)

# Define the function to calculate severity
def calculate_severity(row):
    severity_score = 0
    
    # Add points for genetic markers
    genetic_markers = row['Genetic_Markers']
    if genetic_markers == 'HLA DR3':
        severity_score += 2
    elif genetic_markers == 'HLA DRB1':
        severity_score += 2
    elif genetic_markers == 'IL12B':
        severity_score += 1
        
    # Add points for biomarkers
    biomarkers = row['Biomarkers']
    if biomarkers == 'Elevated IL 6':
        severity_score += 2
    elif biomarkers == 'High ANA':
        severity_score += 3
        
    # Add points for medical history
    medical_history = row['Medical_History']
    if medical_history == 'Asthma':
        severity_score += 1
    elif medical_history == 'Obesity':
        severity_score += 2

    return severity_score

# Apply the severity calculation
df['Severity'] = df.apply(calculate_severity, axis=1)

# Handle missing values: choose one method
for col in df.columns:
    if df[col].dtype == 'object':  # For categorical columns
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:  # For numeric columns
        df[col].fillna(df[col].mean(), inplace=True)

# Clean unnecessary "Unnamed" columns
df_cleaned = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Identify categorical columns
categorical_columns = df_cleaned.select_dtypes(include=['object']).columns

# Separate binary and multi-category columns
binary_columns = [col for col in categorical_columns if df_cleaned[col].nunique() == 2]
multi_category_columns = [col for col in categorical_columns if df_cleaned[col].nunique() > 2]

# Apply Label Encoding to binary columns
label_encoders = {}
for col in binary_columns:
    le = LabelEncoder()
    df_cleaned[col] = le.fit_transform(df_cleaned[col])
    label_encoders[col] = le

# Apply One-Hot Encoding to multi-category columns
df_encoded = pd.get_dummies(df_cleaned, columns=multi_category_columns)

# Convert boolean values to integers (0 and 1)
df_encoded = df_encoded.astype(int)

# Save the processed dataset
df_encoded.to_csv('conv3.csv', index=False)

print("Processed dataset with severity scores saved to 'conv3.csv'")
