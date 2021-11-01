# AWS Take Home Assignement - Rafik Matta

## Model Development
We have a classification problem with 2 classes. Failure and Non- Failure of the device. After some exploratory data analysis 
two major points stand out:
- There is a massive class imbalance favouring the Non-Failure class
- We need to better understand what each of the features labeled "metric" as those numbers are almost meaningless
- It is challenging to do feature engineering/selection without the previous point being addressed

Overall, a Logistic Regression model was chosen and seemed to perform well from an accuracy perspective, but the ROC curve shows us
that it's not really doing much in the way of classification. 

## Model Deployment into a Development Environment

The inference service was built using *FastAPI* and deployed to *Amazon AppRunner*. It works as a hosted service and can provide a basic result 
once a properly formatted JSON object is sent to the "predict" end point as follows:

The DevOps pipeline is primarily being taken care of by Amazon AppRunner in this case which is actively monitoring GitHub and 
is pulling the latest changes to the service to be deployed. 

## TODO to get to production:
- Add logging to API
- Model Versioning 
- API Versioning 
- Regression Tests of the service
- Model Monitoring 
    - Monitor API logs to track how the model is performing and making predictions
    - Regularly pass in labeled data to test output consistency and to see if there a degradation in model accuracy
- API Security
    
    
## Usage:

Below is a usage example of how to call the API. To see the available endpoints you can go to the API docs. You can access these if the API
is locally deployed by going to the following:

http://localhost:8080/docs

Or you can access it at the hosted version here:

https://x3ipkw9r3p.us-east-1.awsapprunner.com/docs

### Input via CURL:
```sh
curl -X 'POST' \
  'http://https://x3ipkw9r3p.us-east-1.awsapprunner.com/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "metric1": 215630672,
  "metric2": 56,
  "metric3": 0,
  "metric4": 52,
  "metric5": 6,
  "metric6": 407438,
  "metric7": 0,
  "metric9": 7
}'
```

### Expected Response:
```json
{
  "timestamp": "10/31/2021, 23:26:20",
  "class": "Non-Failure",
  "probability": "100.0%"
}
```