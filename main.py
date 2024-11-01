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
    40: "Fresh choice",
    42: "Aha Panipuri",
    43: "Zingo Merchandise"
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
        # Group by vendor_id and sum the relevant columns for each vendor
        total_earnings_per_vendor = df.groupby('vendor_id')['order_amount'].sum()
        total_delivery_fee_per_vendor = df.groupby('vendor_id')['delivery_charge'].sum()

        # Calculate net earnings by subtracting delivery fees from total earnings
        net_earnings_per_vendor = total_earnings_per_vendor - total_delivery_fee_per_vendor

        st.write("___")
        st.write("TOTAL SALE VALUE (Excluding Delivery Fees)")
        st.write("___")
        for vendor_id, earnings in total_earnings_per_vendor.items():
            vendor_name = vendor_names.get(vendor_id, f"Vendor ID {vendor_id} (Unknown)")
            delivery_fee = total_delivery_fee_per_vendor.get(vendor_id, 0)
            net_earnings = net_earnings_per_vendor.get(vendor_id, 0)
            st.write(f"**{vendor_name.upper()}**, Total Earnings: {earnings}, Total Delivery Fee: {delivery_fee}")
            st.write(f"**Net Earnings (Minus Delivery Fee): {net_earnings}**")
            st.write("#################")

        # Display the totals at the bottom
        st.write("___")
        st.write("TOTALS")
        st.write("___")
        total_earnings = total_earnings_per_vendor.sum()
        total_delivery_fees = total_delivery_fee_per_vendor.sum()
        total_net_earnings = net_earnings_per_vendor.sum()
        st.write(f"Total Earnings: {total_earnings}")
        st.write(f"Total Delivery Fees: {total_delivery_fees}")
        st.write(f"Total Net Earnings (Minus Delivery Fees): {total_net_earnings}")
