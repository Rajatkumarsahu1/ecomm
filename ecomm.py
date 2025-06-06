import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def main():
    st.title("🛒 E-commerce Business Data Explorer")
    st.sidebar.title("Upload Your File")
    
    uploaded_file = st.sidebar.file_uploader("Upload your CSV or Excel file", type=['csv', 'xlsx'])
    
    if uploaded_file is not None:
        try:
            # Load data according to file type
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)
            else:
                data = pd.read_excel(uploaded_file)
            
            st.sidebar.success("✅ File uploaded successfully!")
            
            # Show data overview
            st.subheader("📊 Data Overview")
            st.dataframe(data.head())
            
            # Basic info
            st.subheader("ℹ️ Basic Information")
            st.write(f"Shape of the data: {data.shape}")
            st.write(f"Columns: {list(data.columns)}")
            st.write("Missing values per column:")
            st.write(data.isnull().sum())
            
            # Descriptive statistics
            st.subheader("📈 Statistical Summary")
            st.write(data.describe())
            
            # Optional: show a correlation heatmap if numeric columns exist
            numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
            if len(numeric_cols) > 1:
                st.subheader("🔗 Correlation Heatmap")
                fig, ax = plt.subplots(figsize=(8, 6))
                sns.heatmap(data[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
                st.pyplot(fig)
            else:
                st.info("Not enough numeric columns to display correlation heatmap.")
                
        except Exception as e:
            st.error(f"⚠️ Oops! Something went wrong: {e}")

if __name__ == "__main__":
    main()
