import streamlit as st

def style_background_home():
    st.markdown(
        """
        <style>
                .stApp {
                background-color: #5865F2 !important;
                    }
                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius:5rem !important;
                }
        </style>
        """,
        unsafe_allow_html=True
    )
def style_background_dashboard():
    st.markdown(
        """
        <style>
       
                .stApp {
                background-color: #E0E3FF !important;
                    }
        </style>
        """,
        unsafe_allow_html=True
    )
def style_base_layout():
    st.markdown(
        """
        <style>
         @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Open+Sans:ital,wght@0,300..800;1,300..800&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap');
         @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Open+Sans:ital,wght@0,300..800;1,300..800&family=Outfit:wght@100..900&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap');
                #MainMenu, footer,header {
                    visibility:hidden;
                }
                .block-container {
                    padding-top:1.5rem !important;
                    }
                h1 {
                font-family: 'Climate Crisis',sans-serif !important;
                font-size:3.5 rem !important;
                line-height:1.1 !impotant;
                margin-bottom:0rem !important;
                
                }
                
                h2 {
                font-family: 'Climate Crisis',sans-serif !important;
                font-size:3.5 rem !important;
                line-height:1.1 !impotant;
                margin-bottom:0rem !important;
                }
                
                h3,h4,p {
                font-family: 'Outfit',sans-serif
                }
                button[kind = "secondary"]{
                background: #EB459E !important;
                border-radius: 1.5rem !important;
                color: white !important;
                padding : 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }
                button[kind = "tertiary"]{
                background: black !important;
                border-radius: 1.5rem !important;
                color: white !important;
                padding : 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }
                button{
                background: #5865F2 !important;
                border-radius: 1.5rem !important;
                color: white !important;
                padding : 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }
                button:hover{
                transform: scale(1.05)}


            
        </style>
        """,
        unsafe_allow_html=True
    )