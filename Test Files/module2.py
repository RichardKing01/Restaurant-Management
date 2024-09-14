
#If your dictionaries are stored in a CSV format, where each row represents a dictionary, you can read them using the csv module in Python. You'll typically have a header row to denote the keys of the dictionary. Here's how you can do it:
import csv

file_path = 'C:/Users/jodya/Desktop/Pythong/Cafe Codes/Cost_Dictionary_Form.csv'

# Open the CSV file in read mode
with open(file_path, 'r', newline='') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Read the header row to get the keys
    keys = next(reader)

    # Iterate over the remaining rows
    for row in reader:
        # Create a dictionary by zipping keys and values
        dictionary = dict(zip(keys, row))

        for key, value in dictionary.items():
            # Try converting the value to an integer
            try:
                dictionary[key] = int(value)
            except ValueError:
                # If conversion fails, keep it as a string
                pass
        print(dictionary)

print(type(dictionary['T']))