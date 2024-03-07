import json

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
def display_results(search_results):
    if not search_results:
        print("No information found for the specified word.")
    else:
        for result in search_results:
            print(f"Key: {result[0]}, Value: {result[1]}")

# Main function
def main():
    # Load the JSON file
    file_path = 'your_file.json'  # Replace with the actual path to your JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # User input for the word to search
    search_word_input = input("Enter the word to search: ")

    # Search for the specified word
    search_results = search_word(data, search_word_input)

    # Display the results
    display_results(search_results)

if __name__ == "__main__":
    main()