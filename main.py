import streamlit as st
import pandas as pd

# Define the vendor IDs and their corresponding names
vendor_names = {
    1: "Momos",
    2: "PAPPA'S TIFFINS",
    3: "BIG BUNS",
    4: "BLUE BELLS RESTAURANT",
    5: "TIBBS FRANKIE",
    6: "THE THICK SHAKE FACTORY",
    7: "ROCKET KITCHEN",
    8: "TEA TIME",
    9: "JUICE BAR",
    10: "BLUE BELLS",
    11: "Tea Point",
    12: "GITAM STORE",
    13: "The Juice Box",
    14: "Test Restaurant",
    15: "SAI VENNELA TIFFINS",
    16: "CHAT BOX",
    17: "GITAM TALENT CAFE",
    18: "GITAM ESSENTIALS",
    19: "SK Canteen",
    20: "SK TIFFINS",
    21: "Meal Box",
    22: "Coffee Day",
    23: "Aura 2023",
    24: "OM SAI RAM CANTEEN",
    25: "GRILL & GOSSIP BREAKFAST",
    26: "Crimsons",
    27: "HERITAGE",
    28: "CRAVINGS & CRIMSON'S",
    29: "FRIES AND CO (old)",
    30: "CRIMSONS BREWERY",
    31: "Maggie",
    32: "G&G",
    33: "Oasis Kitchen",
    34: "MERLOT PATISSERIE",
    35: "PAPPAS TIFFINS",
    36: "GRILL & GOSSIP BREAKFAST",
    37: "BIRYANI STREET",
    38: "WRAPIT",
    39: "fries and co",
}

# Streamlit application
st.title("Vendor Earnings Analyzer")

# Upload the Excel file
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Read the Excel file into a Pandas DataFrame
    df = pd.read_excel(uploaded_file)

    # Button to trigger analysis
    if st.button("Analyze"):
        # Group by vendor_id and sum the restaurant_amount for each vendor
        restaurant_earnings_per_vendor = df.groupby('vendor_id')['restaurant_amount'].sum()
        total_earnings_pervendor = df.groupby('vendor_id')['order_amount'].sum()
        admin_earnings_pervendor = df.groupby('vendor_id')['admin_commission'].sum()

        st.write("___")
        st.write("RESTAURANT PAYOUTS")
        st.write("___")
        # Display the results
        for vendor_id, earnings in restaurant_earnings_per_vendor.items():
            if vendor_id in vendor_names:
                vendor_name = vendor_names[vendor_id]
            else:
                vendor_name = f"Vendor ID {vendor_id} (Unknown)"
            st.write(f"{vendor_name}, Earnings: {earnings}")

        st.write("___")
        st.write("ZINGO EARNINGS")
        st.write("___")

        for vendor_id, earnings in admin_earnings_pervendor.items():
            if vendor_id in vendor_names:
                vendor_name = vendor_names[vendor_id]
            else:
                vendor_name = f"Vendor ID {vendor_id} (Unknown)"
            st.write(f"{vendor_name}, Earnings: {earnings}")

        st.write("___")
        st.write("TOTAL SALE VALUE")
        st.write("___")

        for vendor_id, earnings in total_earnings_pervendor.items():
            if vendor_id in vendor_names:
                vendor_name = vendor_names[vendor_id]
            else:
                vendor_name = f"Vendor ID {vendor_id} (Unknown)"
            st.write(f"{vendor_name}, Earnings: {earnings}")