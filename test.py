from transliterate import translit,  get_available_language_codes

# Test with another language like Armenian ('hy')
try:
    print(translit("Բարեւ", 'hy'))  # Should output 'Barev'
except Exception as e:
    print(f"Error: {e}")

