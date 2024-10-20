import os
from deep_translator import GoogleTranslator
from langdetect import detect

def TransLate(text: str, src: str, dest: str) -> str:
    try:
        # Переклад тексту
        translated = GoogleTranslator(source=src, target=dest).translate(text)
        return translated
    except Exception as e:
        # У випадку помилки повертаємо None
        return None

def LangDetect(text: str) -> str:
    try:
        return detect(text)  # Визначаємо мову
    except Exception as e:
        return f"Error: {e}"

def file_statistics(file_path: str) -> dict:
    """Обчислює і повертає статистику файлу: кількість символів, слів, речень і мову."""
    stats = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        # Статистика файлу
        stats['file_name'] = os.path.basename(file_path)
        stats['file_size'] = os.path.getsize(file_path)  # Розмір файлу в байтах
        stats['char_count'] = len(text)  # Кількість символів
        stats['word_count'] = len(text.split())  # Кількість слів
        stats['sentence_count'] = text.count('.') + text.count('!') + text.count('?')  # Кількість речень
        stats['language'] = LangDetect(text)  # Визначаємо мову

        return stats
    except Exception as e:
        return None

def read_config(file_name: str) -> dict:
    """Зчитує конфігураційний файл і повертає параметри."""
    config = {}
    with open(file_name, 'r') as f:
        for line in f:
            if '=' in line:
                key, value = line.strip().split('=')
                config[key] = value
    return config

def file_translate():
    try:
        # Читаємо конфігураційний файл
        config_file_path = 'files/config.txt'
        config = read_config(config_file_path)
        input_file = config.get('input_file')
        lang_code = config.get('lang_code')
        output_type = config.get('output')

        # Перевіряємо наявність файлу
        input_file_path = f'files/{input_file}'
        if not os.path.exists(input_file_path):
            print(f"Error: File {input_file} not found")
            return

        # Отримуємо статистику файлу
        stats = file_statistics(input_file_path)
        if stats is None:
            print("Error: Could not retrieve file statistics.")
            return

        # Читаємо текст для перекладу
        with open(input_file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        # Переклад тексту
        translated_text = TransLate(text, 'auto', lang_code)

        if translated_text is None:
            print("Error: Translation failed.")
            return

        # Формуємо вміст для виводу або запису у файл
        output_content = (
            f"File size: {stats['file_size']} bytes\n"
            f"Number of characters: {stats['char_count']}\n"
            f"Number of words: {stats['word_count']}\n"
            f"Number of sentences: {stats['sentence_count']}\n"
            f"Language of the text: {stats['language']}\n\n"
            f"Translated text:\n{translated_text}"
        )

        # Виведення результату
        if output_type == 'screen':
            # Відображаємо статистику та перекладений текст на екрані
            print(output_content)
        elif output_type == 'file':
            # Записуємо вміст у файл з доданим кодом мови до назви
            output_file = f'files/{os.path.splitext(input_file)[0]}_{lang_code}.txt'
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(output_content)
            print("Ok")  # На екран виводимо тільки "Ok"
        else:
            print("Error: Invalid output type specified in config")
    except Exception as e:
        print(f"Error: {e}")

file_translate()
