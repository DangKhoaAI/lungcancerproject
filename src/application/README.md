# Application Directory Structure

This directory contains the source code for the Streamlit web application, which serves as the user interface for the lung cancer prediction project.

## File Descriptions

-   `app.py`: The main entry point for the Streamlit application. It handles the overall page structure, navigation sidebar, and model selection. It imports and calls functions from the other modules to render the selected page.

-   `introduction.py`: Contains the function `show_introduction()` which is responsible for displaying the project's business case and problem statement. It reads the detailed content from the `info/intro.md` file.

-   `visualization.py`: Implements the `show_visualization()` function. This page allows users to explore the dataset through various interactive plots, such as feature comparisons and a correlation heatmap.

-   `prediction.py`: Defines the `show_prediction()` function. This module presents a user-friendly form where users can input patient data. It then uses the selected pre-trained model to predict the level of lung cancer risk (Low, Medium, High).

-   `chatbot.py`: Implements the `show_chatbot()` function. This module provides a simple, rule-based chatbot to answer basic user questions.

## Subdirectories

### `info/`

This directory stores static content files used by the application.

-   `intro.md`: A Markdown file containing the detailed business understanding, problem statement, and value proposition of the project. This content is displayed on the "Introduction" page.

### `model/`

This directory contains the serialized, pre-trained machine learning models.

-   `random_forest_model.pkl`: The saved Random Forest classifier model.
-   `adaboost_model.pkl`: The saved AdaBoost classifier model.
