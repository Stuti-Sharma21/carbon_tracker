import streamlit as st
import pandas as pd
import os

st.title("Daily Carbon Tracker ")

st.write("Welcome! Enter your daily activities to calculate your carbon emission.")

km = st.number_input("Kilometers traveled today : ")
electricity = st.number_input("Electricity units used : ")
food = st.selectbox("What meal did you eat today?", ["veg", "non veg"])

if st.button("Calculate Emission"):# for button
    #now button logic
    carbon_emission = 0.2
    unit = 0.8
    daily_limit = 20

    travel_emission = km * carbon_emission
    electricity_emission = electricity * unit

    if food == "veg":
        food_emission = 1
    else:
        food_emission = 3

    total_emission = travel_emission + electricity_emission + food_emission

    st.subheader("Your Daily Emission Report:")
    st.write("Travel emission:", travel_emission, "kg CO₂")
    st.write("Electricity emission:", electricity_emission, "kg CO₂")
    st.write("Food emission:", food_emission, "kg CO₂")
    st.write("Total emission:", total_emission, "kg CO₂")

    if total_emission <= daily_limit:
        credits = (daily_limit - total_emission) * 0.5
        st.success(f"You're under the limit! Credits earned: {credits}")
    else:
        credits = (total_emission - daily_limit) * 0.3
        st.error(f"You exceeded the limit! Credits needed: {credits}")

# Today's data
    data = {
    "km": km,
    "electricity": electricity,
    "food": food,
    "travel_emission": travel_emission,
    "electricity_emission": electricity_emission,
    "food_emission": food_emission,
    "total_emission": total_emission,
    "credits": credits
    }

    #saving new data to csv 

    if os.path.exists("history.csv"): # to check if file exist
        df = pd.read_csv("history.csv") # saves previous day's data
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)  # adds today's data with previous day's data
    else:
        df = pd.DataFrame([data]) # create record if doesnt exist 

    df.to_csv("history.csv",index=False) # to save data 

    st.success("Saved today's record successfully!")



