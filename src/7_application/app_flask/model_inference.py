
import pickle
import pandas as pd

def predict_lung_cancer(data):
    """
    Loads the trained model and makes a prediction on the input data.

    Args:
        data (dict): A dictionary containing the input data.

    Returns:
        int: The prediction (0 for low risk, 1 for high risk).
    """
    # Load the trained model
    with open('../5_modeling/model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Convert the input data to a pandas DataFrame
    df = pd.DataFrame([data])

    # Make a prediction
    prediction = model.predict(df)[0]

    return prediction
