# FlareIon_oneAPI_hack_kpr
This is a prediction model which predict next flare occurrence of the user 

## Description
This is a prediction model which predicts the next flare occurrence of the user using a set of data.The RandomForestRegressor algorithm is trained for the prediction 

## Table Of Contents
- ### [Installation](#Installation)
- ### [Usage](#Usage)
- ### [Features](#Features)
- ### [Configuration](#Configuration)
- ### [Model Details](#Model-Details)
- ### [Genomic Data Integration](Genomic-Data-Integration)
- ### [Contributing](#Contributing)
- ### [License](#License)
- ### [Contact](#Contact)

## Installation
To get started with the project , clone the repository and install the required dependencies.
```bash
git clone https://github.com/nandhubharathan/FlareIon_oneAPI_hack_kpr.git
cd FlareIon_oneAPI_hack_kpr
pip install -r requirements.txt
```
Ensure you have the following dependencies
- Python
- pandas
- scikit-learn
- scikit-learn-intelex
- streamlit
- joblib

## Usage 
To run the model,use the following command
```bash
streamlit run predict2.py
```
## Features
- Predictive Model:predicts "Days Until Next Flare" using patient data.
- Genomic Data Integration: inproves predictions by incorporating patient genetic profiles.
- Customizable: Ability to configure model parameters(eg.number of estimations,depth).
- Error Reduction: Current model achieves the lowest error rate based on multiple optimizations.

```bash
{
    "n_estimators": 100,
    "max_depth": 10,
    "genomic_data_integration": true
}
```bash
python run_model.py --n_estimators 100 --max_depth 10 --genomic_data true
```

