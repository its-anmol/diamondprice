import os
import sys
import pickle
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging\

from sklearn.metrics import r2_score

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb")as file_obj:
            pickle.dump(obj,file_obj)
    
    except Exception as e:
        raise CustomException(e,sys)

def evaluate_model(x_train,y_train,x_test,y_test,models):
    try:
        report={}
        for i in range(len(models)):
            model=list(models.values())[i]

            #train
            model.fit(x_train,y_train)

            #predict
            y_test_pred=model.predict(x_test)

            #get R2score for test data
            test_model_score=r2_score(y_test,y_test_pred)
            report[list(models.keys())[i]]=test_model_score

        return report
    except Exception as e:
        logging.info('exception occured during model training')
        raise CustomException(e,sys)
    