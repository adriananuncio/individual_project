# standard imports
import numpy as np
import pandas as pd
# stats
from scipy import stats
# modeling
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression, LassoLars
from sklearn.metrics import explained_variance_score
# notebook formatting
from pprint import pprint
import warnings
warnings.filterwarnings("ignore")

def hypothesis_test(x, y):
    α = 0.05
    r, p = stats.pearsonr(x, y)
    if p > α:
        print(f'P-value: {p} \nr-value: {r} \nI fail to reject the null hypothesis.')
    else:
        print(f'P-value: {p} \nr-value: {r} \nI reject the null hypothesis.')

def rmse_using_mu(y_train, y_validate):
    # create baseline for train using mean
    y_train['engage_pred_mean'] = y_train['engagement'].mean()
    # create baseline for validate using mean
    y_validate['engage_pred_mean'] = y_validate['engagement'].mean()
    # RMSE of engage_pred_mean
    rmse_train_mu = mean_squared_error(y_train.engagement,
                                    y_train.engage_pred_mean) ** .5
    rmse_validate_mu = mean_squared_error(y_validate.engagement,
                                          y_validate.engage_pred_mean) ** (0.5)
    print(f"""RMSE using Mean
    Train/In-Sample: {round(rmse_train_mu, 2)} 
    Validate/Out-of-Sample: {round(rmse_validate_mu, 2)}""")
    return rmse_train_mu, rmse_validate_mu

def create_models_df(rmse_train_mu, rmse_validate_mu, y_train, y_validate):
    metric_df = pd.DataFrame(data=[
        {'model': 'mean_baseline',
         'RMSE_train': rmse_train_mu,
         'RMSE_validate': rmse_validate_mu,
         'R2_validate': explained_variance_score(y_validate.engagement,
                                             y_validate.engage_pred_mean)
    }]
    )
    return metric_df

def rmse_using_ols(X_train, y_train, X_validate, y_validate):
    # drop username to be able to use ols model
    X_train = X_train.drop(columns=['username'])
    X_validate = X_validate.drop(columns=['username'])
    # make the thing
    lm = LinearRegression()
    # fit the thing
    OLSmodel = lm.fit(X_train, y_train.engagement)
    # use the thing
    y_train['engage_pred_lm'] = lm.predict(X_train)
    # evaluatge the thing - RMSE
    rmse_train = mean_squared_error(y_train.engagement, y_train.engage_pred_lm)**(1/2)
    # predict validate
    y_validate['engage_pred_lm'] = lm.predict(X_validate)
    # evaluate: RMSE
    rmse_validate = mean_squared_error(y_validate.engagement,
                                       y_validate.engage_pred_lm)**(1/2)
    print(f"""RMSE for OLS using LinearRegression
    Training/In-Sample:  {rmse_train} 
    Validation/Out-of-Sample: {rmse_validate}""")
    return rmse_train, rmse_validate

def add_to_models_df(model, metric_df, rmse_train, y_train, rmse_validate, y_validate):
    metric_df = metric_df.append(
        {'model': model,
         'RMSE_train': rmse_train,
         'RMSE_validate': rmse_validate,
         'R2_validate': explained_variance_score(y_validate.engagement,
                                             y_validate.engage_pred_lm)
        }, ignore_index=True)
    return metric_df

def rmse_using_lassolars(X_train, y_train, X_validate, y_validate):
    # drop username to be able to use model
    X_train = X_train.drop(columns=['username'])
    X_validate = X_validate.drop(columns=['username'])
    # make the thing
    lars = LassoLars(alpha=0.01)
    # fit the thing
    lars.fit(X_train, y_train.engagement)
    # use the thing
    y_train['engage_pred_lars'] = lars.predict(X_train)
    # Evaluate: RMSE
    rmse_train = mean_squared_error(y_train.engagement, y_train.engage_pred_lars) ** (1/2)
    # repeat 2-3
    # predict validate
    y_validate['engage_pred_lars'] = lars.predict(X_validate)
    # evaluate: RMSE
    rmse_validate = mean_squared_error(y_validate.engagement,
                                       y_validate.engage_pred_lars) ** (1/2)
    print(f"""RMSE for Lasso + Lars
    _____________________
    Training/In-Sample: {rmse_train}, 
    Validation/Out-of-Sample:  {rmse_validate}
    Difference:  {rmse_validate - rmse_train}""")
    return rmse_train, rmse_validate



