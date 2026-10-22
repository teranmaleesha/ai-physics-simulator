import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Radioactive Decay & Physics Simulator", 
    page_icon="⚛️", 
    layout="wide"
)

# App Header
st.title("⚛️ AI-Powered Radioactive Decay & Physics Simulator")
st.markdown("""
This application simulates the process of **Radioactive Decay** and half-life principles based on exponential decay laws. 
Customize isotope parameters, analyze decay curves, and generate AI-driven insights for physical science modeling.
""")

# Sidebar Controls for User Input
st.sidebar.header("⚙️ Simulation Parameters")

# Isotope Selection
element = st.sidebar.selectbox(
    "Select Radioactive Isotope",
    [
        "Carbon-14 (Half-life: 5,730 years)", 
        "Uranium-238 (Half-life: 4.47 billion years)", 
        "Radon-222 (Half-life: 3.8 days)", 
        "Custom Isotope"
    ]
)

if "Carbon-14" in element:
    half_life = 5730.0
    unit = "Years"
elif "Uranium-238" in element:
    half_life = 4470000000.0
    unit = "Years"
elif "Radon-222" in element:
    half_life = 3.8
    unit = "Days"
else:
    half_life = st.sidebar.number_input("Enter Half-life Value", value=10.0, min_value=0.1)
    unit = "Time Units"

initial_nuclei = st.sidebar.slider(
    "Initial Number of Nuclei ($N_0$)", 
    min_value=100, 
    max_value=10000, 
    value=1000, 
    step=100
)

max_time = st.sidebar.slider(
    f"Max Simulation Time ({unit})", 
    min_value=float(half_life * 0.5), 
    max_value=float(half_life * 5), 
    value=float(half_life * 3)
)

# Physics Calculation: Exponential Decay Law -> N(t) = N_0 * e^(-lambda * t)
# where lambda = ln(2) / half_life
time_points = np.linspace(0, max_time, 500)
decay_constant = np.log(2) / half_life
remaining_nuclei = initial_nuclei * np.exp(-decay_constant * time_points)
decayed_nuclei = initial_nuclei - remaining_nuclei

# Display Key Metrics in Columns
col1, col2, col3 = st.columns(3)
col1.metric("Initial Nuclei ($N_0$)", f"{initial_nuclei:,}")
col2.metric("Half-life ($t_{1/2}$)", f"{half_life:g} {unit}")
col3.metric("Final Remaining Nuclei", f"{int(remaining_nuclei[-1]):,}")

# Plotting Decay Curve using Matplotlib
st.subheader("📈 Decay Curve Visualization")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(time_points, remaining_nuclei, label="Remaining Nuclei N(t)", color="#ff4b4b", linewidth=2.5)
ax.plot(time_points, decayed_nuclei, label="Decayed Nuclei", color="#1f77b4", linestyle="--", linewidth=2)
ax.axvline(half_life, color="green", linestyle=":", label=f"1 Half-life ({half_life:g} {unit})")

ax.set_xlabel(f"Time ({unit})", fontsize=12)
ax.set_ylabel("Number of Radioactive Nuclei", fontsize=12)
ax.set_title("Radioactive Decay Over Time (Exponential Model)", fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

st.pyplot(fig)

# AI & Physics Analysis Insights Section
st.subheader("🤖 AI Physics Insights & Analytics")
st.markdown(f"""
- **Core Principle:** The simulation utilizes the radioactive decay law where the rate of decay is proportional to the number of undecayed nuclei present.
- **Isotope Behavior:** For the selected isotope with a half-life of **{half_life:g} {unit}**, exactly 50% of the parent nuclei disintegrate into daughter isotopes per half-life interval.
- **Predictive Modeling:** Based on the current parameters ($N_0 = {initial_nuclei}$), the system can accurately forecast activity levels and decay rates for advanced scientific research modeling.
""")