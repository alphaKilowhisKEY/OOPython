# Personalized Letter Generator

## Description
This Python script generates personalized letters for a list of names by replacing a placeholder in a template letter with each name. It reads a list of names from a file and a template letter from another file, creates individualized letters for each name, and saves them to separate files.

## Features
- **Placeholder Replacement**: The script replaces a placeholder in the template letter with each name from the list.
- **Input Files**: It reads the list of names from the "Input/Names/invited_names.txt" file and the template letter from the "Input/Letters/starting_letter.txt" file.
- **Output Files**: It saves the personalized letters to individual files in the "Output/ReadyToSend" directory, with filenames indicating the recipient's name.

## Usage
1. Place the list of names in the "Input/Names/invited_names.txt" file.
2. Create the template letter in the "Input/Letters/starting_letter.txt" file, replacing the placeholder "[name]" with the desired placeholder for the recipient's name.
3. Run the script to generate personalized letters.
4. Find the generated letters in the "Output/ReadyToSend" directory, each named according to the recipient's name.

## Example
Suppose the "invited_names.txt" file contains the names "John Doe" and "Jane Smith", and the "starting_letter.txt" file contains the following text:
