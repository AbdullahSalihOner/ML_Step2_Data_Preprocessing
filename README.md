<h1>MachineLearning_Step2_Data_Preprocessing</h1>

<h2>Data Preprocessing</h2>
1) Categorical Data
1.1) Label Encoding
LabelEncoder is a class used to convert categorical values in a dataset into numerical values. This is essential for machine learning algorithms to effectively work with categorical data.

python
Copy code
from sklearn.preprocessing import LabelEncoder

# Sample data
categories = ['red', 'blue', 'green', 'red', 'yellow']

# Creating a LabelEncoder object
encoder = LabelEncoder()

# Transforming categorical values
encoded_categories = encoder.fit_transform(categories)

print(encoded_categories)
Output:

csharp
Copy code
[1 0 2 1 3]
1.2) One-Hot Encoding
OneHotEncoder creates a coding structure where each categorical feature is represented as a separate column. It assigns 0 or 1 values to indicate the presence of a category for each observation.

python
Copy code
from sklearn.preprocessing import OneHotEncoder

# Sample data
categories = ['red', 'blue', 'green', 'blue', 'green', 'blue', 'red', 'blue', 'red', 'red', 'green', 'green']
data = pd.DataFrame(categories, columns=['colors'])

# Creating a OneHotEncoder object
ohe = OneHotEncoder(sparse=False)

# Applying OneHotEncoder
encoded_data = ohe.fit_transform(data[['colors']])

# Getting column names from OneHotEncoder
column_names = ohe.get_feature_names_out(input_features=['colors'])

# Converting transformed data to a DataFrame and setting column names
encoded_df = pd.DataFrame(encoded_data, columns=column_names)

print(data)
print(encoded_df)
2) Data Scaling (Normalization/Standardization)
2.1) Min-Max Scaling (Normalization)
MinMaxScaler is used to scale numerical features to a specific range, commonly between 0 and 1.

python
Copy code
from sklearn.preprocessing import MinMaxScaler

# Sample data
data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]

# Creating a MinMaxScaler object
scaler = MinMaxScaler()

# Scaling the data
scaled_data = scaler.fit_transform(data)

print(scaled_data)
2.2) Standardization
StandardScaler standardizes numerical features by transforming them to have a mean of 0 and a standard deviation of 1.

python
Copy code
from sklearn.preprocessing import StandardScaler

# Sample data
data = [[0, 0], [0, 0], [1, 1], [1, 1]]

# Creating a StandardScaler object
scaler = StandardScaler()

# Scaling the data
scaled_data = scaler.fit_transform(data)

print(scaled_data)
3) Handling Missing Values
3.1) Fill NaN Values
fillna method is used to fill missing values in a DataFrame. Various techniques can be employed based on the nature of the data.

python
Copy code
# Filling missing values with the mean
dataframe['column'].fillna(dataframe['column'].mean(), inplace=True)

# Filling missing values with the mode
dataframe['column'].fillna(dataframe['column'].mode()[0], inplace=True)

# Filling missing values with the median
dataframe['column'].fillna(dataframe['column'].median(), inplace=True)

# Forward fill (use the previous value to fill missing values)
dataframe['column'].fillna(method='ffill', inplace=True)

# Backward fill (use the next value to fill missing values)
dataframe['column'].fillna(method='bfill', inplace=True)
4) Data Splitting
train_test_split function is used to split the dataset into training and testing sets.

python
Copy code
from sklearn.model_selection import train_test_split

# Sample data
X = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
y = [0, 1, 2, 3, 4]

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("X_train:", X_train)
print("X_test:", X_test)
print("y_train:", y_train)
print("y_test:", y_test)
These preprocessing steps are crucial for preparing the data before applying machine learning algorithms. Adjust the methods based on the characteristics of your dataset and the requirements of your machine learning model.
