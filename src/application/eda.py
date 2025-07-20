import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_grouped_bar_count(df: pd.DataFrame, feature: str):
    """
    Vẽ biểu đồ cột phân nhóm (countplot) theo `feature` và `Level`.

    Parameters:
    - df: pandas DataFrame chứa dữ liệu
    - feature: tên cột phân loại đầu vào (str)
    """

    # Kiểm tra điều kiện dữ liệu
    if feature not in df.columns:
        raise ValueError(f"Feature '{feature}' không tồn tại trong DataFrame.")
    if 'Level' not in df.columns:
        raise ValueError("Cột 'Level' phải có trong DataFrame.")

    # Ánh xạ nhãn nếu Level đang là số
    if df['Level'].dtype in [int, float]:
        df['Level_str'] = df['Level'].map({0: 'Low', 1: 'Medium', 2: 'High'})
    else:
        df['Level_str'] = df['Level']

    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x=feature, hue='Level_str', palette='inferno')
    plt.title(f"Patient Count by {feature} Grouped by Risk Level", fontsize=16)
    plt.xlabel(feature)
    plt.ylabel("Count")
    plt.legend(title="Level")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_faceted_bar_count(df: pd.DataFrame, feature: str):
    """
    Vẽ biểu đồ `catplot` chia theo từng Level (Low, Medium, High) với feature đầu vào.

    Parameters:
    - df: pandas DataFrame chứa dữ liệu
    - feature: tên cột phân loại đầu vào (str)
    """

    if feature not in df.columns:
        raise ValueError(f"Feature '{feature}' không tồn tại trong DataFrame.")
    if 'Level' not in df.columns:
        raise ValueError("Cột 'Level' phải có trong DataFrame.")

    if df['Level'].dtype in [int, float]:
        df['Level_str'] = df['Level'].map({0: 'Low', 1: 'Medium', 2: 'High'})
    else:
        df['Level_str'] = df['Level']

    g = sns.catplot(
        data=df,
        x=feature,
        kind="count",
        col="Level_str",
        col_order=["Low", "Medium", "High"],
        palette="viridis",
        height=5,
        aspect=0.8
    )
    g.set_titles("{col_name} Risk")
    g.set_axis_labels(feature, "Count")
    g.fig.suptitle(f"Patient Count by {feature} Across Risk Levels", y=1.05, fontsize=16)
    plt.tight_layout()
    plt.show()


# ========== TEST SAMPLE ==========
if __name__ == "__main__":
    # Đọc dữ liệu mẫu để kiểm tra
    df = pd.read_csv("/mnt/data/FPTStudy/Semester4/DAP391m/project/lung_cancer_project/data/raw/cancerpatientdatasets.csv")  # ← thay bằng đường dẫn thật

    feature = "Alcohol use"  # ← bạn có thể thay thành "Smoking", "Obesity", ...

    plot_grouped_bar_count(df, feature)
    plot_faceted_bar_count(df, feature)
