from deep_translator import GoogleTranslator
from langdetect import detect

def TransLate(text: str, src: str, dest: str) -> str:
    try:
        # Виводимо інформацію про процес перекладу
        print(f"Translating from {src} to {dest}: {text[:50]}...")  # Виводимо перші 50 символів тексту для перевірки
        translated = GoogleTranslator(source=src, target=dest).translate(text)
        print(f"Translated text: {translated[:50]}...")  # Виводимо перші 50 символів перекладеного тексту для діагностики
        return translated
    except Exception as e:
        return f"Error: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        detected_lang = detect(text)
        if set == "lang":
            return detected_lang
        elif set == "confidence":
            # Оскільки langdetect не повертає впевненість, повернемо загальне повідомлення
            return "Confidence cannot be calculated with langdetect"
        else:
            return f"Language: {detected_lang}, Confidence: Unknown"
    except Exception as e:
        return f"Error: {e}"

def CodeLang(lang: str) -> str:
    # Отримуємо підтримувані мови з Google Translator
    lang_dict = GoogleTranslator().get_supported_languages(as_dict=True)
    try:
        if lang in lang_dict:
            return lang_dict[lang]
        else:
            inv_lang_dict = {v: k for k, v in lang_dict.items()}
            return inv_lang_dict.get(lang, "Error: Language not found")
    except Exception as e:
        return f"Error: {e}"

def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        lang_dict = GoogleTranslator().get_supported_languages(as_dict=True)
        if out == "screen":
            print(f"{'N':<5} {'Language':<15} {'ISO-639 code':<15} {'Text':<15}")
            print('-' * 50)
            for i, (code, lang) in enumerate(lang_dict.items(), 1):
                translated_text = GoogleTranslator(source='auto', target=code).translate(text) if text else ""
                print(f"{i:<5} {lang:<15} {code:<15} {translated_text:<15}")
            return "Ok"
        elif out == "file":
            with open('languages.txt', 'w', encoding='utf-8') as f:
                f.write(f"{'N':<5} {'Language':<15} {'ISO-639 code':<15} {'Text':<15}\n")
                f.write('-' * 50 + '\n')
                for i, (code, lang) in enumerate(lang_dict.items(), 1):
                    translated_text = GoogleTranslator(source='auto', target=code).translate(text) if text else ""
                    f.write(f"{i:<5} {lang:<15} {code:<15} {translated_text:<15}\n")
            return "Ok"
        else:
            return "Error: Invalid output type"
    except Exception as e:
        return f"Error: {e}"
    