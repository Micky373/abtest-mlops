import pandas as pd
import numpy as np
# To Train our data
from xgboost import XGBClassifier
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix
# To Visualize Data
import matplotlib.pyplot as plt
import seaborn as sns


class ML_Models:
    """
    It returns different models
    """
    def evaluate_model(self, model, df, x_test, y_test, alg):
        pred_xgb = model.predict(x_test)
        accuracy = accuracy_score(pred_xgb, y_test)
        print("The model accuracy is: ", accuracy)
        print("the loss function is: ", model.objective)

        sorted_idx = model.feature_importances_.argsort()
        columns = np.array(df.columns.to_list()[:5])
        plt.barh(columns[sorted_idx], model.feature_importances_[sorted_idx])
        plt.xlabel(alg+" Feature Importance")

    def xgb_model(self, x_train, y_train, x_val, y_val):
        """
        xgb model
        """
        # Define XGBoost Model
        model = XGBClassifier(
        learning_rate =0.08,
        n_estimators=1000,
        eval_metric='rmse',
        )
        
        xgb_param = model.get_xgb_params()
        xgtrain = xgb.DMatrix(x_train, label=y_train)
        cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=model.get_params()['n_estimators'], nfold=5,
            early_stopping_rounds=50)
        model.set_params(n_estimators=cvresult.shape[0])
        # We fit our model with our train data
        model.fit(
            x_train, y_train,
            eval_set=[(x_val, y_val)],
            verbose=False
        )

        return model

    