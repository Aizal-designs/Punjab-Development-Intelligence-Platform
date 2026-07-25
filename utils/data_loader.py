from pathlib import Path
import pandas as pd
import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
DATA_FILE = DATA_DIR / "district_master.csv"


@st.cache_data
def load_data():
    """Load master dataset."""
    return pd.read_csv(DATA_FILE)


@st.cache_data
def get_districts():
    """Return all district names."""
    df = load_data()
    return sorted(df["District"].tolist())


@st.cache_data
def get_district(district):
    """Return selected district."""
    df = load_data()
    return df[df["District"] == district]


@st.cache_data
def get_total_districts():
    return len(load_data())


@st.cache_data
def get_dataset():
    return load_data()