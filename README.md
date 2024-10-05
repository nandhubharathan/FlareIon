# FlareIon_oneAPI_hack_kpr
This is a prediction model which predict next flare occurrence of the user 

## Description
This is a prediction model which predicts the next flare occurrence of the user using a set of data.The RandomForestRegressor algorithm is trained for the prediction 

## Table Of Contents
- ### [Installation](#Installation)
- ### [Usage](#Usage)
- ### [Features](#Features)
- ### [Model Details](#Model-Details)
- ### [Contributing](#Contributing)
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

## Model Features
This project uses a Random Forest Regressor to predict the number of days until the next flare.

- Target Variable: Days Until Next Flare
- Features: Patient demographic and medical history data
- Excluded Features: Flare Frequency, Flare Time Period

### Training and Evaluation
The model was trained using a dataset of historical patient data. The following performance metrics were achieved:

Mean Absolute Error: 0.21
R-squared: 1.5

## Contributing
Contributions are welcome! To contribute:

1.Fork the repository.
2.Create a new branch (git checkout -b feature-branch).
3.Commit your changes (git commit -m "Add feature").
4.Push to the branch (git push origin feature-branch).
5.Create a new Pull Request.

## Contact
For questions, feel free to reach out at:

Email: nandhubharathan2513@gmail.com
GitHub: nandhubharathan



