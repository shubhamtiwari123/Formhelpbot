import streamlit as st
import datetime
import speech_recognition as sr
import pyttsx3

def get_audio_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source) 
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("User said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Error:", str(e))
        return ""

def voice_input(prompt, engine):
    st.write(prompt)
    engine.say(prompt)
    engine.runAndWait()
    response = get_audio_input()
    
    if not response:
        retry = st.radio("Retry?", ("Yes", "No"))
        if retry == "Yes":
            return voice_input(prompt, engine)
        else:
            return None
    
    return response

def crop_selling_form():
    st.title("Crop Selling Form")

    engine = pyttsx3.init()

    seller_name = voice_input("Please say the seller's name.", engine)
    if seller_name:
        st.text_input("Seller Name", seller_name)

    process_type = voice_input("Is the crop processed or unprocessed?", engine)
    if process_type:
        process_type = "Unprocessed" if "unprocessed" in process_type.lower() else "Processed"
        st.radio("Process Type", ("Processed", "Unprocessed"), index=1 if process_type == "Unprocessed" else 0)

    if process_type == "Unprocessed":
        growth_type = voice_input("Please specify the growth type.", engine)
        if growth_type:
            st.selectbox("Growth Type", ("Normal", "Bio Fertilized", "Hybrid"))

        crop_type = voice_input("Please specify the crop type.", engine)
        if crop_type:
            crop_type = "Fruits" if "fruits" in crop_type.lower() else "Grains"
            st.selectbox("Crop Type", ("Fruits", "Grains"), index=0 if crop_type == "Fruits" else 1)

        if crop_type == "Fruits":
            trade_unit = voice_input("Please specify the trade unit.", engine)
            if trade_unit:
                trade_unit = "Box" if "box" in trade_unit.lower() else "Crate"
                st.selectbox("Trade Unit", ("Box", "Crate"), index=0 if trade_unit == "Box" else 1)

            trade_quantity = voice_input("Please specify the number of units.", engine)
            if trade_quantity:
                st.slider("Number of Units", 1, 1000)

        elif crop_type == "Grains":
            trade_quantity = voice_input("Please specify the trade quantity in kilograms.", engine)
            if trade_quantity:
                st.slider("Trade Quantity (Kgs)", 1, 1000)

        plucking_date = voice_input("Please specify the plucking date.", engine)
        if plucking_date:
            st.date_input("Plucking Date", datetime.date.today())

        packaging_date = voice_input("Please specify the packaging date.", engine)
        if packaging_date:
            st.date_input("Packaging Date", datetime.date.today())

    elif process_type == "Processed":
        trade_quantity = voice_input("Please specify the trade quantity in kilograms.", engine)
        if trade_quantity:
            st.slider("Trade Quantity (Kgs)", 1, 1000)

        process_complete_date = voice_input("Please specify the processing complete date.", engine)
        if process_complete_date:
            st.date_input("Processing Complete Date", datetime.date.today())

        packaging_date = voice_input("Please specify the packaging date.", engine)
        if packaging_date:
            st.date_input("Packaging Date", datetime.date.today())

    origin = st.selectbox("Origin", options=[
        "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
        "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
        "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
        "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
    ], index=0, label="Please specify the origin.")

    submit_button = st.button("Submit")

    if submit_button:
        st.success("Form Submitted Successfully!")

if __name__ == "__main__":
    crop_selling_form()
