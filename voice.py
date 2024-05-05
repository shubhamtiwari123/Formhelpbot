import speech_recognition as sr
import spacy

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

def extract_information(text):
    doc = nlp(text)
    name = None
    date = None
    quantity = None
    
    # Extracting entities
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            name = ent.text
        elif ent.label_ == 'DATE':
            date = ent.text
        elif ent.label_ == 'CARDINAL':
            quantity = ent.text
    
    return name, date, quantity

# Function to recognize speech using Google Web Speech API
def recognize_speech():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)
    
    print("Processing...")
    
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

# Main function
def main():
    while True:
        print("Please speak the name:")
        name_input = recognize_speech()
        
        if name_input:
            print("Please speak the date:")
            date_input = recognize_speech()
            
            print("Please speak the quantity:")
            quantity_input = recognize_speech()
            
            name, date, quantity = extract_information(name_input), extract_information(date_input), extract_information(quantity_input)
            print("Name:", name[0])
            print("Date:", date[1])
            print("Quantity:", quantity[2])
            print()
            break

if __name__ == "__main__":
    main()
