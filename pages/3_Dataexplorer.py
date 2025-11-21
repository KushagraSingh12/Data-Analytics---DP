import streamlit as st
import seaborn as sns
import pandas as pd

st.set_page_config(page_title="Data Explorer", page_icon="🔎", layout="wide")

st.title("🔎 Data Explorer")

# Load dataset
df = sns.load_dataset("car_crashes")

# Sidebar Filters
st.sidebar.header("Filter Data")
states = st.sidebar.multiselect("Select States", options=df['abbrev'].unique(), default=df['abbrev'].unique())
min_acc, max_acc = st.sidebar.slider("Filter by Total Accidents", 
                                     min_value=int(df['total'].min()), 
                                     max_value=int(df['total'].max()), 
                                     value=(int(df['total'].min()), int(df['total'].max())))

# Apply filters
filtered_df = df[(df['abbrev'].isin(states)) & (df['total'].between(min_acc, max_acc))]

st.subheader("📋 Filtered Dataset")
st.dataframe(filtered_df, use_container_width=True)

# Download Option
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("📥 Download Filtered Data", data=csv, file_name="filtered_car_crashes.csv", mime="text/csv")

