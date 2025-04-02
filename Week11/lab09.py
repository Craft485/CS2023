'''
n_estimator | Accuracy (%)
1           | 67.21
2           | 75.41
3           | 83.61
4           | 81.97
5           | 86.89
6           | 85.25
7           | 88.52
8           | 80.33
9           | 91.80
10          | 85.25

An n_estimator value of 9 gave the best result with an accuracy of ~91.8%
'''

_author_ = "Colin Davis"
_credits_ = []
_email_ = "davis7cl@mail.uc.edu"

from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# Load csv and pull column headers from it
heart_disease = pd.read_csv('./heart.csv') # Modify this to your file system
X = heart_disease.drop(['target'], axis = 1) # Get every column except target
Y = heart_disease['target'] # Get column named target
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)

np.random.seed(42)
for i in range(1, 11, 1):
    # Setup model
    clf = RandomForestClassifier(n_estimators = i)
    clf.fit(X_train, Y_train) # Load the data into the model?
    #Evaluate how well the model did
    print(f'Accuracy for {i} n_estimator(s): {clf.score(X_test, Y_test) * 100:.2f}%')
