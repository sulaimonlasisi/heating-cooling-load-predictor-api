import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=UserWarning)
    import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from joblib import dump
data_file = "ENB2012_data.csv"


def trainModel(data_file):

    # read csv and get X, Y
    df = pd.read_csv(data_file)
    feature_list = [f"X{idx}" for idx in range(1,9)]
    target_list = [f"Y{idx}" for idx in range(1,3)]
    Y = df[target_list]
    X = df[feature_list]

    # train test split and shuffle data
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.25, random_state=0)
    
    # run linear regression
    linear_reg = LinearRegression()
    linear_reg.fit(X_train, Y_train)

    dump(linear_reg, 'linear_reg.joblib')

trainModel(data_file)