# Heating and Cooling Load Predictor API

## Overview

## Model

Machine learning regression model that predicts the value of dependent variables - heating load and cooling load. Given 768 samples, we build this model and prepare to use it for serving requests about the model.



## Training

Training was done using 75% of the shuffled dataset. The remaining 25% of data was saved for testing. Experimentation was done using common regression models like Ridge Regression, Lasso Regression and Simple Linear Regression. The outcome of several iterations (15) of experimentation and testing showed that the simple linear regression performed better (90%) when scored and compared against Ridge regression (87%) and Lasso Regression (78%).

## API

Tiny flask server that exposes one endpoint to predict the heating and cooling loads of a building given its important 8 parameters.

The API imports the persisted trained model from above (linear_reg.joblib) and instantiates it so that it can call the predict method on the model object.

## Prediction

Prediction is done at the main endpoint of the app. 
Sample data sent for a `curl` prediction request looks like below:

```
    curl -H "Content-Type: application/json" \
    --request POST \
    --data '{
        "X1": 0.98,
        "X2": 514.50,
        "X3": 294.00,
        "X4": 110.25,
        "X5": 7.00,
        "X6": 2,
        "X7": 0.00,
        "X8": 0
    }' \
    http://localhost:5000/
```

The response to a sample request similar to the one shown above looks like below:

```
    {
      "results": {
        "Cooling Load": 26.25,
        "Heating Load": 23.21
      }
    }

```


## How To Test
  
  - Clone this repo
  - From the root folder where the Dockerfile sits, run `docker build -t hc-app .` to build the app image.
  - Fron the same location, run `docker run -itd -p 5000:5000 hc-app` to run the app in detached mode.
  - From a different terminal, run the prediction request shown above and you should see the response right below it.

