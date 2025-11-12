"""Composant sidebar réutilisable"""

import streamlit as st
from src.ui.styles.common import get_sidebar_style


def setup_sidebar():
    """Configure la sidebar complète avec logo, navigation et style"""
    st.markdown(get_sidebar_style(), unsafe_allow_html=True)

    st.sidebar.image("assets/images/42.png", use_container_width=True)

    st.sidebar.markdown(
        '<p style="margin-bottom: -40px; margin-top: 75px; padding: 0;"><b>Navigation</b></p>',
        unsafe_allow_html=True,
    )
    st.sidebar.write("---")

    # Menu de navigation
    st.sidebar.page_link(
        "pages/1_🤖_chatbot.py", label="Chatbot", use_container_width=True
    )
    st.sidebar.page_link(
        "pages/2_🎯_pratique.py", label="Pratique", use_container_width=True
    )

    st.sidebar.write("---")

    st.sidebar.markdown(
        """
    <div style="position: fixed; bottom: 20px; left: 20px; text-align: left; font-size: 14px; font-weight: bold;">
    \tCité des Métiers 2025
    </div>
    """,
        unsafe_allow_html=True,
    )
