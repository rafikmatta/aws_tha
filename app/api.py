from pydantic import BaseModel
from fastapi import FastAPI, Response, status
import pandas as pd
from joblib import load


class MaintenanceMetrics(BaseModel):
    metric1: float
    metric2: float
    metric3: float
    metric4: float
    metric5: float
    metric6: float
    metric7: float
    metric8: float
    metric9: float


# Instantiating FastAPI
api = FastAPI()


# Defining a test root path and message
@api.get('/')
def root():
    return {'message': 'Hello Amazon Hiring Team!'}


# Defining the prediction endpoint without data validation
@api.post('/predict/')
async def basic_predict(m: MaintenanceMetrics):
    lr_model = load('model.joblib')
    # Getting the JSON from the body of the request
    # Getting the prediction from the Logistic Regression model
    input_data = pd.DataFrame([m.dict()])
    return lr_model.predict(input_data)[0]
