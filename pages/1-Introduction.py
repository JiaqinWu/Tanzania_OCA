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

    title = 'Organizational Capacity Assessment Tool'
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
    ### New Partners Initiative Technical Assistance (NuPITA) Project

    The New Partners Initiative Technical Assistance (NuPITA) project is funded by the United States Agency for International Development (USAID) through Contract No: GHS-I-00-07-00002-00. The Technical Assistance Project to New Partners Initiative (TA-NPI) project is funded by the United States Department of Health and Human Services—Centers for Disease Control and Prevention through Contract No: 200-2004-05316/Task Order 002. Both projects are implemented by John Snow, Inc. in collaboration with Initiatives Inc.

    This document is made possible by the generous support of the American people through USAID and Department of Health and Human Services—Centers for Disease Control and Prevention (CDC). The contents are the responsibility of John Snow, Inc., and do not necessarily reflect the views of USAID, CDC, or the United States Government.

    """)

    st.markdown("""
    ### Organizational Capacity Assessment Tool

    #### Goal:
    The goal of this tool is to assist organizations in assessing the critical elements for effective organizational management, and identifying those areas that need strengthening or further development.
    
    #### Purpose:
    The OCA tool was designed to enable organizations to define a capacity-building improvement plan, based on self-assessed need. This Organizational Capacity Assessment (OCA) was initially designed to measure overall capacity of organizations funded by President’s Emergency Plan for AIDS Relief (PEPFAR) under the New Partners Initiative (NPI). This OCA tool provides organizations with a set of criteria to assess their current management capacity to implement quality health programs, to identify key areas that need strengthening. Although many capacity assessments exist, the structure and process of this tool distinguishes it from others. Multi-level and multi-department involvement fosters team building and organizational learning. Inclusion of management, compliance, and program components ensure a holistic understanding of the organization’s strengths and challenges and the guided self-assessment by skilled facilitators instills ownership on the part of the organization for its improvement plan.

    #### The OCA tool assesses technical capacity in seven domains, and each domain has a number of sub-areas.            

    #### OCA Domains
    1. Governance
    2. Administration
    3. Human Resources
    4. Financial Management
    5. Organizational Management
    6. Program Management
    7. Project Performance Management
                
    #### Using This Tool
    This Organizational Capacity Assessment tool is designed to enable organizational learning, foster team sharing, and encourage reflective self-assessment within organizations.

    Recognizing that organizational development is a process, the use of the OCA tool results in concrete action plans to provide organizations with a clear organizational development road map. The OCA can be repeated on an annual basis to monitor the effectiveness of previous actions, evaluate progress in capacity improvement, and identify new areas in need of strengthening.

    The OCA is an interactive self-assessment process that should bring together staff from all departments at implementing organizations, both at headquarters and in the field, for the two- to three-day assessment.

    Not intended to be a scientific method, the value of the OCA is in its collaborative, self-assessment process. The framework offers organizations a chance to reflect on their current status against recognized best practices. Lively discussions are also an opportunity for management, administration, and program staff to learn how each functions, strengthening the team and reinforcing the inter- relatedness of the seven OCA components.
 
    Each page of this tool examines one area. A range of examples of services available is provided along a continuum, from 1-4.

    The methodology is a guided self-assessment that encourages active participation. The facilitator and participants meet and discuss each area to determine where the organization sits along the continuum of implementation. Facilitators ask open-ended, probing questions to encourage group discussion, and take notes on participant responses. These notes are later used for the action planning.

    Sample questions which might help the facilitator to probe further into the content areas are presented on each page.

    The scores that are arrived at are designed to set priorities for the actions and are not used to judge performance. Facilitators use the information from the scoring and rationale sheets to define the issues and actions. The organization reviews or adjusts the problem statement and builds on the suggested actions to define action steps, responsibilities, timeframe, and possible technical assistance needs.

    The ability to identify areas to be addressed will strengthen the organization and in subsequent years, enable it to view improvement and note where progress is still needed.

    """)
                            
    st.markdown("""
    #### Using This Dashboard
    This dashboard is designed to allow audiences to explore and analyze scoring data across different dimensions. Here are the details of the four sub-tabs:

    1. **Tab 1: Guidance** - Comprehensive instructions on how to effectively navigate and utilize the dashboard.
    2. **Tab 2: Metric Check** - Check metrics for each subsection, including domain, domain objective, subsection objective, grading rubrics, and guiding questions.
    3. **Tab 2: Score Filtering** - Filter and explore subsections that meet specific score criteria.
    4. **Tab 3: Section Analysis** - Analyze and compare how a specific program performs across various subsections within a selected domain.
    5. **Tab 4: Institution Comparison** - Compare the performance of different programs on a specific subsection.
                
    Feel free to explore any tab to interact with the data!
    """)





if __name__ == "__main__":
    app()
