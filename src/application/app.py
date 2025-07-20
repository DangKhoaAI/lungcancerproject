import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# --- Path setup ---
APP_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = APP_DIR.parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "cancerpatientdatasets.csv"

from introduction import show_introduction
from visualization import show_visualization
from prediction import show_prediction
from chatbot import show_chatbot

# Load the dataset
df = pd.read_csv(DATA_PATH)

# Page configuration
st.set_page_config(page_title="Lung Cancer Prediction", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
tabs = ["Introduction", "Visualization", "Model Prediction", "Chatbot"]
selected_tab = st.sidebar.radio("Go to", tabs)

if selected_tab == "Introduction":
    show_introduction()
elif selected_tab == "Visualization":
    show_visualization(df)
elif selected_tab == "Model Prediction":
    show_prediction() 
elif selected_tab == "Chatbot":
    show_chatbot()
