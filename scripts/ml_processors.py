import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import FunctionTransformer

class ML_Processor:
    """
    provides transformer functions for machine learning.
    """
    def __init__(self) -> None:
        pass
    
    
    # def drop_cols(self, df ):
    #     columns_to_be_dropped = ['no','SAID_YES']
    #     cleaned = df.drop(columns_to_be_dropped,axis=1)
    #     return cleaned

    
    def sep_cat_num(self, df):
        """
        separates categorical and numerical variables
        """
        categorical_columns = df.select_dtypes(include='object').columns.tolist()
        numerical_columns = df.select_dtypes(exclude='object').columns.tolist()

        return categorical_columns, numerical_columns

    
    def cat_labeler(self, df, cat_cols):
        """
        assigns a numerical label to categorical values
        """
        for column in cat_cols:
            encoder = LabelEncoder()
            df[column] = encoder.fit_transform(df[column])
        
        print("cat_labeler output...\n")
        print(df.head(2))
        print("\n")

        return df


    def scaler(self, df):
        """
        transforms values within 0 to 1 range
        """
        scaling = MinMaxScaler()
        df[:] = scaling.fit_transform(df[:])

        print("scaler output... \n")
        print(df.head(2))
        print("\n")
        
        return df


    def target_feature(self, df, f_r, t):
        """
        target and feature separator
        """
        features = df.iloc[:,f_r[0]:f_r[1]].values
        target = df.iloc[:,t].values
        
        print("target_features output... \n")
        print("features size: {}".format(features.shape))
        print("\n")

        return features, target

    def set_splitter(self, input, test, val, rand_state):
        """
        splits dataset into specified percentages.
        """
        features, target = input
        per_1 = test
        per_2 = (1-test)*val
        x_train, x_test, y_train, y_test = train_test_split(features, target,test_size= per_1,shuffle = True, random_state = rand_state )
        x_train, x_val, y_train, y_val = train_test_split(x_train, y_train,test_size= per_2, shuffle = True, random_state = rand_state)

        print("set_splitter output... \n")
        print("X_train shape: {}".format(x_train.shape))
        print("y_train shape: {}".format(y_train.shape))
        print("x_test shape: {}".format(x_test.shape))
        print("y_test shape: {}".format(y_test.shape))
        print("X_val shape: {}".format(x_val.shape))
        print("y_val shape: {}".format(y_val.shape))


        return [x_train, y_train, x_test, y_test, x_val, y_val]