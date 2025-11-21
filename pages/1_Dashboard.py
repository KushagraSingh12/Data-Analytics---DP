import streamlit as st

import seaborn as sns
import plotly.express as px
import streamlit as st


st.title("Welcome to the Data Analytics Dashboard")
st.write("Use the sidebar to navigate between pages.")


st.title("Explore the Dashboard")
st.subheader("DATA")
df = sns.load_dataset("car_crashes")
st.dataframe(df)

fig = px.bar( df, x='abbrev', y='total',
           title='Total Car Accidents by State',
          labels={'abbrev': 'State', 'total': 'Total Accidents'},
          color = 'total',
          color_continuous_scale=px.colors.sequential.Agsunset,
         template='plotly_dark'
)

st.plotly_chart(fig)
st.subheader("📈 Summary: Alcohol vs. Speeding Accidents")
st.subheader("Graph Summary: Total Car Accidents by State")
st.markdown("This Bar Chart shows the total Car accidents accross several US states")
st.markdown(" - HIGHEST ACCIDENTS - Texas ,Kansas and Virginia have the most accidents counts approaching 20.")
st.markdown(" - LOWEST ACCIDENTS - Washington D.C. stands out with the fewest accidents, while maryland and Michigan also have low totals")
st.markdown("KEY INSIGHT - The Charts colour gradient(blue to orange) effectively highlights which states have more or fewer accidents, making the data easy to interpret at glance")

top10 = df.sort_values('ins_premium', ascending=False).head(10)

fig = px.bar(
    top10, 
    x='abbrev', 
    y='ins_premium',
    title='Top 10 States by Insurance Premium',
    labels={'abbrev': 'State', 'ins_premium': 'Insurance Premium'},
    color='ins_premium',
    color_continuous_scale=px.colors.sequential.Agsunset,
    template='plotly_dark'
)
st.plotly_chart(fig)
st.subheader("📈 Summary: Alcohol vs. Speeding Accidents")
st.subheader("Summary: Top 10 States by Insurance premium")
st.markdown("The Bar Chart Visualizes the top 10 states based on insurance premium costs.")
st.markdown(" - HIGHEST PREMIUMS : New jersey(NJ)m,Louisiana(LA), and Washington D.C.(DC) have the highest insurance premiums, with cost over $1,200")
st.markdown(" - LOWEST PREMIUMNS(in this top 10): Connecticut (CT), and Alaska (AK) have the lowest premiums, at around $1,100")
st.markdown("COLOUR AS GUIDE: The colour gradient reinforces the data, with darker orange indicating higher premium and a transition to purple for the lower premiums. ")

fig = px.scatter(
    df, x='alcohol', y='speeding',
    title='Alcohol vs Speeding Accidents',
    labels={'alcohol':'Alcohol Related Accidents', 'speeding':'Speeding Related Accidents'},
    color='abbrev',
    color_discrete_sequence=px.colors.sequential.Agsunset,
    template='plotly_dark',
    size='total'
)

fig.update_layout(title={'x': 0.5})
st.plotly_chart(fig)

st.subheader("📈 Summary: Alcohol vs. Speeding Accidents")
st.markdown("This scatter plot shows the relationship between alcohol-related and speeding-related accidents across different states.")
st.markdown(" - POSTIVE CORRELATION: The graph shows a clear positive correlation between the two variables. As the number of alcohol-related accidents increases, so does the number of speeding-related accidents.")
st.markdown(" - KEY OUTLIERS: Some states have very high numbers for both types of accidents (top right of the graph), while others have very low numbers (bottom left). This suggests that states with more one type of accident tend to have more of the other.")
st.markdown(" - DATA DENSITY: The data points are clustered in the bottom left-hand corner, indicating that most states have relatively low numbers of both alcohol- and speeding-related accidents.")

fig = px.pie(
    df, 
    values='speeding', 
    names='abbrev',
    title='Percentage of Speeding Accidents by State',
    color_discrete_sequence=px.colors.sequential.Agsunset,
    template='plotly_dark'
)

fig.update_traces(textposition='inside')
st.plotly_chart(fig)

st.subheader("📈 Percentage of speeding Accidents by state")
st.markdown("The pie chart Titled above shows how the total number aboveof speedingaccidents distributed across various U.S. States")
st.markdown(" - THE LARGEST SLICES: Represents the Highest percentage of accidents, belong to PA and HI.Conversely,States like OK and AZ have some of smalllest Slices")
st.markdown("CONCLUSION- The chart highlights which states Contribute the most of the total number of speeding accidents.")

fig = px.scatter_3d(
    df, x='alcohol', y='speeding', z='total',
    title='3D Scatter Plot of Alcohol, Speeding and Total Accidents',
    labels={'alcohol':'Alcohol Related Accidents', 'speeding':'Speeding Related Accidents', 'total':'total Accidents'},
    color='abbrev',
    color_discrete_sequence=px.colors.sequential.Agsunset,
    template='plotly_dark',
    size='total'
)
st.plotly_chart(fig)

st.subheader("Purpose of the Plot")
st.markdown("The 3D Scatter Plot visualizes the relationship bw alcohol-related accidents, speeding accidents, and total accidents for various U.S. states")
st.markdown("Each point represents a single state,postioned according to its data for all three Variables")
st.markdown("ANALYSIS OF THE DATA: The plot shows a Clear postive Correlation among the three variables")
st.markdown(" - States with higher number of alcohol- related accidents tends to also have a high number of speeding accidents and higher total no of accidents ")
st.markdown(" - The data points are not randomly Scattered; They form a diagonal Trend , indicating that states with lower values for one metric generally have lower values for others, and vice versa")
st.markdown(" - This suggests that these factors are interconnected and the stares with ahigh incidence of one type of accidents often face challenges with the others as well.")
