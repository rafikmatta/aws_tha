from pydantic import BaseModel
from fastapi import FastAPI
import pandas as pd
import pickle
import uvicorn
from datetime import datetime

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


class MaintenanceMetrics(BaseModel):
    metric1: int
    metric_2: float
    metric_3: float
    metric_4: float
    metric_5: float
    metric_6: float
    metric_7: float
    metric_8: float
    metric_9: float


# Instantiating FastAPI
api = FastAPI()


# Defining a test root path and message
@api.get('/')
def root():
    return {'message': 'Hello Amazon Hiring Team!'}


# Defining a test root path and message
@api.get('/health')
def health():
    return {'status': 'UP'}


# Defining the prediction endpoint without data validation
@api.post('/predict/')
async def basic_predict(m: MaintenanceMetrics):
    with open("model.pickle", 'rb') as f:
        lr_model = pickle.load(f)

    # Getting the JSON from the body of the request
    # Getting the prediction from the Logistic Regression model
    input_data = pd.DataFrame([m.dict()])
    pred = lr_model.predict(input_data)[0]
    pred_prob = lr_model.predict_proba(input_data)[0][pred]
    if pred == 1:
        pred_class = "Failure"
    else:
        pred_class = "Non-Failure"

    result = {"timestamp": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), "class": pred_class, "probability": str(pred_prob*100) + "%"}
    return JSONResponse(content=result)


if __name__ == '__main__':
    uvicorn.run(api, host='127.0.0.1', port=8000)
