import pytest
import os
import re
from transliterate import translit

def main():
#File to be opened in non Latin alphabet
    file_Russian         = 'allwordsinalllanguages/Russian/Russian.txt'
    file_English         = 'allwordsinalllanguages/English/English.txt'
    
    # Check if the file exists
    if os.path.exists(file_English):
        try:
            with open(file_English, 'r', encoding='utf-8') as file:
                text = file.read()
                
                if text.strip():
                    print("Original content:")
                    print(repr(text))  # Print the entire content
                    
                    # Clean and process text
                    # Remove unwanted characters but keep commas
                    clean_text = re.sub(r'[^\w\s,]', '', text)  # Remove special characters except commas
                    clean_text = re.sub(r'\s+', ' ', clean_text.strip())  # Normalize spaces

                    # Debug: Display cleaned text
                    print("\nCleaned content:")
                    print(clean_text)
                    
                    # Split the text into words (retaining commas in the original content)
                    words = [word.strip() for word in clean_text.split(',') if word.strip()]

                    # Transliterate each word
                    processed_words = []
                    for word in words:
                        try:
                            transliterated = translit(word, language_code='ru', reversed=False)
                            processed_words.append(f"{word} {transliterated}")
                        except Exception as e:
                            print(f"Error transliterating word '{word}': {e}")
                            processed_words.append(word)  # Keep the original word if transliteration fails
                    
                    # Debug: Display all detected words
                    # print("\nProcessed Words:")
                    # print(", ".join(words))  # Print all words as comma-separated
                    
                    # Count the words
                    num_words = len(words)
                    print(f"\nWord Count: {num_words}")
                else:
                    print("The file is empty.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print(f"File not found: {file_path}")

# Ensure the script runs as main
if __name__ == "__main__":
    main()
