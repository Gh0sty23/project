#######################
# Import libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt
from wordcloud import WordCloud
from mpl_toolkits.mplot3d import Axes3D
import re
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler

#######################
# Page configuration
st.set_page_config(
    page_title="Dota 2 Pro Meta Team Maker and Win rate predictor", # Replace this with your Project's Title
    page_icon="assets/icon.png", # You may replace this with a custom icon or emoji related to your project
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

#######################

# Initialize page_selection in session state if not already set
if 'page_selection' not in st.session_state:
    st.session_state.page_selection = 'about'  # Default page

# Function to update page_selection
def set_page_selection(page):
    st.session_state.page_selection = page

# Sidebar
with st.sidebar:

    # Sidebar Title (Change this with your project's title)
    st.title('Dota 2 Pro Meta Team Maker and Win rate predictor')

    # Page Button Navigation
    st.subheader("Pages")

    if st.button("About", use_container_width=True, on_click=set_page_selection, args=('about',)):
        st.session_state.page_selection = 'about'
    
    if st.button("Dataset", use_container_width=True, on_click=set_page_selection, args=('dataset',)):
        st.session_state.page_selection = 'dataset'

    if st.button("EDA", use_container_width=True, on_click=set_page_selection, args=('eda',)):
        st.session_state.page_selection = "eda"

    if st.button("Data Cleaning / Pre-processing", use_container_width=True, on_click=set_page_selection, args=('data_cleaning',)):
        st.session_state.page_selection = "data_cleaning"

    if st.button("Machine Learning", use_container_width=True, on_click=set_page_selection, args=('machine_learning',)): 
        st.session_state.page_selection = "machine_learning"

    if st.button("Prediction", use_container_width=True, on_click=set_page_selection, args=('prediction',)): 
        st.session_state.page_selection = "prediction"

    if st.button("Conclusion", use_container_width=True, on_click=set_page_selection, args=('conclusion',)):
        st.session_state.page_selection = "conclusion"

    # Project Members
    st.subheader("Members")
    st.markdown("1. Elon Musk\n2. Jeff Bezos\n3. Sam Altman\n4. Mark Zuckerberg")

#######################
# Data

# Load data
dataset = pd.read_csv("Current_Pro_meta.csv")

# 1 SPLIT ROLES
dataset['Roles_List'] = dataset['Roles'].str.split(',')

# 2 PICK RATE
total_picks = dataset['Times Picked'].sum()
dataset['Pick Rate (%)'] = (dataset['Times Picked'] / total_picks) * 100

# 3 BAN RATE
total_bans= dataset['Times Banned'].sum()
dataset['Ban Rate (%)'] = (dataset['Times Banned'] / total_bans) * 100

# 4 CONTESTATION RATE
dataset['Contestation Rate (%)'] = dataset['Pick Rate (%)'] + dataset['Ban Rate (%)']

#######################

# Pages

# About Page
if st.session_state.page_selection == "about":
    st.header("ℹ️ About")

    st.markdown("""
        Just a streamtlit web app that shows some **Exploratory Data Analysis (EDA)**, **Data Pre-processing** and usage of **Clustering and Linear Regression** 
        to make a Dota 2 team compostion and predict a team's win rate based on the type of heroes in the team
    
    """)

# Dataset Page
elif st.session_state.page_selection == "dataset":
    st.header("📊 Dataset")

    st.write("IRIS Flower Dataset")
    st.write("")

    # Your content for your DATASET page goes here

# EDA Page
elif st.session_state.page_selection == "eda":
    st.header("📈 Exploratory Data Analysis (EDA)")


    col = st.columns((1.5, 4.5, 2), gap='medium')

    # Your content for the EDA page goes here

    with col[0]:
        st.markdown('#### Graphs Column 1')


    with col[1]:
        st.markdown('#### Graphs Column 2')
        
    with col[2]:
        st.markdown('#### Graphs Column 3')

# Data Cleaning Page
elif st.session_state.page_selection == "data_cleaning":
    st.header("🧼 Data Cleaning and Data Pre-processing")

    # Your content for the DATA CLEANING / PREPROCESSING page goes here
    st.dataframe(dataset.head())

    st.write("""
    Since we'll mostly ever be looking only at win rates, pick rates and ban rates, 
             we will be dropping most every other column except for those that we need.
    """)

    roles_split = dataset['Roles'].str.get_dummies(sep=', ')
    dataset = pd.concat([dataset.drop(columns=['Roles']), roles_split], axis=1)

    # Drop unnecessary columns
    columns_to_drop = ['Unnamed: 0', 'Primary Attribute', 'Attack Type', 
                       'Attack Range', 'Roles', 'Total Pro wins', 
                       'Times Picked', 'Times Banned', 'Roles_List',
                       'Niche Hero?'
                       ]
    dataset = dataset.drop(columns=[col for col in columns_to_drop if col in dataset.columns])
    st.dataframe(dataset.head())

    features = ['Contestation Rate (%)','Pick Rate (%)', 'Ban Rate (%)', 'Win Rate']

    new = dataset[features]
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(new)
    X_scaled_df = pd.DataFrame(X_scaled, columns=features)
    
    st.dataframe(X_scaled_df.head())

# Machine Learning Page
elif st.session_state.page_selection == "machine_learning":
    st.header("🤖 Machine Learning")

    # Your content for the MACHINE LEARNING page goes here

# Prediction Page
elif st.session_state.page_selection == "prediction":
    st.header("👀 Prediction")

    # Your content for the PREDICTION page goes here

# Conclusions Page
elif st.session_state.page_selection == "conclusion":
    st.header("📝 Conclusion")

    # Your content for the CONCLUSION page goes here
