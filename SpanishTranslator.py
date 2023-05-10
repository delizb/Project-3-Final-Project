from googletrans import Translator

def translate_to_spanish(text):
    translator = Translator()
    translation = translator.translate(text, dest='es')
    return translation.text

## Prompts user to enter text to translate in the prompt ##

input_text = input("Enter the text you want to translate to Spanish: ")

## Translates the english text into spanish text ##

spanish_text = translate_to_spanish(input_text)

## Prints the translated text ##

print(f"{input_text} in Spanish is {spanish_text}")