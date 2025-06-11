import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gspec - Electrical Design Tool", layout="wide")

# Title and Branding
st.markdown("<h1 style='color:#212121;'>gspec</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:#666;'>ELECTRICAL DESIGN</h3>", unsafe_allow_html=True)
st.divider()

# Inputs
region = st.selectbox("Select Region", ["City of Cape Town", "Overstrand", "Swartland"])
voltage = st.selectbox("Voltage", ["230V", "400V"])
amperage = st.selectbox("Main Breaker Amperage", ["60A", "80A", "100A", "125A", "160A"])
enclosure = st.selectbox("Enclosure Type", ["12-way Stainless Steel Kiosk", "Wall Mount", "Pole Mount"])

# Simulated costing
base_price = 12000
if region == "Overstrand":
    base_price += 1000
elif region == "Swartland":
    base_price += 2000

if amperage in ["125A", "160A"]:
    base_price += 2500

cost = base_price * 2
st.success(f"💰 Estimated Cost: R {cost:,.2f}")

# Simulated BOM
st.subheader("Bill of Materials (BOM)")
bom_data = {
    "Item Code": ["CU256", "DIM30SP", "L26", "SETM8X40A2"],
    "Description": ["Copper Flat Bar 25x6", "Hinge Concealed S/S", "Label - Rating Plate", "Screw M8 x 40 A2"],
    "Quantity": [0.42, 4, 1, 4]
}
df = pd.DataFrame(bom_data)
st.dataframe(df, use_container_width=True)

# 3D Viewer
st.subheader("Kiosk 3D Model Preview")
with open("gspec_kiosk_webviewer.html", "r") as f:
    html_content = f.read()
st.components.v1.html(html_content, height=500, scrolling=False)

# Download
st.download_button("📥 Download Spec Sheet", data=df.to_csv(index=False), file_name="gspec_spec_sheet.csv", mime="text/csv")
