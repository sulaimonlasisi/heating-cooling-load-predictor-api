# Heating and Cooling Load Predictor API

## Overview

## Model

Machine learning regression model that predicts the value of dependent variables - heating load and cooling load. Given 768 samples, we build this model and prepare to use it for serving requests about the model.

## Training

Training will be done using 80% of the shuffled dataset. Models for each variable will be generated separately.
   
   - TODO:
   - Cross-Validation

## Prediction

Prediction will be done for each variable (heating, cooling) at separate endpoints.

## API

Tiny flask server that exposes endpoints for predicting values for heating and cooling load parameters.

## TODO
