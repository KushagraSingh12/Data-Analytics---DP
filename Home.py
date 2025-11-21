import streamlit as st
import seaborn as sns

# --------------- PAGE CONFIG ----------------
st.set_page_config(
    
    page_title="Car Crash Analysis Dashboard",
    page_icon="🚗",
    layout="wide"
)
 
# Load dataset
df = sns.load_dataset("car_crashes")

# --------------- HERO SECTION ----------------
st.markdown(
    """
    <div style="padding:40px; text-align:center; background:#0A0A0A; border-radius:15px;">
        <h1 style="color:#E6E6E6; font-size:48px; font-weight:800;">
            🚦 Car Crash Analysis Dashboard
        </h1>
        <p style="color:#BBBBBB; font-size:20px; max-width:700px; margin:auto;">
            Explore accident trends, insurance premiums, and the relationship between alcohol & speeding.  
            Designed as an <b>interactive minor project</b> using Streamlit, Plotly, and Seaborn.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# --------------- KPI CARDS ----------------
st.subheader("📊 Quick Insights")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total States", len(df))
with col2:
    st.metric("Avg. Accidents", f"{df['total'].mean():.1f}")
with col3:
    st.metric("Max Accidents", df['total'].max())
with col4:
    st.metric("Avg. Premium", f"${df['ins_premium'].mean():.0f}")

st.markdown("---")

# --------------- NAVIGATION BUTTONS ----------------
st.subheader("📍 Explore the Dashboard")

col1, = st.columns(1)

with col1:
    if st.button("📊 Open Dashboard"):
        st.switch_page("pages/1_Dashboard.py")



st.markdown("---")

# --------------- EXPANDABLE SECTIONS ----------------
st.subheader("📌 Project Overview")

with st.expander("🔍 Key Features"):
    st.write(
        """
        - 📊 Interactive charts to explore accident statistics.
        - 🚘 Insights into alcohol & speeding-related accidents.
        - 💰 Comparison of insurance premiums by state.
        - 🌎 3D visualization of accident factors.
        """
    )

with st.expander("🛠️ Tech Stack"):
    st.write(
        """
        - **Python Libraries**: Streamlit, Plotly, Seaborn, Pandas  
        - **Visualization**: Interactive Bar, Pie, Scatter & 3D Plots  
        - **Design**: Custom HTML/CSS with animations  
        """
    )

with st.expander("🎯 Purpose of Project"):
    st.write(
        """
        This project demonstrates how data visualization uncovers insights into 
        real-world challenges, supporting data-driven decision-making in 
        **road safety** and **insurance policies**.
        """
    )

st.markdown("---")

# --------------- FOOTER ----------------
st.markdown(
    """
    <div style="text-align:center; color:#AAAAAA; padding:20px; animation: fadeIn 3s;">
        🚗 Built with <b>Streamlit</b> | Minor Project by <b>[Kushagra Singh]</b>
    </div>
    """,
    unsafe_allow_html=True
)
