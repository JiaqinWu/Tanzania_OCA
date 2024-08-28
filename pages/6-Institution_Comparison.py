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
df = pd.read_csv('Final_dataset1.csv',encoding='utf-8')
df['Statement'] = df['Statement'].str.replace('_\t', '•')


# Streamlit application
def app():
    # Main page content
    #st.set_page_config(page_title = 'Dashboard -- Uganda SCORE Survey', page_icon='🇺🇬',layout='wide')

    title = 'Comparison of Scores by Program Within the Selected Subsection'
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
    module_selected = st.sidebar.selectbox('Select Domain', df['Domain'].unique())
    part_selected = st.sidebar.selectbox('Select Sub Section', df[df['Domain'] == module_selected]['Sub Section'].unique())
    st.sidebar.markdown(f"#### You selected: {part_selected}")
    plot_selected = st.sidebar.selectbox('Select Visualization Type',['Bar Plot','Pie Plot','Radar Plot', 'Table'],index=0)

    
    # Filter data based on selections
    filtered_data = df[(df['Domain'] == module_selected) & 
                        (df['Sub Section'] == part_selected)].reset_index()
    
    color_scale = alt.Scale(
        domain=[1, 2, 3, 4],
        range=['#d73027', '#fc8d59', '#fee08b', '#1a9850']  # Custom colors for each score
    )
    if not filtered_data.empty:
        # Create and display the selected plot type
        if plot_selected == 'Bar Plot':
            st.write("")
            chart = alt.Chart(filtered_data).mark_bar().encode(
                y=alt.Y('Program:N', sort=filtered_data['Program'].unique()),  # Using :N to denote a nominal categorical field
                x=alt.X('Score:Q', scale=alt.Scale(domain=[0, 4]),  # Using Score on the x-axis with a defined domain
                axis=alt.Axis(values=[0, 1, 2, 3, 4])), 
                color=alt.Color('Score:N',scale=color_scale),  # Optional: coloring bars by Institution
                tooltip=['Program', 'Score', 'Statement']  # Optional: tooltips on hover
            ).properties(
                width=600,
                height=600,
                title=alt.TitleParams(
                    text=[
                        f"Bar Plot of Scores by Program within {module_selected}: {part_selected}"
                    ]
                ))

            # Combine the chart and the text
            final_chart = alt.layer(chart).configure_axis(
                labelFontSize=12,
                titleFontSize=14
            )

            # Display the chart in a Streamlit container
            st.altair_chart(final_chart, use_container_width=True)

        elif plot_selected == 'Pie Plot':
            st.write("")
            base = alt.Chart(filtered_data).mark_arc().encode(
                theta=alt.Theta('Score:Q').stack(True),  
                color=alt.Color('Program:N'),
                tooltip=['Program', 'Score', 'Statement'] 
            )

            pie = base.mark_arc(outerRadius = 120)
            text1 = base.mark_text(radius=150, size=12).encode(text="Score:N")

            # Combine the chart and the text
            final_chart1 = alt.layer(pie, text1).properties(
                width=600,
                height=400,
                title=alt.TitleParams(
                    text=[
                        f"Pie Plot of Scores by Program within {module_selected}: {part_selected}"
                    ]
                )).configure_axis(
                labelFontSize=12,
                titleFontSize=14
            ).interactive()

            # Display the chart in a Streamlit container
            st.altair_chart(final_chart1, use_container_width=True)


        elif plot_selected == 'Radar Plot':
            # Creating a radar chart
            fig = px.line_polar(filtered_data, r='Score', theta='Program', line_close=True,
                                text='Score',
                                template="plotly_dark",
                                title=f"<br>Radar Plot of Scores by Program within {module_selected}: {part_selected}",
                                hover_data={
                                    'Program': True,
                                    'Score': True
                                })
            
            # Adjustments to improve layout
            fig.update_traces(textposition='bottom center')  # Adjust text positions to reduce overlap
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(showticklabels=True, tickangle=0),  # Adjust radial axis properties
                    angularaxis=dict(rotation=90, direction='clockwise', tickfont_size=15)  # Rotate angular axis for better label positioning
                ),
                font=dict(size=8)
            )

            # Displaying the chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)
        
        else:
            records = filtered_data[['Program', 'Domain','Sub Section','Score','Statement']].reset_index().drop(columns='index')
            st.markdown(f"#### Comparison of Scores by Program within {module_selected}: {part_selected} are shown below:")
            st.dataframe(records)

    else:
        st.write("No quantitative data available for the selected question.")

if __name__ == "__main__":
    app()