import re

def count_vowels(text: str) -> int:
    if text is None: raise TypeError("Input cannot be None")
    return len(re.findall(r'[aeiou]', text, re.IGNORECASE))

def reverse_string(text: str) -> str:
    if text is None: raise TypeError("Input cannot be None")
    return text[::-1]

def is_palindrome(text: str) -> bool:
    if text is None: raise TypeError("Input cannot be None")
    clean_text = "".join(text.split()).lower()
    return clean_text == clean_text[::-1]

def word_count(text: str) -> int:
    if text is None: raise TypeError("Input cannot be None")
    return len(text.split())

def capitalise_words(text: str) -> str:
    if text is None: raise TypeError("Input cannot be None")
    return " ".join(word.capitalize() for word in text.split())

def remove_duplicates(text: str) -> str:
    if text is None: raise TypeError("Input cannot be None")
    if not text: return ""
    result = [text[0]]
    for i in range(1, len(text)):
        if text[i] != text[i-1]:
            result.append(text[i])
    return "".join(result)