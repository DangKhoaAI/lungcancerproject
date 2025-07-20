import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

def show_visualization(df):
    st.title("Data Visualization")

    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(exclude=['number']).columns.tolist()

    # ========== RAW DATA ================
    with st.expander("🗂️ Show Raw Data (Nhấn để mở bảng dữ liệu gốc)"):
        st.dataframe(df)
        st.markdown("---")


    # ========== FEATURE DESCRIPTION ================
    with st.expander("📝 Feature Description"):
        try:
            with open("info/datades.md", "r", encoding="utf-8") as f:
                st.markdown(f.read(), unsafe_allow_html=True)
        except FileNotFoundError:
            st.warning("⚠️ Không tìm thấy file mô tả `datades.md`. Vui lòng kiểm tra đường dẫn.")
    # ========== FEATURE COMPARISON ===============
    with st.expander("📊 Feature Comparison"):
        st.subheader("Choose Features to Compare")

        features = st.multiselect(
            "Select features", 
            options=df.columns.tolist(), 
            default=[df.columns[0]]
        )

        plot_type = st.selectbox("Plot type", [
            "Bar Chart", 
            "Grouped Bar Chart", 
            "Grouped Count Bar Chart",  
            "Histogram", 
            "Boxplot"
        ])  # ❌ Đã xóa "Line Chart"

        if len(features) == 0:
            st.warning("Please select at least one feature.")
        else:
            if plot_type == "Histogram":
                for feat in features:
                    fig, ax = plt.subplots(figsize=(8, 4))
                    sns.histplot(df[feat], kde=True, bins=20, ax=ax, color='skyblue')
                    ax.set_title(f"Histogram & KDE for {feat}")
                    st.pyplot(fig)

            elif plot_type == "Boxplot":
                if 'Level' not in df.columns:
                    st.warning("Boxplot yêu cầu cột 'Level' để phân nhóm.")
                else:
                    for feat in features:
                        fig, ax = plt.subplots(figsize=(8, 4))
                        sns.boxplot(
                            x='Level', y=feat, data=df, ax=ax,
                            palette='Set3'
                        )
                        ax.set_title(f"{feat} vs Risk Level (Boxplot)")
                        st.pyplot(fig)

            elif plot_type == "Bar Chart" and len(features) == 1:
                st.bar_chart(df[features[0]].value_counts())

            elif plot_type == "Grouped Count Bar Chart":
                if len(features) != 1:
                    st.warning("Chọn đúng 1 feature để vẽ biểu đồ.")
                elif 'Level' not in df.columns:
                    st.warning("Dataset cần có cột 'Level' để vẽ biểu đồ.")
                else:
                    feat = features[0]

                    # Dùng trực tiếp Level làm hue
                    fig, ax = plt.subplots(figsize=(10, 5))
                    sns.countplot(
                        data=df,
                        x=feat,
                        hue='Level',
                        palette='inferno',
                        ax=ax
                    )
                    ax.set_title(f"Patient Count by {feat} Grouped by Risk Level", fontsize=14)
                    ax.set_xlabel(feat)
                    ax.set_ylabel("Count")
                    ax.legend(title="Level")
                    plt.xticks(rotation=45)
                    st.pyplot(fig)
            
            elif plot_type == "Grouped Bar Chart":
                if len(features) != 1:
                    st.warning("Grouped Bar Chart yêu cầu chọn đúng 1 feature.")
                elif 'Level' not in df.columns:
                    st.warning("Dataset cần có cột 'Level' để vẽ biểu đồ.")
                else:
                    feat = features[0]

                    # Dùng trực tiếp cột 'Level' làm phân nhóm cột nhỏ
                    g = sns.catplot(
                        data=df,
                        x=feat,
                        col='Level',  # Không cần tạo cột Level_str nữa
                        kind='count',
                        col_order=['Low', 'Medium', 'High'],
                        color='skyblue',
                        height=4,
                        aspect=0.9
                    )
                    g.set_titles("{col_name} Risk")
                    g.set_axis_labels(feat, "Count")
                    g.figure.suptitle(f"Patient Count by {feat} Across Risk Levels", y=1.05, fontsize=14)
                    plt.tight_layout()
                    st.pyplot(g.figure)


            else:
                st.info("Biểu đồ này yêu cầu đúng định dạng đầu vào.")




    # ========== CORRELATION HEATMAP ==========
    with st.expander("🧠 Correlation Heatmap"):
        st.subheader("Correlation Matrix")

        method = st.selectbox("Correlation Method", ["pearson", "spearman"])
        selected_cols = st.multiselect("Select columns for correlation", numeric_cols, default=numeric_cols)

        if len(selected_cols) < 2:
            st.warning("Vui lòng chọn ít nhất 2 cột số.")
        else:
            corr = df[selected_cols].corr(method=method)
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(corr, fmt=".2f", cmap="coolwarm", ax=ax)
            ax.set_title(f"{method.capitalize()} Correlation Matrix")
            st.pyplot(fig)
