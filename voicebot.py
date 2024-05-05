# Hindi version
import speech_recognition as sr
import pyttsx3
import csv

def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source) 
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return "Error: " + str(e)


def fill_form_hindi():
    engine = pyttsx3.init()
    
    def get_input(prompt):
        engine.say(prompt)
        engine.runAndWait()
        while True:
            response = get_audio()
            engine.say("आपने कहा: " + response)
            engine.runAndWait()
            confirmation = input("क्या मैंने सही समझा? (हां/नहीं): ").strip().lower()
            if confirmation == "हां":
                return response
            elif confirmation == "नहीं":
                engine.say("कृपया फिर से कोशिश करें।")
                engine.runAndWait()
            else:
                engine.say("मुझे आपके जवाब को समझा नहीं। कृपया हां या नहीं बोलें।")
                engine.runAndWait()

    
    seller_name = get_input("कृपया विक्रेता का नाम बताएं।")
    
    engine.say("कृपया प्रोसेसिंग प्रकार का चयन करें: प्रोसेस्ड या अप्रोसेस्ड।")
    engine.runAndWait()
    processing_type = get_input("कृपया प्रोसेसिंग प्रकार का चयन करें: प्रोसेस्ड या अप्रोसेस्ड।")
    
    if processing_type.lower() == "अप्रोसेस्ड":
        engine.say("कृपया प्रशस्ति प्रकार का चयन करें: सामान्य, बायो सर्टीफाईड या हाइब्रिड।")
        engine.runAndWait()
        growth_type = get_input("कृपया प्रशस्ति प्रकार का चयन करें: सामान्य, बायो सर्टीफाईड या हाइब्रिड।")
        
        engine.say("कृपया फसल का प्रकार निर्दिष्ट करें: फल या अनाज।")
        engine.runAndWait()
        crop_type = get_input("कृपया फसल का प्रकार निर्दिष्ट करें: फल या अनाज।")
        
        if crop_type.lower() == "फल":
            engine.say("कृपया व्यापारिक इकाई निर्दिष्ट करें: बक्सा या क्रेट।")
            engine.runAndWait()
            trade_unit = get_input("कृपया व्यापारिक इकाई निर्दिष्ट करें: बक्सा या क्रेट।")
        elif crop_type.lower() == "अनाज":
            trade_unit = "किलोग्राम"
        
        engine.say("कृपया इकाइयों की संख्या निर्दिष्ट करें।")
        engine.runAndWait()
        units = get_input("कृपया इकाइयों की संख्या निर्दिष्ट करें।")
        
        engine.say("कृपया तोड़ने की तिथि निर्दिष्ट करें।")
        engine.runAndWait()
        plucking_date = get_input("कृपया तोड़ने की तिथि निर्दिष्ट करें।")
        
        engine.say("कृपया पैकेजिंग की तिथि निर्दिष्ट करें।")
        engine.runAndWait()
        packaging_date = get_input("कृपया पैकेजिंग की तिथि निर्दिष्ट करें।")
        
    elif processing_type.lower() == "प्रोसेस्ड":
        trade_unit = "किलोग्राम"
        
        engine.say("कृपया मात्रा को किलोग्राम में निर्दिष्ट करें।")
        engine.runAndWait()
        quantity = get_input("कृपया मात्रा को किलोग्राम में निर्दिष्ट करें।")
        
        engine.say("कृपया प्रोसेसिंग पूर्णता की तिथि निर्दिष्ट करें।")
        engine.runAndWait()
        processing_completion_date = get_input("कृपया प्रोसेसिंग पूर्णता की तिथि निर्दिष्ट करें।")
        
        engine.say("कृपया पैकेजिंग की तिथि निर्दिष्ट करें।")
        engine.runAndWait()
        packaging_date = get_input("कृपया पैकेजिंग की तिथि निर्दिष्ट करें।")
    
    engine.say("कृपया मूल स्थान निर्दिष्ट करें।")
    engine.runAndWait()
    origin = get_input("कृपया मूल स्थान निर्दिष्ट करें।")
    
    # Write to CSV
    with open('form_responses_hindi.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([seller_name, processing_type, growth_type, crop_type, trade_unit, units, plucking_date, packaging_date, quantity, processing_completion_date, origin])

if __name__ == "__main__":
    fill_form_hindi()
