import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import altair as alt 
import numpy as np
import re
import plotly.express as px
from navigation import make_sidebar

make_sidebar()

# Import the dataset
image = "CGHPI.png"
df = pd.read_csv('Metrics1.csv',encoding='utf-8')
df1 = pd.read_csv('Grading_Q1.csv',encoding='utf-8')
# Replace '¥' with bullet points
df.replace('¥', '•', regex=True, inplace=True)

# Clean up the text by replacing \n and \t with spaces
df.replace({'\n': ' ', '\t': ' '}, regex=True, inplace=True)
#df.replace("organization_","organization_'s")
df1 = df1.replace(np.nan, '', regex=True)

# Create an HTML table with custom CSS for text size and bullet point handling
def render_html_table(df):
    # Define custom CSS for smaller text and bullet points
    style = """
    <style>
    table {
        font-size: 6px !important; /* Force smaller text size */
        width: 100%;
    }
    td {
        word-wrap: break-word;
        white-space: pre-wrap;
        vertical-align: top;
        font-size: 6px !important; /* Ensure that the text size is applied to table cells */
    }
    li {
        margin-left: 10px;
        list-style-type: disc;
        font-size: 6px !important; /* Force smaller text size in bullet points */
    }
    p {
        margin: 0; /* Remove default paragraph margins */
        font-size: 6px !important; /* Ensure paragraph text is small */
    }
    </style>
    """


    # Convert DataFrame to HTML, ensuring each bullet point starts on a new line
    html = df.to_html(index=False, escape=False)

    # Replace bullet points to ensure proper line breaks
    html = html.replace('•', '<br>&bull;')  # Replace with HTML bullet points

    # Wrap the table in the custom style
    return  html

# Streamlit application
def app():
    # Main page content
    #st.set_page_config(page_title = 'Dashboard -- Uganda SCORE Survey', page_icon='🇺🇬',layout='wide')

    title = 'Check metrics for each subsection'
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
            <h2 style='text-align: center'>{title}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


        

    # Sidebar for selection
    st.sidebar.title('Enter your selections here!')
    module_selected1 = st.sidebar.selectbox('Select Domain', df['Domain'].unique())
    part_selected1 = st.sidebar.selectbox('Select Subection', df[df['Domain'] == module_selected1]['Subsection'].unique())
    st.sidebar.markdown(f"#### You selected: {module_selected1}: {part_selected1}")




    # Show data based on selections
    # Filter data based on selections
    filtered_data = df[(df['Domain'] == module_selected1) & 
                    (df['Subsection'] == part_selected1)].reset_index()
    st.markdown(f'### {module_selected1}')
    st.markdown(f'<strong>Objective:</strong> <span style="font-weight: normal;">{filtered_data.Objective[0]}</span>', unsafe_allow_html=True)
    st.markdown(f'#### {part_selected1}')
    st.markdown(f'<strong>Subsection Objective:</strong> <span style="font-weight: normal;">{filtered_data["Subsection Objective"][0]}</span>', unsafe_allow_html=True)
    st.markdown(f'<strong>Resources:</strong> <span style="font-weight: normal;">{filtered_data["Resources"][0]}</span>', unsafe_allow_html=True)
    st.markdown(f"##### Metrics:")
    records = filtered_data[['1', '2','3','4']].reset_index().drop(columns='index')
    st.markdown(render_html_table(records), unsafe_allow_html=True)
    st.markdown(f"##### Guiding Questions:")
    fil_df = df1[df1['Sub Section'] == part_selected1][['Subsection Checklist', 'Yes','No','N/A','Comments/Quality Notes']].reset_index().drop(columns='index')
    st.markdown(render_html_table(fil_df), unsafe_allow_html=True)

if __name__ == "__main__":
    app()