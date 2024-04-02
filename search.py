import os
import sys

def search_files(target_text):
    directory_to_search = './'
    script_name = os.path.basename(__file__)
    for root, dirs, files in os.walk(directory_to_search):
        for file in files:
            if file == script_name:
                continue
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    if target_text.lower() in f.read().lower():
                        print(f"Match found in: {file_path}")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <search_text>")
        sys.exit(1)

    search_text = sys.argv[1]
    search_files(search_text)
