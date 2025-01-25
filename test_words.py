from transliterate.base import TranslitLanguagePack, registry

# Define the custom language pack
class CustomRussianLanguagePack(TranslitLanguagePack):
    language_code = "ru"
    language_name = "Russian"
    mapping = {
        "А": "A", "а": "a", "Б": "B", "б": "b", "В": "V", "в": "v",
        "Г": "G", "г": "g", "Д": "D", "д": "d", "Е": "E", "е": "e",
        "Ё": "Yo", "ё": "yo", "Ж": "Zh", "ж": "zh", "З": "Z", "з": "z",
        "И": "I", "и": "i", "Й": "Y", "й": "y", "К": "K", "к": "k",
        "Л": "L", "л": "l", "М": "M", "м": "m", "Н": "N", "н": "n",
        "О": "O", "о": "o", "П": "P", "п": "p", "Р": "R", "р": "r",
        "С": "S", "с": "s", "Т": "T", "т": "t", "У": "U", "у": "u",
        "Ф": "F", "ф": "f", "Х": "Kh", "х": "kh", "Ц": "Ts", "ц": "ts",
        "Ч": "Ch", "ч": "ch", "Ш": "Sh", "ш": "sh", "Щ": "Shch", "щ": "shch",
        "Ъ": "", "ъ": "", "Ы": "Y", "ы": "y", "Ь": "", "ь": "",
        "Э": "Eh", "э": "eh", "Ю": "Yu", "ю": "yu", "Я": "Ya", "я": "ya"
    }

    def __init__(self):
        # Forward translation table
        self.translation_table = self.mapping
        # Reverse translation table
        self.reversed_translation_table = {}
        for k, v in self.mapping.items():
            # Avoid overwriting keys for identical Latin representations
            if v not in self.reversed_translation_table:
                self.reversed_translation_table[v] = k

    def transliterate(self, text, reversed=False):
        """Custom transliteration logic."""
        table = self.reversed_translation_table if reversed else self.translation_table

        # Replace characters using the mapping
        result = ""
        i = 0
        while i < len(text):
            matched = False
            for key in table.keys():
                if text[i : i + len(key)] == key:
                    result += table[key]
                    i += len(key)
                    matched = True
                    break
            if not matched:
                result += text[i]
                i += 1
        return result


# Register the custom language pack
try:
    from transliterate.contrib.languages.ru.translit_language_pack import RussianLanguagePack
    registry.unregister(RussianLanguagePack)
except Exception:
    pass
registry.register(CustomRussianLanguagePack)


# Tests
def test_transliteration_with_custom_pack():
    pack = CustomRussianLanguagePack()
    result = pack.transliterate("Привет", reversed=False)
    assert result == "Privet", f"Expected 'Privet', got '{result}'"

def test_transliteration_reversed_with_custom_pack():
    pack = CustomRussianLanguagePack()
    result = pack.transliterate("Privet", reversed=True)
    assert result == "Привет", f"Expected 'Привет', got '{result}'"

def test_manual_transliteration():
    text = "Привет"
    expected = "Privet"
    mapping = CustomRussianLanguagePack.mapping
    transliteration_table = {k: v for k, v in mapping.items()}
    result = ''.join([transliteration_table.get(char, char) for char in text])
    assert result == expected, f"Expected '{expected}', got '{result}'"

