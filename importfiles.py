import os
import psycopg2

# Database connection
conn = psycopg2.connect(
    dbname='languages',
    user='user',
    password = 'password',
    host='localhost',
    port='5432'
)
cur = conn.cursor()

# Generator to yield words from a file
def word_generator(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = [word.strip() for word in line.strip().split(',') if word.strip()]
            for word in words:
                yield word

root_dir = '/home/jai/projects/languages/allwordsinalllanguages'

# Traverse through the root directory and its subdirectories
for dirpath, dirnames, filenames in os.walk(root_dir):
    for file in filenames:
        if file.endswith('.txt'):
            file_path = os.path.join(dirpath, file)
            table_name = os.path.splitext(file)[0]  # Remove .txt for the table name

            try:
                # ✅ Create table if it doesn't exist
                cur.execute(f"""
                    CREATE TABLE IF NOT EXISTS public."{table_name}" (
                        id SERIAL PRIMARY KEY,
                        "Words" TEXT NOT NULL
                    );
                """)
                conn.commit()

                # ✅ Insert words into the table
                words = list(word_generator(file_path))
                print(f"Inserting {len(words)} words into table: {table_name}")

                if words:
                    batch_size = 10000  # Insert in batches
                    for i in range(0, len(words), batch_size):
                        batch = words[i:i+batch_size]
                        try:
                            cur.executemany(
                                f'INSERT INTO public."{table_name}" ("Words") VALUES (%s);',
                                [(word,) for word in batch]
                            )
                            conn.commit()  # Commit after each batch
                            print(f"Inserted batch {i // batch_size + 1} ({len(batch)} words) into {table_name}")
                        except Exception as insert_error:
                            print(f"Error inserting batch into {table_name}: {insert_error}")
                            conn.rollback()  # Rollback on error
                else:
                    print(f"No words found in file: {file_path}")

            except Exception as e:
                print(f"Error processing {file_path}: {e}")
                conn.rollback()  # Rollback in case of error

# Close the database connection
cur.close()
conn.close()
