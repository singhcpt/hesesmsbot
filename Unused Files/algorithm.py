#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import graphviz
import matplotlib.pyplot as plt
import matplotlib.axes
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

cache = []


# In[4]:


def loadData(filename):
    
    data = pd.read_csv(filename)
    
    return data


# In[5]:


def trainModel(data, n_estimators, max_depth, min_samples_leaf):

    X = data.values[:,1:7]
    Y = data.values[:,7:8]
    
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, stratify=Y)
    
    rf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, min_samples_leaf=min_samples_leaf)

    rf.fit(X_train, y_train)

    y_pred = rf.predict(X_test)

    accuracy = accuracy_score(y_pred, y_test)
    
    return rf, accuracy 


# In[6]:


def predictCase(model, data_point):
    
    global cache
    
    prediction = model.predict(data_point)
    
    if prediction == 0:
        
        for report in cache:
        
            if data_point[0][1:]==report[0][1:]:
                
                prediction = [1, 'cache']
                
                cache.remove(report)
                
                return prediction
                
        cache.append(data_point)
        
    return prediction[0]     


# In[7]:


def updateData(data, dataAdditions):
    
    appended_data = pd.DataFrame([dataAdditions], columns=data.columns)
    
    new_data = data.append(appended_data, ignore_index=True)
    
    return(new_data)    


# In[8]:


data = loadData('Toy Data.csv')


# In[9]:


rf, accuracy = trainModel(data, 1000, 2, .25)


# In[11]:


prediction = predictCase(rf, [[3, 1, 1, 1, 1, 1]])
print(prediction)


# In[ ]:




