import os
import pandas as pd
import json

# Directory containing the JSON files
folder_path = './pages'

# List to hold individual DataFrames
df_list = []

# Loop through all files in the directory
for file_name in os.listdir(folder_path):
    if file_name.endswith('.json'):
        file_path = os.path.join(folder_path, file_name)

        # Load the JSON data
        with open(file_path, 'r', encoding='windows-1251') as file:
            data = json.load(file)

        # Normalize the JSON data to create a DataFrame
        df = pd.json_normalize(data)

        # Add the DataFrame to the list
        df_list.append(df)

# Concatenate all DataFrames into a single DataFrame
final_df = pd.concat(df_list, ignore_index=True)

# Save the concatenated DataFrame to a CSV file
final_df.to_csv('combined_output.csv', index=False, encoding='utf-8')

print("CSV file created successfully!")