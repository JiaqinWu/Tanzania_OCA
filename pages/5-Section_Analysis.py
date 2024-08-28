import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import altair as alt 
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

    title = 'Comparison of Scores of Subsections'
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
    
    st.sidebar.title('Enter your selections here!')

    # Ensure the Score column is sorted
    program_selected = st.sidebar.selectbox('Select Program', df['Program'].unique())
    module_selected = st.sidebar.selectbox('Select Domain', df['Domain'].unique())    
    plot_selected = st.sidebar.selectbox('Select Visualization Type',['Bar Plot','Pie Plot','Radar Plot','Table'],index=0)


        
    # Filter data based on selections
    filtered_data = df[(df['Domain'] == module_selected) & 
                        (df['Program'] == program_selected)]
    
    color_scale = alt.Scale(
        domain=[1, 2, 3, 4],
        range=['#d73027', '#fc8d59', '#fee08b', '#1a9850']  # Custom colors for each score
    )
    if not filtered_data.empty:
        #module_selected1 = module_selected.split(':')[1]
        if plot_selected == 'Bar Plot':
            st.write("")
            chart = alt.Chart(filtered_data).mark_bar().encode(
                y=alt.Y('Sub Section:N'),
                x=alt.X('Score:Q', scale=alt.Scale(domain=[0, 4]),
                        axis=alt.Axis(values=[0, 1, 2, 3, 4])),
                color=alt.Color('Score:N',scale=color_scale),
                tooltip=['Sub Section', 'Score', 'Statement']
            ).properties(
                width=600,
                height=600,
                title=f'{program_selected} -- Bar Plot of Scores by Subsection within {module_selected}'
            )

            final_chart = alt.layer(chart).configure_axis(
                labelFontSize=12,
                titleFontSize=14
            )

            st.altair_chart(final_chart, use_container_width=True)

        elif plot_selected == 'Pie Plot':
            st.write("")
            base = alt.Chart(filtered_data).mark_arc().encode(
                theta=alt.Theta('Score:Q').stack(True),  
                color=alt.Color('Sub Section:N'),
                tooltip=['Sub Section', 'Score', 'Statement']
            )

            pie = base.mark_arc(outerRadius = 120)
            text1 = base.mark_text(radius=150, size=12).encode(text="Score:N")

            final_chart1 = alt.layer(pie, text1).properties(
                width=600,
                height=400,
                title=f'{program_selected} -- Pie Plot of Scores by Subsection within {module_selected}'
            ).configure_axis(
                labelFontSize=12,
                titleFontSize=14
            ).interactive()

            st.altair_chart(final_chart1, use_container_width=True)

        elif plot_selected == 'Radar Plot':
            #filtered_data['Question1'] = 'Q' + filtered_data['Qn'].astype(str)
            # Define a custom hover template
            fig = px.line_polar(filtered_data, r='Score', theta='Sub Section', line_close=True,
                                text='Score',
                                template="plotly_dark",
                                title=f'{program_selected} -- Radar Plot of Scores by Subsection within {module_selected}',
                                hover_data={
                                    'Sub Section': True,
                                    'Score': True
                                })
            
            fig.update_traces(textposition='bottom center')
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(showticklabels=True, tickangle=0),
                    angularaxis=dict(rotation=90, direction='clockwise', tickfont_size=15)
                ),
                font=dict(size=8)
            )


            st.plotly_chart(fig, use_container_width=True)
        
        else:
            records = filtered_data[['Program', 'Domain','Sub Section','Score','Statement']].reset_index().drop(columns='index')
            st.markdown(f"#### Comparison of Scores by Subsection within {module_selected} in Program {program_selected} are shown below:")
            st.dataframe(records)

    else:
        st.markdown("### No data available for the selected criteria.")

if __name__ == "__main__":
    app()