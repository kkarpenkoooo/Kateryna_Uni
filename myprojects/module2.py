from deep_translator import GoogleTranslator

def deep_translate(text: str, target_lang: str) -> str:
    try:
        translated = GoogleTranslator(target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"Error: {e}"
