import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import shap
from pathlib import Path


def show_prediction():
    st.title("Lung Cancer Prediction With AI")

    # ======= 1. Choose Model =======
    model_options = ["Random Forest", "AdaBoost"]
    selected_model = st.selectbox("📦 Choose a model", model_options)

    APP_DIR = Path(__file__).resolve().parent
    model_path = APP_DIR / "model" / (
        "random_forest_model.pkl" if selected_model == "Random Forest" else "adaboost_model.pkl"
    )
    model = joblib.load(model_path)

    # ======= 2. Feature Importance (Global) =======
    with st.expander("📊 Show Model Feature Importance"):
        if hasattr(model, 'feature_importances_'):
            importances = model.feature_importances_
            features = [
                'Age', 'Gender', 'Air Pollution', 'Alcohol use', 'Dust Allergy',
                'OccuPational Hazards', 'Genetic Risk', 'chronic Lung Disease', 'Balanced Diet',
                'Obesity', 'Smoking', 'Passive Smoker', 'Chest Pain', 'Coughing of Blood',
                'Fatigue', 'Weight Loss', 'Shortness of Breath', 'Wheezing',
                'Swallowing Difficulty', 'Clubbing of Finger Nails',
                'Frequent Cold', 'Dry Cough', 'Snoring'
            ]
            indices = np.argsort(importances)

            fig, ax = plt.subplots(figsize=(8, 6))
            ax.barh(range(len(indices)), importances[indices], color="skyblue")
            ax.set_yticks(range(len(indices)))
            ax.set_yticklabels([features[i] for i in indices])
            ax.set_xlabel("Importance")
            ax.set_title("Feature Importance ")
            st.pyplot(fig)
        else:
            st.info("This model does not support feature importances.")
    # ========== FEATURE DESCRIPTION ================
    with st.expander("📝 Feature Description"):
        try:
            with open("info/datades.md", "r", encoding="utf-8") as f:
                st.markdown(f.read(), unsafe_allow_html=True)
        except FileNotFoundError:
            st.warning("⚠️ Không tìm thấy file mô tả `datades.md`. Vui lòng kiểm tra đường dẫn.")

    # ======= 3. Input Form + Predict Button =======
    def user_input_features():
        with st.expander("📝 Enter Patient Data"):
            col1, col2 = st.columns(2)

            with col1:
                age = st.slider("Age", 1, 100, 50)
                air_pollution = st.slider("Air Pollution", 1, 8, 4)
                alcohol_use = st.slider("Alcohol Use", 1, 8, 4)
                dust_allergy = st.slider("Dust Allergy", 1, 8, 4)
                occupational_hazards = st.slider("Occupational Hazards", 1, 8, 4)
                genetic_risk = st.slider("Genetic Risk", 1, 7, 3)
                chronic_lung_disease = st.slider("Chronic Lung Disease", 1, 7, 3)
                balanced_diet = st.slider("Balanced Diet", 1, 7, 3)
                obesity = st.slider("Obesity", 1, 7, 3)
                smoking = st.slider("Smoking", 1, 8, 4)
                passive_smoker = st.slider("Passive Smoker", 1, 8, 4)

            with col2:
                gender = st.selectbox("Gender", ["Male", "Female"])
                chest_pain = st.slider("Chest Pain", 1, 9, 5)
                coughing_of_blood = st.slider("Coughing of Blood", 1, 9, 5)
                fatigue = st.slider("Fatigue", 1, 9, 5)
                weight_loss = st.slider("Weight Loss", 1, 8, 4)
                shortness_of_breath = st.slider("Shortness of Breath", 1, 9, 5)
                wheezing = st.slider("Wheezing", 1, 8, 4)
                swallowing_difficulty = st.slider("Swallowing Difficulty", 1, 8, 4)
                clubbing_of_finger_nails = st.slider("Clubbing of Finger Nails", 1, 9, 5)
                frequent_cold = st.slider("Frequent Cold", 1, 7, 3)
                dry_cough = st.slider("Dry Cough", 1, 7, 3)
                snoring = st.slider("Snoring", 1, 7, 3)

        data = {
            'Age': age,
            'Gender': 1 if gender == "Male" else 2,
            'Air Pollution': air_pollution,
            'Alcohol use': alcohol_use,
            'Dust Allergy': dust_allergy,
            'OccuPational Hazards': occupational_hazards,
            'Genetic Risk': genetic_risk,
            'chronic Lung Disease': chronic_lung_disease,
            'Balanced Diet': balanced_diet,
            'Obesity': obesity,
            'Smoking': smoking,
            'Passive Smoker': passive_smoker,
            'Chest Pain': chest_pain,
            'Coughing of Blood': coughing_of_blood,
            'Fatigue': fatigue,
            'Weight Loss': weight_loss,
            'Shortness of Breath': shortness_of_breath,
            'Wheezing': wheezing,
            'Swallowing Difficulty': swallowing_difficulty,
            'Clubbing of Finger Nails': clubbing_of_finger_nails,
            'Frequent Cold': frequent_cold,
            'Dry Cough': dry_cough,
            'Snoring': snoring
        }

        return pd.DataFrame(data, index=[0])

    input_df = user_input_features()

    # ======= 4. Prediction =======
    if st.button("🔍 Predict"):
        pred = model.predict(input_df)[0]
        probs = model.predict_proba(input_df)
        pred_prob = probs[0][pred]  # Xác suất cho class được dự đoán

        label_map = {0: "Low", 1: "Medium", 2: "High"}
        label = label_map[pred]

        st.subheader("🎯 Prediction Result")
        st.write(f"✅ Predicted Class: **{label}**")
        st.write(f"📈 Probability: **{pred_prob:.3f}**")

        if label == "Low":
            st.success(f"Prediction: {label} risk")
        elif label == "Medium":
            st.warning(f"Prediction: {label} risk")
        else:
            st.error(f"Prediction: {label} risk")

        # ====== SHAP Explanation =======
        with st.expander("🧠 SHAP Explanation (Why this result?)"):
            try:
                explainer = shap.TreeExplainer(model)
                shap_values = explainer.shap_values(input_df)

                if isinstance(shap_values, np.ndarray):
                    # Multi-class: shape = (1, n_features, n_classes)
                    values = shap_values[0, :, pred]
                    base_value = explainer.expected_value[pred]
                else:
                    # Trường hợp list[class][samples, features]
                    values = shap_values[pred][0]
                    base_value = explainer.expected_value[pred]

                shap_exp = shap.Explanation(
                    values=values,
                    base_values=base_value,
                    data=input_df.values[0],
                    feature_names=input_df.columns.tolist()
                )

                fig, ax = plt.subplots(figsize=(10, 4))
                shap.plots.waterfall(shap_exp, max_display=15)
                st.pyplot(fig)

            except Exception as e:
                st.warning("SHAP explanation failed.")
                st.exception(e)
