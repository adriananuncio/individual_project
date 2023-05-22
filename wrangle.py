# standard imports
import numpy as np
import pandas as pd
# train, test, split
from sklearn.model_selection import train_test_split

# --------------------------------------------------------------------------------
# Acquire
def import_df(csv_file):
    ''' This function will import and return a specified csv file 
        as a pandas dataframe. It will also summarize the dataframe
        through print statements.'''
    df = pd.read_csv(csv_file)
    # summarize data/ inital glace at data
    print('_'*50)
    print(f'Shape: \n{df.shape}')
    print('_'*50)
    print(f'Stats: \n{df.describe().T}')
    print('_'*50)
    print('Info: ')
    print(df.info())
    print('_'*50)
    print(f'Data Types: \n{df.dtypes}')
    print('_'*50)
    print(f'Null Values: \n{df.isnull().sum()}')
    print('_'*50)
    print(f'NA Values: \n{df.isna().sum()}')
    print('_'*50)
    print(f'Unique Value Count: \n{df.nunique()}')
    print('_'*50)
    print(f'Columns: \n{df.columns}')
    print('_'*50)
    print(f'Column Value Counts: \n{df.columns.value_counts(dropna=False)}')
    print('_'*50)
    return df

# --------------------------------------------------------------------------------
# Prepare
def prep_data(df):
    '''This function will drop columns: Tiktok Link and name using their index. Next the function will format column titles to be all lowercase, snakecase, and remove periods. Next columns will be renamed for simplicity, and numeric column dtypes are changed to be numeric and formated for use in regression modeling. Lastly, duplicate rows are dropped and column: engagement is created.'''
    # drop Tiktok Link and name using their index - 2, 3
    df = df.drop(df.columns[[2,3]], axis=1)
    # format column names to be all lowercase
    # format column names to be in snakecase
    # remove . from column names
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('.', '')
    # rename columns
    df = df.rename(columns={'subscribers_count': 'subscribers'
                       , 'views_avg': 'views'
                       , 'likes_avg': 'likes'
                       , 'comments_avg': 'comments'
                       , 'shares_avg': 'shares'})
    # convert subscribers, views, likes, comments, and shares to be numeric
    def convert_to_numeric(value):
        if isinstance(value, str):
            if value[-1] == 'M':
                return float(value[:-1]) * 1000000
            elif value[-1] == 'K':
                return float(value[:-1]) * 1000
            else:
                return float(value)
        else:
            return value
    df['subscribers'] = df['subscribers'].apply(convert_to_numeric)
    df['views'] = df['views'].apply(convert_to_numeric)
    df['likes'] = df['likes'].apply(convert_to_numeric)
    df['comments'] = df['comments'].apply(convert_to_numeric)
    df['shares'] = df['shares'].apply(convert_to_numeric)
    # drop specified duplicates
    df = df.drop([100, 101, 102], axis=0)
    # create total engagement column 
    # this column will be the sum of engagement metrics:
    # views, likes, comments, and shares.
    df['engagement'] = df['subscribers'] + df['views'] + df['likes'] + df['comments'] + df['shares']
    return df

# --------------------------------------------------------------------------------
# train, test, split
def train_validate_test(df, target):
    '''
    this function takes in a dataframe and splits it into 3 samples, 
    a test, which is 20% of the entire dataframe, 
    a validate, which is 24% of the entire dataframe,
    and a train, which is 56% of the entire dataframe. 
    It then splits each of the 3 samples into a dataframe with independent variables
    and a dataframe with the dependent, or target variable. 
    The function returns 6 dataframes:
    X_train & y_train, X_validate & y_validate, X_test & y_test. 
    '''
    # split df into test (20%) and train_validate (80%)
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    # split train_validate off into train (70% of 80% = 56%) and validate (30% of 80% = 24%)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)
    # split train into X (dataframe, drop target) & y (series, keep target only)
    X_train = train.drop(columns=[target])
    y_train = train[target].to_frame(name='engagement')
    # split validate into X (dataframe, drop target) & y (series, keep target only)
    X_validate = validate.drop(columns=[target])
    y_validate = validate[target].to_frame(name='engagement')
    # split test into X (dataframe, drop target) & y (series, keep target only)
    X_test = test.drop(columns=[target])
    y_test = test[target].to_frame(name='engagement')
    return X_train, y_train, X_validate, y_validate, X_test, y_test
