# FlareIon_flare prediction app
this a machine learning-powered web application that predicts the number of days until the next autoimmune flare, based on patient-specific input data such as age, gender, disease type, biomarkers, genetic markers, environmental factors, and medical history.

## Description
This is a prediction model which predicts the next flare occurrence of the user using a set of data.The RandomForestRegressor algorithm is trained for the prediction 

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
The model uses a Random Forest Regressor trained on synthetic medical data to estimate the interval between autoimmune flares.

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



