import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello World!")

# Print versions
st.write(f"Streamlit version: {st.__version__}")
st.write(f"Pandas version: {pd.__version__}")
st.write(f"NumPy version: {np.__version__}")