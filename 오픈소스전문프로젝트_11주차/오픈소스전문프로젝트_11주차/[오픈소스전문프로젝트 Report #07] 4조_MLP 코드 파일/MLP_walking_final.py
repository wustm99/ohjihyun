#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = pd.read_csv('walking_final.csv', names = ["level","impect"])
print(data.head())


# In[2]:


print (data.shape)


# In[3]:


X = data.loc[:,['impect']]

y = data['level']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y)


# In[4]:


from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
scaler.fit(X_train)

StandardScaler(copy = True, with_mean=True, with_std=True)

X_train=scaler.transform(X_train)
X_test=scaler.transform(X_test)


# In[14]:


from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(10,10,10))
mlp.fit(X_train,y_train)


# In[15]:


from sklearn.metrics import classification_report,confusion_matrix

predictions = mlp.predict(X_test)

print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))


# In[ ]:




