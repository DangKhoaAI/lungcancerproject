# Lung Cancer Analysis and Prediction Platform

This project is a web-based AI application built with Streamlit to analyze patient data, predict the likelihood of lung cancer, and provide a user-friendly interface for interaction.

## Features

- **Data Analysis and Visualization:** Identifies health patterns through statistical analysis and visualizations.
- **Lung Cancer Prediction:** Utilizes a machine learning model to predict the likelihood of lung cancer based on patient data.
- **Interactive Chatbot:** Integrates a chatbot to answer user questions about lung cancer.
- **Web-Based Interface:** Provides a simple and intuitive web interface built with Streamlit.

## Folder Structure

```
lung_cancer_project/
│
├── src/
│   ├── 1_business_understanding/
│   ├── 2_data_preparation/
│   ├── 3.4_EDAandvisualization/
│   ├── 5_modeling/
│   └── application/
├── data/
│   ├── raw/
│   └── processed/
├── reports/
├── requirements.txt
└── README.md
```

## How to Run This Project

### Prerequisites

- Anaconda or Miniconda

### 1. Set Up the Environment

First, you need to set up the conda environment. Open your terminal and run the following commands from the project's root directory:

1.  **Create and activate the conda environment:**
    ```bash
    conda create -n dap_lungcancer python=3.10 -y
    conda activate dap_lungcancer
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### 2. Run the Project Scripts

Once the environment is set up, run these scripts in order to ensure the data is processed and the model is trained:

1.  **Preprocess the data:**
    ```bash
    python src/2_data_preparation/preprocessing.py
    ```

2.  **Train the prediction model:**
    ```bash
    python src/5_modeling/train_model.py
    ```

### 3. Start the Web Application

Finally, start the Streamlit web server:

```bash
streamlit run src/application/app.py
```

You can then access the application by opening your web browser and navigating to the local URL provided by Streamlit (usually http://localhost:8501).

### Exploring the Notebooks (Optional)

To view the data analysis and model evaluation notebooks, you can use Jupyter Lab:

1.  **Install JupyterLab (if not already installed):**
    ```bash
    pip install jupyterlab
    ```
2.  **Run JupyterLab:**
    ```bash
    jupyter lab
    ```
    Then, navigate to the `src/3.4_EDAandvisualization` and `src/5_modeling` directories to explore the notebooks./