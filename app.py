# Distance Converter Function
import streamlit as st
def distance_convertor(from_unit, to_unit,value):
    units = {
        "Meters": 1,
        "Kilometers": 1000,
        "Miles": 1609.34,
        "Feet": 0.3048,
    }
    result = value * units[from_unit] / units[to_unit]
    return result
#  Temperatur Convertor Function
def temperatur_convertor(from_unit, to_unit,value):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32 
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (value - 32) * 5/9
    else:
        result = value
    return result    

#  Weight Convertor Function
def weigth_convertor(from_unit, to_unit,value):
    units = {
        "Kilometers": 0.001,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# Pressure Convertor Function
def pressure_convertor(from_unit, to_unit,value):
    units = {
        "Pascals": 1,
        "Hectopascals": 100,
        "Kilopascals": 1000,
        "Bar": 100000,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# Streamlit UI
st.title("🌐 Unit Converter App")

category = st.selectbox("Select Category", ["Distance", "Temperature", "Weight", "Pressure"])

if category == "Distance":
   from_unit = st.selectbox("From", ["Meters", "Kilometers", "Miles", "Feet"])
   to_unit = st.selectbox("To", ["Meters", "Kilometers", "Miles", "Feet"])
   value = st.number_input("Enter Value")
   if st.button("Convert"):
    result = distance_convertor (from_unit, to_unit, value)
    st.success(f"{value} {from_unit} = {result: .2f} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
     result = temperatur_convertor(from_unit, to_unit, value)
     st.success(f"{value} {from_unit} = {result: .2f} {to_unit}")
 

elif category == "Weight":
    from_unit = st.selectbox("From",["Kilometers", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("To", ["Kilometers", "Grams", "Pounds", "Ounces"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
     result = weigth_convertor(from_unit, to_unit, value)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Pressure":
    from_unit = st.selectbox("From", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    to_unit = st.selectbox("To", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
     result = pressure_convertor(from_unit, to_unit, value)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
