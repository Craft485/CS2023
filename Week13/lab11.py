"""
Multiple Linear Regression using All features  
R2 score : 0.6008983115964333
MSE score: 0.5350149774449118

Feature 0 has R2 score : 0.4630810035698606
          has MSE score 0.7197656965919478
Feature 1 has R2 score : 0.013185632224592903
          has MSE score 1.3228720450408296
Feature 2 has R2 score : 0.024105074271276283
          has MSE score 1.3082340086454287
Feature 3 has R2 score : -0.0011266270315772875
          has MSE score 1.3420583158224824
Feature 4 has R2 score : 8.471986797708997e-05
          has MSE score 1.3404344471369465
Feature 5 has R2 score : -0.00018326453581640756
          has MSE score 1.340793693098357
Feature 6 has R2 score : 0.020368890210145207
          has MSE score 1.3132425427841639
Feature 7 has R2 score : 0.0014837207852690382
          has MSE score 1.3385590192298276

The multiple linear regression shows a stringer correlation than any of the single linear regressions. 
The strongest single linear regression (highest R2 and lowest MSE) is the first feature, MedInc, with and R2 of ~0.46 and MSE of ~0.72
"""

_author_ = "Colin Davis"
_credits_ = []
_email_ = "davis7cl@mail.uc.edu"

import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

cali = fetch_california_housing()
cali_df = pd.DataFrame(cali.data, columns=cali.feature_names)
cali_df['MedHouseValue'] = pd.Series(cali.target)

X_train, X_test, y_train, y_test = train_test_split(cali.data, cali.target, random_state=11)

mu_regress = LinearRegression()
mu_regress.fit(X=X_train, y=y_train)
predicted = mu_regress.predict(X_test)
expected = y_test

print(f"Multiple Linear Regression using ALL features\nR2 score : {r2_score(expected, predicted)}\nMSE score: {mean_squared_error(expected, predicted)}\n")

for i in range(len(cali.feature_names)):
    X_train, X_test, y_train, y_test = train_test_split(cali_df[cali.feature_names[i]].values.reshape(-1, 1), cali.target, random_state=11)
    lr = LinearRegression()
    lr.fit(X=X_train, y=y_train)
    y_pred = lr.predict(X_test)
    print(f"Feature {i} has R2 score : {r2_score(y_test, y_pred)}\n\t  has MSE score {mean_squared_error(y_test, y_pred)}")