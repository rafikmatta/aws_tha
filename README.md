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

The inference service was built using FastAPI and deployed to Amazon AppRunner. It works as a hosted serviced and can provide a basic result 
once a properly formatted JSON object is sent to the "predict" end point as follows:

The DevOps pipeline is primarily being taken care of by Amazon AppRunner in this case which is actively monitoring GitHub and 
is pulling the latest changes to the service to be deployed. 

## TODO to get to production:
- Model Versioning 
- API Versioning 
- Regression Tests of the service
- Model Monitoring 
    - Monitor API logs to track how the model is making predictions
    - Regularly pass in labeled data to test output consistency and to see if there a degradation in model accuracy
    