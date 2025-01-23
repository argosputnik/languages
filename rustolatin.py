import os
import re
from transliterate import translit

def main():
    file_path = 'allwordsinalllanguages/Russian/Russian.txt'
    
    # Check if the file exists
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
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

                    
                    # Debug: Display all detected words
                    print("\nProcessed Words:")
                    print(", ".join(words))  # Print all words as comma-separated
                    
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
