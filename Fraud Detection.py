#!/usr/bin/env python
# coding: utf-8

# # Fraud Detection

# # Task 2 CODECLAUSE INTERNSHIP - JULY 

# In[1]:


get_ipython().system('pip install --upgrade pillow')


# In[2]:


from PIL import Image


# In[4]:


# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report


# In[5]:


# Load the dataset
data = pd.read_csv('creditcard.csv')


# In[6]:


# Explore the data
print(data.head())
print(data.info())
print(data.describe())


# In[7]:


# Visualize the class distribution
sns.countplot(data['Class'])
plt.title('Class Distribution')


# In[8]:


# Split the data into training and testing sets
X = data.drop('Class', axis=1)
y = data['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[9]:


# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# In[10]:


# Train a random forest classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train_scaled, y_train)


# In[11]:


# Make predictions on the test set
y_pred = rf.predict(X_test_scaled)


# In[12]:


# Evaluate the model
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


# # Thank You

# In[ ]:




