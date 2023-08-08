# -*- coding: utf-8 -*-
"""LoanDecisionTree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WABw18VSW5wgEx2vl5eFVKjDOYLR0tFK
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus
import xgboost as xgb

loans = pd.read_csv('/loan-train.csv')
updatedloans = loans.fillna(loans.mean())
updatedloans.head()

print(updatedloans.describe())
print(updatedloans.info())
print(updatedloans.shape)

features = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']
X = updatedloans[features]
y = updatedloans['Loan_Status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)

classify = DecisionTreeClassifier(criterion="entropy")
classify.fit(X_train, y_train)
y_pred = classify.predict(X_test)

print('The Accuracy of this model:', metrics.accuracy_score(y_test, y_pred))

data = StringIO()
export_graphviz(classify, out_file = data, filled = True, rounded = True, special_characters = True, feature_names = features, class_names = ['0', '1'])
graph = pydotplus.graph_from_dot_data(data.getvalue())
graph.write_png('tree.png')
Image(graph.create_png())

xgb_model = xgb.XGBClassifier()
y_train = y_train.map({'N':0, 'Y':1})
y_test = y_test.map({'N':0, 'Y':1})
xgb_model.fit(X_train, y_train)
y_pred = xgb_model.predict(X_test)

accuracy = metrics.accuracy_score(y_test, y_pred)
print("Accuracy Score is: %f" % accuracy)

xgb_model = xgb.XGBClassifier(learning_rate=0.1, n_estimators=100)
xgb_model.fit(X_train, y_train)

data = StringIO()
export_graphviz(classify, out_file = data, filled = True, rounded = True, special_characters = True, feature_names = features, class_names = ['0', '1'])
graph = pydotplus.graph_from_dot_data(data.getvalue())
graph.write_png('tree.png')
Image(graph.create_png())