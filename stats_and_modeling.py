#!/usr/bin/env python
# coding: utf-8

# In[1]:


# standard imports
import numpy as np
import pandas as pd
# stats
from scipy import stats
# modeling
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.metrics import explained_variance_score
# notebook formatting
from pprint import pprint
import warnings
warnings.filterwarnings("ignore")


# In[ ]:


def hypothesis_test(x, y):
    α = 0.05
    r, p = stats.pearsonr(x, y)
    if p > α:
        print(f'P-value: {p} \nr-value: {r} \nI fail to reject the null hypothesis.')
    else:
        print(f'P-value: {p} \nr-value: {r} \nI reject the null hypothesis.')


# In[ ]:


def rmse_using_mu(y_train):
    # create baseline for train using mean
    y_train['engage_pred_mean'] = y_train['engagement'].mean()
    # RMSE of engage_pred_mean
    rmse_train_mu = mean_squared_error(y_train.engagement,
                                    y_train.engage_pred_mean) ** .5
    print(f"""RMSE using Mean
    Train/In-Sample: {round(rmse_train_mu, 2)}""")
    return rmse_train_mu


# In[ ]:


def create_models_df(rmse_train_mu, y_train)    
    metric_df = pd.DataFrame(data=[
        {'model': 'mean_baseline',
         'RMSE_train': rmse_train_mu,
         'R2_train': explained_variance_score(y_train.engagement,
                                                 y_train.engage_pred_mean)
        }]
    )
    return metric_df


# In[ ]:


def rmse_using_ols
    # drop username and name to be able to use ols model
    X_train = X_train.drop(columns=['username'])
    # make the thing
    lm = LinearRegression()
    # fit the thing
    OLSmodel = lm.fit(X_train, y_train.engagement)
    # use the thing
    y_train['engage_pred_lm'] = lm.predict(X_train)
    # evaluatge the thing - RMSE
    rmse_train = mean_squared_error(y_train.engagement, y_train.engage_pred_lm)**(1/2)
    print(f"""RMSE for OLS using LinearRegression
    Training/In-Sample:  {rmse_train}""")
    return rmse_train


# In[ ]:


def add_to_models_df(rmse_train, y_train)
    metric_df = metric_df.append(
        {'model': 'OLS Regressor',
         'RMSE_train': rmse_train,
         'R2_train': explained_variance_score(y_train.engagement,
                                                 y_train.engage_pred_lm)
        }, ignore_index=True)
    return metric_df

