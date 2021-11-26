# AWS Inference Service Project

## Business Value

This device failure prediction API leverages machine learning to take in real-time device metrics and determine the probability of 
device failure or non-failure.

This can be used and integrated into the companies maintenance solutions to address maintenance needs. It can help prempetively determine
how close a device might be to failure. 

This can save the company hours and money spent on regular maintenance and allow them to build a maintenance process that is more 
ad-hoc in nature. 

## Model Development

We have a classification problem with 2 classes. Failure and Non- Failure of the device. After some exploratory data analysis 
two major points stand out:
- There is a massive class imbalance favouring the Non-Failure class
- We need to better understand what each of the features labeled "metric" as those numbers are almost meaningless
- It is challenging to do feature engineering/selection without the previous point being addressed

Two classification models were tested (Logit and Decision Tree) and Decision Tree was chosen and seemed to perform well from an accuracy perspective, as well as reducing 
false positive and false negative rates as the client requested. That being said, there is some suspicion that model might be 
overfitting and further investigation is needed by doing things such as reviewing validation curves etc. assuming time permits.

We did not use the specific device as a feature. This was an intentional choice. Keeping the model device agnostic helps 
us maintain some flexibility in the prediction. This is assuming that the devices are all essentially the same, but if the metrics
have different meanings per device we would need to adjust the model to incorporate device info.

## Model Deployment into a Development Environment

The inference service was built using *FastAPI* and deployed to *Amazon AppRunner*. It works as a hosted service and can provide a prediction result and probability
of failure/non-failure once a properly formatted JSON object is sent to the "/predict" end point.

The DevOps pipeline is primarily being taken care of by Amazon AppRunner which is actively monitoring GitHub and 
is pulling the latest changes to the service to be deployed. An extension of this in the future would be to make the deployment tagged
and branch specific to ensure we are releasing properly tested versions of the model API.

One thing that is missing from the CI pipeline is automated unit and regression testing. Those can be incorporated in a few different ways
and using different hosted services. These would serve as important gates to deployment to ensure only correct code goes out.

Other important notes for entering production are as follows. 

## TODO to get to production:
- Add logging to API
- Model Versioning (and hosting model files on S3)
- API Versioning (or using GraphQL instead)
- Add unit and regression tests of the service
- Model Monitoring 
    - Monitor API logs to track how the model is performing and making predictions
    - Regularly pass in labeled data to test output consistency and to see if there a degradation in model accuracy
    - Data input monitoring to ensure that the data is valid and within an expected range
- API Authentication and Authorization


## Running the API locally:

You should be running a Python 3.8 or greater environment with all the dependencies listed in the requirements.txt installed. 


Please use the following bash command where your current directory is the root of this folder:

```nashorn js
uvicorn api:api --host 0.0.0.0 --port 5001 --reload
```
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

This API can be called using any HTTP client library for any language. 
