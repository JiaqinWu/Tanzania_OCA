import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import altair as alt 
import numpy as np
from navigation import make_sidebar 

make_sidebar()

# Import the dataset
image = "CGHPI.png"


# Streamlit application
def app():
    # Main page content
    #st.set_page_config(page_title = 'Dashboard -- Uganda SCORE Survey', page_icon='🇺🇬',layout='wide')

    #st.image(image, width=200, use_column_width=False)
    #st.title('Sustainable Capacity of Local Organizations to Reach and End the HIV/AIDS Pandemic (SCORE)')

    title = 'Guidance for this dashboard'
    col1, col2, col3 = st.columns([3, 1, 5])

    with col1:
        st.write("")

    with col2:
        st.image(image, width=250)

    with col3:
        st.write("")

    # Center the image and title using HTML and CSS in Markdown
    st.markdown(
        f"""
        <style>
        .centered {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 30vh;
            text-align: center;
        }}
        </style>
        <div class="centered">
            <h1 style='text-align: center'>{title}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
        Welcome to the dashboard! Below are the instructions on how to effectively navigate and utilize each tab:

        1. **Tab 1: Metric Check**
            - In this tab, you can check detailed metrics for each subsection.
            - Metrics include domain, domain objective, subsection objective, grading rubrics, and guiding questions.
            - Use this tab to get a comprehensive understanding of how each subsection is evaluated.

        2. **Tab 2: Score Filtering**
            - This tab allows you to filter and explore subsections that meet specific score criteria.
            - You can select the score range you are interested in and view only the subsections that fall within that range.
            - It's a great tool for quickly identifying areas of strength or concern.

        3. **Tab 3: Section Analysis**
            - Analyze and compare the performance of a specific program across various subsections within a selected domain.
            - This tab helps you understand how a program performs in different areas, allowing for targeted improvements and insights.

        4. **Tab 4: Institution Comparison**
            - Use this tab to compare the performance of different programs on a specific subsection.
            - This is particularly useful for benchmarking and understanding how one program stacks up against others in key areas.
            - Ideal for institutions looking to evaluate and improve their standing.

        We hope this dashboard provides valuable insights and helps you in making informed decisions.
        """)

    
if __name__ == "__main__":
    app()