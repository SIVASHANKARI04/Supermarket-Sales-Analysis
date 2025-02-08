import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
@st.cache_data
def load_data():
    file_path = "E:\DSDemo\env\project\Demoprojects\supermarket_sales new.csv"
    return pd.read_csv(file_path)

data = load_data()

# Streamlit app title
st.title("Supermarket Sales Dashboard")

# Display Dataframe
st.sidebar.header("Data Overview")
if st.sidebar.checkbox("Show Raw Data"):
    st.subheader("Dataset Preview")
    st.write(data)

# Filter by city
st.sidebar.subheader("City Filter")
city_filter = st.sidebar.multiselect("Select City:", data["City"].unique(), default=data["City"].unique())
filtered_data = data[data["City"].isin(city_filter)]

# Customer Type Analysis
st.subheader("Product line Distribution")
fig2, ax2 = plt.subplots()
filtered_data["Product line"].value_counts().plot(kind="pie", autopct="%1.1f%%", colors=["lightcoral", "lightskyblue"], ax=ax2)
plt.title("product line Distribution")
plt.ylabel("")
st.pyplot(fig2)

# Sales Summary Statistics
st.subheader("Sales Summary Statistics")
st.write(filtered_data.describe())

# Invoice ID Search
st.subheader("Search Invoice Details")
invoice_id = st.text_input("Enter Invoice ID:")
if invoice_id:
    result = data[data["Invoice ID"] == invoice_id]
    if not result.empty:
        st.write(result)
    else:
        st.error("Invoice not found.")
