import pandas as pd
from langdetect import detect
from mtranslate import translate

def en_to_tr(text):
    return translate(text, 'tr', 'en')

def split_text(text, split_threshold=2000):
    texts = []
    # split the text by the last '.' after the split_threshold until remaining text is less than split_threshold
    while len(text) > split_threshold:
        last_dot = text[:split_threshold].rfind('.')
        if last_dot == -1:
            last_dot = split_threshold
        texts.append(text[:last_dot+1])
        text = text[last_dot+1:]
    texts.append(text)
    return texts


def tr_if_en(text):
    try:
        detected = detect(text[:min(100, len(text))])
        if detected == 'en':
            return en_to_tr(text)
        else:
            if detected != 'tr':
                print('[WARN]: Detected language is not Turkish or English:', detected)
                return translate(text, 'tr', detected)
            return text
    except:
        return text

def tr_if_en_split(text, split_threshold=2000):
    try:
        detected = detect(text[:min(100, len(text))])
        if detected == 'en':
            return [en_to_tr(t) for t in split_text(text, split_threshold)]
        else:
            if detected != 'tr':
                print('[WARN]: Detected language is not Turkish or English:', detected)
                return [translate(t, 'tr', detected) for t in split_text(text, split_threshold)]
            return [t for t in split_text(text, split_threshold)]
    except:
        return [t for t in split_text(text, split_threshold)]
