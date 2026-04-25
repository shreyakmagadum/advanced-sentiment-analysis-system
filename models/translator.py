from deep_translator import GoogleTranslator
from langdetect import detect

LANG_MAP = {
    "hi": "Hindi",
    "kn": "Kannada",
    "ta": "Tamil",
    "te": "Telugu",
    "ml": "Malayalam",
    "mr": "Marathi",
    "bn": "Bengali",
    "gu": "Gujarati",
    "pa": "Punjabi",
    "ur": "Urdu",
    "en": "English"
}

def translate_to_english(text):
    try:
        lang = detect(text)
        lang_name = LANG_MAP.get(lang, lang)

        if lang != 'en':
            translated = GoogleTranslator(source='auto', target='en').translate(text)
            return translated, lang_name
        else:
            return text, "English"
    except:
        return text, "Unknown"