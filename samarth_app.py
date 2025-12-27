import streamlit as st
import pandas as pd

st.title("Project Samarth: Agriculture & Climate Q&A System")

rainfall = pd.read_csv("rainfall.csv")
crops = pd.read_csv("crops.csv")  # Example CSV format as above

st.markdown("""
#### Demo queries:
- Compare the average annual rainfall in two states for last N years, and show top M crops in those states for that period.
- Find the highest and lowest production districts for Crop_Z in two states for the most recent year.
- Show the decadal trend for Crop_Type_C and correlate with rainfall trend.
- Policy advice: Data-backed arguments for promoting Crop_A over Crop_B in a given region.
""")

user_query = st.text_input("Type your question...")

def compare_rainfall_and_top_crops(state1, state2, crop_type, years, top_n):
    # Filter rainfall for both states (your file likely contains only normals, not time-series)
    r1 = rainfall[rainfall["STATE_UT_NAME"].str.upper() == state1.upper()]["ANNUAL"].mean()
    r2 = rainfall[rainfall["STATE_UT_NAME"].str.upper() == state2.upper()]["ANNUAL"].mean()
    # Filter crops
    crop_df = crops[
        (crops["Year"].isin(years)) &
        (crops["Crop"].str.upper() == crop_type.upper()) &
        (crops["State"].str.upper().isin([state1.upper(), state2.upper()]))
    ]
    # Get top M by production for each state
    summary = {}
    for s in [state1.upper(), state2.upper()]:
        top_crops = (
            crop_df[crop_df["State"].str.upper() == s]
            .groupby("Crop")["Production"].sum()
            .sort_values(ascending=False)
            .head(top_n)
        )
        summary[s] = top_crops
    return r1, r2, summary

def find_highest_and_lowest(state_x, state_y, crop, year):
    # Highest in state_x
    sx_df = crops[(crops["State"].str.upper() == state_x.upper()) &
                  (crops["Crop"].str.upper() == crop.upper()) &
                  (crops["Year"] == year)]
    high_x = sx_df.loc[sx_df["Production"].idxmax()]
    sy_df = crops[(crops["State"].str.upper() == state_y.upper()) &
                  (crops["Crop"].str.upper() == crop.upper()) &
                  (crops["Year"] == year)]
    low_y = sy_df.loc[sy_df["Production"].idxmin()]
    return high_x, low_y

def crop_trend_and_correlate(region, crop_type, years):
    # Crop trend
    crop_df = crops[(crops["Crop"].str.upper() == crop_type.upper()) &
                    (crops["State"].str.upper() == region.upper()) &
                    (crops["Year"].isin(years))]
    trend = crop_df.groupby("Year")["Production"].sum()
    # Rainfall: use annual (your file doesn't have yearly data, for demo use the normal)
    r_df = rainfall[rainfall["STATE_UT_NAME"].str.upper() == region.upper()]
    rain_norm = r_df["ANNUAL"].mean()
    return trend, rain_norm

def policy_arguments(region, crop_a, crop_b, years):
    a_df = crops[(crops["Crop"].str.upper() == crop_a.upper()) &
                 (crops["State"].str.upper() == region.upper()) &
                 (crops["Year"].isin(years))]
    b_df = crops[(crops["Crop"].str.upper() == crop_b.upper()) &
                 (crops["State"].str.upper() == region.upper()) &
                 (crops["Year"].isin(years))]
    rain_df = rainfall[rainfall["STATE_UT_NAME"].str.upper() == region.upper()]
    rain_norm = rain_df["ANNUAL"].mean()
    # Generate 3 sample arguments (example logic, expand as needed)
    arg1 = f"{crop_a} yields ({a_df['Production'].mean():.1f}) are higher than {crop_b} ({b_df['Production'].mean():.1f}) in {region.title()}."
    arg2 = f"{crop_a} is less sensitive to rainfall, which is {rain_norm:.1f} mm (compare with crop_b trends)."
    arg3 = f"Promoting {crop_a} increases climate resilience under below-average rainfall."
    return [arg1, arg2, arg3]

# --- DEMO --- Parse placeholder queries and call appropriate functions ---
if user_query:
    st.warning("Demo only. Type query keywords. Advanced NLP parser can be added if requested!")
    # Compare rainfall and crops
    if "compare" in user_query.lower() and "rainfall" in user_query.lower() and "top" in user_query.lower():
        state1 = st.text_input("State 1")
        state2 = st.text_input("State 2")
        crop = st.text_input("Crop Type")
        top_n = st.number_input("Number of top crops per state (M)", value=3)
        start_year = st.number_input("Start Year", value=2015)
        end_year = st.number_input("End Year", value=2020)
        years = list(range(int(start_year), int(end_year)+1))
        if state1 and state2 and crop:
            r1, r2, summary = compare_rainfall_and_top_crops(state1, state2, crop, years, int(top_n))
            st.write(f"Average annual rainfall in {state1}: {r1}")
            st.write(f"Average annual rainfall in {state2}: {r2}")
            st.write("Top crops:")
            st.write(summary)
    # Highest/lowest crop districts
    elif "highest production" in user_query.lower() and "compare" in user_query.lower():
        crop = st.text_input("Crop")
        state_x = st.text_input("State X")
        state_y = st.text_input("State Y")
        year = st.number_input("Year", value=2020)
        if crop and state_x and state_y:
            high_x, low_y = find_highest_and_lowest(state_x, state_y, crop, int(year))
            st.write(f"Highest production for {crop} in {state_x}: {high_x['District']} ({high_x['Production']})")
            st.write(f"Lowest production for {crop} in {state_y}: {low_y['District']} ({low_y['Production']})")
    # Crop trend and correlation
    elif "trend" in user_query.lower() and "correlate" in user_query.lower():
        crop = st.text_input("Crop Type")
        region = st.text_input("Region")
        start_year = st.number_input("Start Year", value=2010)
        end_year = st.number_input("End Year", value=2020)
        years = list(range(int(start_year), int(end_year)+1))
        trend, rain_norm = crop_trend_and_correlate(region, crop, years)
        st.line_chart(trend)
        st.info(f"Average annual rainfall over last decade in {region}: {rain_norm:.1f} mm.")
    # Policy arguments
    elif "policy" in user_query.lower() and "arguments" in user_query.lower():
        region = st.text_input("Region")
        crop_a = st.text_input("Crop Type A")
        crop_b = st.text_input("Crop Type B")
        start_year = st.number_input("Start Year", value=2015)
        end_year = st.number_input("End Year", value=2020)
        years = list(range(int(start_year), int(end_year)+1))
        args = policy_arguments(region, crop_a, crop_b, years)
        for i, arg in enumerate(args, 1):
            st.write(f"{i}. {arg}")
    else:
        st.info("""Please choose one of the demo features: 
        - Compare rainfall/crops, 
        - Find highest/lowest production, 
        - Trend + correlation,
        - Policy arguments.
        NLP pattern matching can be added for natural language queries.
        """)

st.caption("Sources: IMD Rainfall Dataset, Agricultural Crop Production Dataset.")
