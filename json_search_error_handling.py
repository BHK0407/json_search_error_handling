import json
import argparse

# Function to load JSON file


def load_json(file_path):
    # Load the JSON file
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: File not found at path {args.file_path}.")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file.")
        return

# Function to recursively search for a word in the JSON data


def search_word(obj, word):
    results = []
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, (dict, list)):
                results.extend(search_word(value, word))
            elif isinstance(value, str) and word in value:
                results.append((key, value))
    elif isinstance(obj, list):
        for item in obj:
            results.extend(search_word(item, word))
    return results

# Function to display search results


def display_result(search_results):
    if not search_results:
        print("No information found for the specified word.")
    else:
        for result in search_results:
            print(f"Key:  {result[0]}, Value: {result[1]}")

# Main function


def main():
    parser = argparse.ArgumentParser(description="Search for a word in a JSON file.")
    parser.add_argument("file_path", nargs="?", default=None, type=str, help="Path to the JSON file.")
    args = parser.parse_args()

    if args.file_path is None:
        args.file_path = input("Enter the path to the JSON file: ")

    data = load_json(args.file_path)
    if data is None:
        return
    #file_path = r"C:\Users\Admin\anaconda3\pkgs\jupyterlab-3.6.3-py311haa95532_0\share\jupyter\lab\static\build_log.json"

    formatted_data = json.dumps(data, indent=2)
    print(formatted_data)

    try:
    # User input for the word to search
        search_word_input = input("Enter a word to search for: ")
    except KeyboardInterrupt:
        print("\nSearch canceled by the user.")
        return
    # Search for the specified word
    search_result = search_word(data, search_word_input)

    # Display the results
    display_result(search_result)

if __name__ == "__main__":
    main()
