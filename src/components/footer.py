import streamlit as st

def footer_home():
    st.markdown(
        """
        <div style="display:flex; flex-direction:column; align-items:center;
                    justify-content:center; margin:30px 0;">
            <p style="font-weight:bold; color:white;">Created by Prapti Yadav</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
def footer_dashboard():
    st.markdown(
        """
        <div style="display:flex; flex-direction:column; align-items:center;
                    justify-content:center; margin:30px 0;">
            <p style="font-weight:bold; color:black;">Created by Prapti Yadav</p>
        </div>
        """,
        unsafe_allow_html=True,
    )