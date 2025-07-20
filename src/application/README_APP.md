# Lung Cancer Prediction Web App

## Project Overview (Giới thiệu chung)

This project is a web application designed to predict the likelihood of lung cancer based on user-provided health data. It also offers exploratory data analysis (EDA) of the dataset used for training the prediction model and a chatbot for answering questions related to lung cancer. The primary goal is to provide an accessible and user-friendly tool for preliminary assessment and information dissemination.

## Project Structure (Cấu trúc thư mục)

```
├───app.py
├───chatbot.py
├───eda.py
├───introduction.py
├───prediction.py
├───README_APP.md
├───README.md
├───visualization.py
├───__pycache__/
├───info/
│   ├───datades.md
│   └───intro.md
└───model/
    ├───adaboost_model.pkl
    └───random_forest_model.pkl
```

-   **app.py**: The main entry point of the Streamlit web application. It orchestrates the different modules and tabs.
-   **chatbot.py**: Contains the logic for the chatbot feature, which answers user questions about lung cancer.
-   **eda.py**: Implements the Exploratory Data Analysis tab, showcasing visualizations and insights from the dataset.
-   **introduction.py**: Displays the introductory content of the application.
-   **prediction.py**: Handles the lung cancer prediction logic based on user input and the trained models.
-   **visualization.py**: A utility module for creating various plots and charts used in the EDA tab.
-   **info/**: A directory containing markdown files for displaying static information on the web app.
    -   **datades.md**: Markdown file with a description of the dataset.
    -   **intro.md**: Markdown file for the introduction page.
-   **model/**: This directory stores the pre-trained machine learning models.
    -   **adaboost_model.pkl**: The saved AdaBoost classifier model.
    -   **random_forest_model.pkl**: The saved Random Forest classifier model.

## Installation Guide (Hướng dẫn cài đặt)

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd lung_cancer_project/src/application
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

## Usage (Cách sử dụng)

Once the application is running, you can navigate through the different tabs on the sidebar:

-   **Introduction**: Read the project overview and description.
-   **EDA (Exploratory Data Analysis)**: Explore interactive charts and summaries of the lung cancer dataset.
-   **Predict**: Input your health parameters into the form and click "Predict" to see the lung cancer risk assessment.
-   **Chatbot**: Ask questions about lung cancer in the chat interface to get responses from the AI-powered chatbot.

## Feature List (Tính năng)

-   **Lung Cancer Prediction**: Predicts the likelihood of lung cancer using two different ML models (Random Forest and AdaBoost).
-   **Exploratory Data Analysis (EDA)**: Provides a detailed analysis of the dataset with various visualizations.
-   **Interactive Chatbot**: An AI-powered chatbot to answer user queries about lung cancer.
-   **User-Friendly Interface**: A simple and intuitive web interface built with Streamlit.
-   **Multi-page Layout**: A clean, organized multi-page layout for easy navigation.

## Function/Module Descriptions (Giải thích hàm / module)

-   **app.py**: This is the main script that runs the Streamlit application. It uses the `streamlit_option_menu` to create the sidebar navigation and calls the functions from other modules to display the content of each tab.
-   **introduction.py**: Contains the `show_introduction()` function, which reads and displays the content from the markdown files in the `info/` directory.
-   **eda.py**: The `show_eda()` function loads the dataset and uses functions from `visualization.py` to display various plots and data summaries.
-   **prediction.py**: The `show_prediction()` function creates a form for user input, loads the pre-trained models, and displays the prediction results.
-   **chatbot.py**: The `show_chatbot()` function sets up the chatbot interface, handles user input, and uses a language model to generate responses.
-   **visualization.py**: This module contains functions for creating different types of plots like histograms, bar charts, and correlation heatmaps.

## Tab/Web Page Descriptions

-   **Introduction**: This tab serves as the landing page, providing a general introduction to the project, its objectives, and the dataset used.
-   **EDA (Exploratory Data Analysis)**: This section is dedicated to data exploration. It includes various visualizations that help in understanding the distribution of data, the relationship between different features, and other key insights from the dataset.
-   **Predict**: This is the core functional tab where users can input their health information (e.g., age, smoking habits, and other medical indicators) to get a prediction on their lung cancer risk.
-   **Chatbot**: An interactive feature where users can ask questions related to lung cancer and receive informative answers from an AI chatbot.