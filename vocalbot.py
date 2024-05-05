import speech_recognition as sr
import pyttsx3
import csv


def fill_form():
    
    engine = pyttsx3.init()
    
    # Function to get input with feedback
    def get_input(prompt):
        engine.say(prompt)
        engine.runAndWait()
        while True:
            response = get_audio()
            engine.say("You said: " + response)
            engine.runAndWait()
            confirmation = input("Did I understand correctly? (yes/no): ").strip().lower()
            if confirmation == "yes":
                return response
            elif confirmation == "no":
                engine.say("Please try again.")
                engine.runAndWait()
            else:
                engine.say("I didn't understand your response. Please say yes or no.")
                engine.runAndWait()

    # Form filling
    seller_name = get_input("Please say the seller's name.")
    
    engine.say("Please select the processing type: processed or unprocessed.")
    engine.runAndWait()
    processing_type = get_input("Please select the processing type: processed or unprocessed.")
    
    if processing_type.lower() == "unprocessed":
        engine.say("Please select the type of growth: Normal, Bio Fertified, or Hybrid.")
        engine.runAndWait()
        growth_type = get_input("Please select the type of growth: Normal, Bio Fertified, or Hybrid.")
        
        engine.say("Please specify the crop type: Fruits or Grains.")
        engine.runAndWait()
        crop_type = get_input("Please specify the crop type: Fruits or Grains.")
        
        if crop_type.lower() == "fruits":
            engine.say("Please specify the trade unit: Box or Crate.")
            engine.runAndWait()
            trade_unit = get_input("Please specify the trade unit: Box or Crate.")
        elif crop_type.lower() == "grains":
            trade_unit = "Kgs"
        
        engine.say("Please specify the number of units.")
        engine.runAndWait()
        units = get_input("Please specify the number of units.")
        
        engine.say("Please specify the plucking date.")
        engine.runAndWait()
        plucking_date = get_input("Please specify the plucking date.")
        
        engine.say("Please specify the packaging date.")
        engine.runAndWait()
        packaging_date = get_input("Please specify the packaging date.")
        
    elif processing_type.lower() == "processed":
        trade_unit = "Kgs"
        
        engine.say("Please specify the quantity in kgs.")
        engine.runAndWait()
        quantity = get_input("Please specify the quantity in kgs.")
        
        engine.say("Please specify the processing completion date.")
        engine.runAndWait()
        processing_completion_date = get_input("Please specify the processing completion date.")
        
        engine.say("Please specify the packaging date.")
        engine.runAndWait()
        packaging_date = get_input("Please specify the packaging date.")
    
    engine.say("Please specify the origin.")
    engine.runAndWait()
    origin = get_input("Please specify the origin.")
    
    # Write to CSV
    with open('form_responses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([seller_name, processing_type, growth_type, crop_type, trade_unit, units, plucking_date, packaging_date, quantity, processing_completion_date, origin])

if __name__ == "__main__":
    fill_form()
