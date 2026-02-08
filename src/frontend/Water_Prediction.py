import streamlit as st
import requests
import os
import pandas as pd
from dotenv import load_dotenv
from typing import Dict, Any

# Load environment variables
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="AquaSafe | Water Potability AI",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Base API URL
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    .stSuccess {
        background-color: #d4edda;
        color: #155724;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #c3e6cb;
    }
    .stError {
        background-color: #f8d7da;
        color: #721c24;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #f5c6cb;
    }
    h1 {
        color: #2c3e50;
    }
    h2, h3 {
        color: #34495e;
    }
    </style>
    """, unsafe_allow_html=True)


# ----------------- Utility Functions -----------------
def check_api_health() -> bool:
    """Check if the FastAPI backend is healthy."""
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=2)
        return response.status_code == 200
    except:
        return False


def predict_potability(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Send input data to the API for prediction."""
    try:
        response = requests.post(f"{API_BASE_URL}/predict", json=payload, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ API request failed: {e}")
        return None


# ----------------- UI Layout -----------------
def main():
    # Sidebar
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/3105/3105807.png", width=100)
        st.title("AquaSafe AI")
        st.markdown("### 🔍 Model Status")
        
        if check_api_health():
            st.success("🟢 System Online")
        else:
            st.error("🔴 Offline")
            st.warning("Ensure backend is running on port 8000")

        st.markdown("---")
        st.write("### 📊 Dataset Info")
        st.info(
            "This model is trained on water quality metrics including pH, Hardness, Solids, "
            "Chloramines, Sulfate, Conductivity, Organic Carbon, Trihalomethanes, and Turbidity."
        )
        st.markdown("[View Source Code](https://github.com/TahaZaman6547/Water_Potability_Prediction))")

    # Main Content
    st.title("💧 Water Potability Predictor")
    st.markdown("#### Instant AI-Analysis for Water Quality Safety")
    st.write("Enter the chemical properties of the water sample below to generate a safety report.")
    
    st.markdown("---")

    # Input Form
    with st.form("water_form"):
        st.subheader("🧪 Chemical Parameters")
        
        c1, c2, c3 = st.columns(3)
        
        with c1:
            ph = st.number_input("pH Level", 0.0, 14.0, 7.0, help="Acid-base balance (0-14)")
            Hardness = st.number_input("Hardness (mg/L)", 0.0, 400.0, 200.0)
            Solids = st.number_input("Total Dissolved Solids (ppm)", 0.0, 60000.0, 20000.0)
        
        with c2:
            Chloramines = st.number_input("Chloramines (ppm)", 0.0, 15.0, 7.0)
            Sulfate = st.number_input("Sulfate (mg/L)", 0.0, 500.0, 300.0)
            Conductivity = st.number_input("Conductivity (μS/cm)", 0.0, 800.0, 400.0)
            
        with c3:
            Organic_carbon = st.number_input("Organic Carbon (ppm)", 0.0, 30.0, 15.0)
            Trihalomethanes = st.number_input("Trihalomethanes (μg/L)", 0.0, 150.0, 60.0)
            Turbidity = st.number_input("Turbidity (NTU)", 0.0, 7.0, 4.0)

        st.markdown("---")
        submitted = st.form_submit_button("🚀 Analyze Sample")

    # Results Section
    if submitted:
        payload = {
            "ph": ph, "Hardness": Hardness, "Solids": Solids,
            "Chloramines": Chloramines, "Sulfate": Sulfate, "Conductivity": Conductivity,
            "Organic_carbon": Organic_carbon, "Trihalomethanes": Trihalomethanes, "Turbidity": Turbidity
        }

        with st.spinner("🔬 Analyzing sample composition..."):
            result = predict_potability(payload)

        if result:
            st.markdown("## 📋 Analysis Report")
            
            prediction = result.get("prediction")
            status = result.get("result")
            
            col_res1, col_res2 = st.columns([1, 2])
            
            with col_res1:
                if prediction == 1:
                    st.image("https://cdn-icons-png.flaticon.com/512/190/190411.png", width=150)
                else:
                    st.image("https://cdn-icons-png.flaticon.com/512/564/564619.png", width=150)

            with col_res2:
                if prediction == 1:
                    st.success(f"### Result: {status}")
                    st.markdown("✅ **Safety Status:** Safe for human consumption.")
                    st.markdown("This sample meets the required safety standards based on the provided metrics.")
                else:
                    st.error(f"### Result: {status}")
                    st.markdown("⚠️ **Safety Status:** Unsafe / Contaminated.")
                    st.markdown("This sample contains levels of contaminants that may be harmful.")

            with st.expander("Show Raw API Response"):
                st.json(result)


if __name__ == "__main__":
    main()

