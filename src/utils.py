# load a model
# use a database
# evalulate model

import os
import sys

import numpy as np 
import pandas as pd
import pickle, dill

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

# Saves model
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            # hyperparameter tuning using Grid Search
            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            # Training the model with best hyperparameters recieved from Grid Search CV
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)  

            # Running Inference
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score
        return report

    except Exception as e:
        raise CustomException(e, sys)
    
# Loads model in memory
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj) # We can also use dill to load

    except Exception as e:
        raise CustomException(e, sys)
