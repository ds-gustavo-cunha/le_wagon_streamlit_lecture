import streamlit as st

cred_01 = st.secrets['credential_01']
cred_02 = st.secrets.credential_section.credential_02


st.write(f"Cred 01: {cred_01}")
st.write(f"Cred 02: {cred_02}")