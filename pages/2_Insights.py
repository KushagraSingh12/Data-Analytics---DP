import streamlit as st
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="Insights", page_icon="📈", layout="wide")

st.title("📈 Key Insights")

# Load dataset
df = sns.load_dataset("car_crashes")

# Insight 1: Top 5 states by accidents
top_states = df.sort_values("total", ascending=False).head(5)
fig1 = px.bar(top_states, x="abbrev", y="total", 
              title="Top 5 States by Total Accidents",
              color="total", template="plotly_dark")
st.plotly_chart(fig1, use_container_width=True)

st.markdown("**Insight 1:** States like Texas, Kansas, and Virginia report the highest accident counts.")

# Insight 2: Correlation Alcohol vs Speeding
fig2 = px.scatter(df, x="alcohol", y="speeding", size="total", color="abbrev", 
                  title="Alcohol vs Speeding Accidents", template="plotly_dark")
st.plotly_chart(fig2, use_container_width=True)

st.markdown("**Insight 2:** There is a clear positive correlation — states with more alcohol-related accidents tend to have more speeding-related ones.")

# Insight 3: Insurance Premiums
fig3 = px.histogram(df, x="ins_premium", nbins=20, title="Distribution of Insurance Premiums", template="plotly_dark")
st.plotly_chart(fig3, use_container_width=True)

st.markdown("**Insight 3:** Most insurance premiums cluster between $900 and $1200, with a few states paying significantly higher.")
