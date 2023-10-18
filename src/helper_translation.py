

from mtranslate import translate as mtranslate_translate

def translate_to_english(text, src_lang):
    """
    The function `translate_to_english` translates text from a source language to English using the
    `mtranslate_translate` function, unless the source language is already English.
    
    :param text: The text that you want to translate to English
    :param src_lang: The parameter "src_lang" represents the source language of the text that needs to
    be translated
    :return: the translated text if the source language is not English, otherwise it returns the
    original text.
    """
    if src_lang != "en":
        translated_text = mtranslate_translate(text, "en", src_lang)
        return translated_text
    else:
        return text

from mtranslate import translate as mtranslate_translate

def translate_array_to_english(texts, src_lang, length_limit=2000):
    if src_lang != "en":
        max_chunk_length = length_limit  # Maximum character limit per translation request
        translated_texts = []
        current_chunk = []

        for text in texts:
            if len("\n".join(current_chunk)) + len(text) <= max_chunk_length:
                current_chunk.append(text)
            else:
                try:
                    combined_text = "\n".join(current_chunk)  # Combine current chunk texts
                    translated_combined_text = mtranslate_translate(combined_text, 'en', src_lang)
                    translated_texts.extend(translated_combined_text.split("\n"))  # Split the translated text by newlines
                except Exception as e:
                    # Handle translation error (you can log the error or take other actions as needed)
                    print(f"Translation error: {e}")
                    translated_texts.extend(current_chunk)  # Use the original texts in case of error

                current_chunk = [text]  # Start a new chunk with the current text

        # Translate the remaining chunk (if any)
        if current_chunk:
            try:
                combined_text = "\n".join(current_chunk)
                translated_combined_text = mtranslate_translate(combined_text, 'en', src_lang)
                translated_texts.extend(translated_combined_text.split("\n"))
            except Exception as e:
                # Handle translation error (you can log the error or take other actions as needed)
                print(f"Translation error: {e}")
                translated_texts.extend(current_chunk)  # Use the original texts in case of error

        return translated_texts
    else:
        return texts
